import streamlit as st
import pandas as pd
from data_loader import load_data

# Page title
st.title("Explore the Landscape of AI 🚀")
st.write("")

# Load & Display Profile Picture (Replace 'profile.jpg' with your actual file)
col1, col2 = st.columns([1, 3])
with col1:
    st.image("pictures/author_thumbnail.jpg", use_container_width=True)
    st.write("")  # Another empty space to balance alignment
with col2:
    st.markdown(
        """
        **Hi, my name is Lily :)**

        With an information science background and currently doing research in digital humanities at UChicago, my work spans **AI research, digital knowledge representation, and computational data analysis**.
        This project combines my passion for **data visualization and AI** to make complex AI data more accessible for the public. [Question or Feedback?](lilydong@uchicago.edu)
        """
    )
st.divider()

# 📌 **Navigation & Interactive Features**
st.subheader("🖥️ About the Project ")
st.markdown(
    """
    In recent years, **AI models have evolved rapidly**, but understanding their capabilities,
    development, and impact remains **challenging**.
    This visualization project aims to:
    - **Simplify AI model trends** through **interactive charts**.
    - **Provide insights** into **model benchmarks & technical specifications**.
    - **Help users navigate AI complexity** with **intuitive visual exploration**.

    Whether you're a **researcher, developer, or enthusiast**, this tool will help you understand **AI's growth & influence**.
    """
)
st.markdown(
    """
    This project contains several sections to help you explore the AI landscape:
    - **AI Landscape & Trends:** Explore general AI model statistics and historical trends.
    - **Feature Comparison:** Compare AI models by selecting different technical features (e.g., parameters vs. training time).
    - **Benchmark Performance:** See how models perform on various AI benchmarks using a radar chart.
    - **Understanding AI Impact:** Read insights into what these trends mean for AI development;

    as well as some interactive features to enhance your experience:
    - **Dropdown Filters:** Use the sidebar to select **specific AI models or features** to compare.
    - **Hover for Details:** Move your cursor over **charts and graphs** for additional insights.
    - **Clickable Navigation:** Use the top menu to quickly jump between sections.
    """
)

st.divider()

# 📌 **Data Source Section**
st.subheader("📊 About the Data")
st.markdown(
    """
    The data used in this project comes from **Epoch AI**
    [Data on AI](https://epoch.ai/data),
    as well as [Airtable database of ML models and benchmark results](https://github.com/epoch-research/epochai-python) through Epoch AI's open-source Python client library.

    The dataset includes:
    - **Development Information:** Who built the models, their training resources, and when they were published.
    - **Model Specifications:** Number of parameters, accessibility, and hardware usage.
    - **Benchmark Performance:** Model accuracy on various AI evaluation benchmarks (e.g., Hendrycks Math, GPQA).
    """
)

st.divider()

# Load Data & Display a Preview
st.subheader("📄 Sample Data Preview")
st.write("Below is a quick preview of the dataset used for analysis:")
df = load_data()
st.dataframe(df.head())

st.markdown("📌 **Data Source:** [Epoch AI Large-Scale AI Models Dataset](https://epoch.ai/data/large_scale_ai_models.csv)")
