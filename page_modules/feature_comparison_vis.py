import streamlit as st
import pandas as pd
import plotly.express as px
from data_loader import load_data

st.title("📊 Feature Comparison")

st.markdown("""
### 🔍 Explore AI Model Relationships
This interactive tool allows you to **compare different AI model features** and analyze how they relate to each other.
- Select **two numerical features** (e.g., Model Size, Training Data, Compute)
- Adjust the **log scale option** to explore trends across different magnitudes
- Hover over points to see **specific model details**

👉 Try different feature combinations to uncover hidden insights!
""")


# Load data
df = load_data()

# Ensure numeric columns are available, excluding unnecessary ones
exclude_columns = ["Citations", "Training compute (FLOP)", "Finetune compute (FLOP)", "Base model"]
numeric_columns = [col for col in df.select_dtypes(include=['float64', 'int64']).columns if col not in exclude_columns]

# Ensure "Publication Date" is available
if "Publication date" in df.columns:
    numeric_columns.append("Publication date")

# Default selections
default_x = "Publication date" if "Publication date" in numeric_columns else numeric_columns[0]
default_y = "Parameters" if "Parameters" in numeric_columns else numeric_columns[1]

if len(numeric_columns) < 2:
    st.warning("Not enough numeric columns available for comparison.")
else:
    # Sidebar Filters
    st.sidebar.header("Feature Selection")
    x_feature = st.sidebar.selectbox("Select X-axis feature", numeric_columns, index=numeric_columns.index(default_x))
    y_feature = st.sidebar.selectbox("Select Y-axis feature", numeric_columns, index=numeric_columns.index(default_y))

    # Handle log scaling
    log_scale = st.sidebar.checkbox("Use Log Scale (X-axis)", value=False)

    # Scatter plot
    st.subheader("Scatter Plot")
    st.markdown("""
Each **dot** in the scatter plot represents an AI model. Position of the dot shows how the two selected features relate, and hover over to see the model’s name for further exploration
""")

    fig_scatter = px.scatter(df, x=x_feature, y=y_feature, title=f"{x_feature} vs {y_feature}",
                             log_x=log_scale, hover_name="Model")

    st.plotly_chart(fig_scatter)

st.markdown("📌 **Data Source:** [Epoch AI Benchmark Performance](https://github.com/epoch-research/epochai-python)")