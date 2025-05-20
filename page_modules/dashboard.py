import streamlit as st
import pandas as pd
import plotly.express as px
from data_loader import load_data

st.title("🌍 AI Landscape Dashboard")
st.markdown("""
Artificial intelligence has seen **rapid growth**, with models being developed across different domains, institutions, and geographies.
This dashboard provides an **interactive** exploration of AI development trends, including:
- **Who develops AI models?** (countries, institutions)
- **What are AI models used for?** (domains, applications)
- **How has AI evolved over time?** (publication trends)
""")

st.divider()


# Load data
df = load_data()
df["Publication date"] = pd.to_datetime(df["Publication date"], errors="coerce")

# Helper function to parse, explode columns, and remove original rows
def parse_and_explode(df, column):
    """Splits comma-separated values in a column into multiple rows and removes original list-based rows."""
    df = df.dropna(subset=[column]).copy()

    # Create a mask to identify rows that contain lists (multiple values)
    mask = df[column].str.contains(",", regex=False, na=False)

    # Explode only the rows that contained lists
    df_exploded = df[mask].copy()
    df_exploded[column] = df_exploded[column].str.split(",")
    df_exploded = df_exploded.explode(column)

    # Remove original rows with lists and combine with exploded DataFrame
    df_cleaned = pd.concat([df[~mask], df_exploded], ignore_index=True)

    # Strip whitespace from values
    df_cleaned[column] = df_cleaned[column].str.strip()

    return df_cleaned

# Apply cleaning to key categories
df_country_expanded = parse_and_explode(df, "Country (of organization)")
df_domain_expanded = parse_and_explode(df, "Domain")
df_org_expanded = parse_and_explode(df, "Organization categorization (from Organization)")

# Key Statistics (Using Cleaned Data)
st.subheader("Key Statistics")
col1, col2, col3 = st.columns(3)
col1.metric("Total Models", len(df))
col2.metric("Unique Domains", df_domain_expanded["Domain"].nunique())
col3.metric("Countries Involved", df_country_expanded["Country (from Organization)"].nunique())

st.subheader("Key Plots")
# Layout for displaying graphs in two rows with two columns each
col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

# AI Models by Country
with col1:
    fig_country = px.bar(
        df_country_expanded["Country (from Organization)"].value_counts().reset_index(),
        x="Country (from Organization)",
        y="count",
        labels={"Country (from Organization)": "Country", "count": "Number of AI Models"},
        title="AI Models by Country"
    )

    fig_country.update_layout(
        xaxis_title="Country",  # ✅ X-Axis Label Added
        yaxis_title="Number of AI Models",
        xaxis_tickangle=-45  # ✅ Rotates labels for better readability
    )

    st.plotly_chart(fig_country, use_container_width=True)


# AI Models by Domain
with col2:
    fig_domain = px.pie(df_domain_expanded["Domain"].value_counts(),
                        names=df_domain_expanded["Domain"].value_counts().index,
                        values=df_domain_expanded["Domain"].value_counts().values,
                        title="AI Models by Domain")
    st.plotly_chart(fig_domain, use_container_width=True)

# AI Model Publications Over Time
with col3:
    time_series = df.groupby(df["Publication date"].dt.year).size()
    fig_time = px.line(x=time_series.index, y=time_series.values,
                       labels={'x': 'Year', 'y': 'Number of AI Models'}, title="AI Model Publications Over Time")
    st.plotly_chart(fig_time, use_container_width=True)

# AI Models by Organization Type
with col4:
    fig_org = px.bar(df_org_expanded["Organization categorization (from Organization)"].value_counts(),
                     labels={'index': 'Organization Type', 'value': 'Number of AI Models'}, title="AI Models by Organization Type")
    st.plotly_chart(fig_org, use_container_width=True)

st.markdown("📌 **Data Source:** **Epoch AI** [Data on AI](https://epoch.ai/data), data is fetched and updated every 24 hrs.")