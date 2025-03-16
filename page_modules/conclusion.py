import streamlit as st

st.title("🤔 Reflections")

## 🔍 Summary of Findings
st.subheader("🔍 Key Takeaways from the Data")
st.markdown("""
Through the interactive dashboard, we’ve explored **how AI models have evolved over time**, including:
- 🌍 **Global Distribution:** AI model development is dominated by a few key countries, but more regions are entering the space.
- 🏛️ **Who Builds AI?** Industry leads AI development, but academia still plays a crucial role.
- 📈 **Trends Over Time:** The number of AI models has **surged in recent years**, reflecting rapid innovation.
- 🏆 **Benchmark Performance:** AI models vary significantly in performance across different tasks.

This data highlights the **growth, distribution, and technological advancements** in AI models.
""")

st.divider()

## 📌 Methodology Explanation
st.subheader("📊 Methodology & Data Processing")

### 🔹 Why These Visualizations?
st.markdown("""
The data visualizations were designed to **effectively convey key insights** from the AI model dataset. Each visualization serves a specific purpose:

- **Bar Charts (Country & Organization Type)** → Shows AI model distribution **by region & industry**.
- **Pie Chart (Model Domains)** → Highlights **categorical breakdowns** of AI use cases.
- **Line Chart (Publication Trends)** → Tracks **historical AI development** over time.
- **Scatter Plot (Feature Comparison)** → Enables **custom analysis** of AI model attributes.
- **Radar Chart (Benchmark Performance)** → Compares models across multiple performance metrics, having hover-over details for each model.
""")

### 🔹 Data Preparation & Cleaning
st.markdown("""
Before visualizing, the dataset underwent several **data preprocessing steps**:
- **Standardizing Date Formats** → Ensuring publication dates were consistent.
- **Exploding Multi-Value Columns** → Splitting columns with multiple values (e.g., countries, organization types) for accurate counting.
- **Filtering & Cleaning** → Removing unnecessary columns and handling missing values.
- **Ensuring Numeric Data** → Converting relevant fields into **integer/float types** for plotting.
""")

st.divider()

## ⚠️ Limitations & Challenges
st.subheader("⚠️ Challenges & Limitations")
st.markdown("""
While these datavisualizations provides **valuable insights**, it has certain limitations:

- **📊 Data Gaps** → Some AI models lack publicly available details on **compute, dataset size, and benchmarking results**.
- **🏆 Benchmarking Complexity** → Different AI tasks use **varying evaluation methods**, making direct comparisons difficult. Future work could include a deeper analysis of **which models perform best for different AI tasks using task-specific benchmarks for analysis**.
- **🌱 Ethical Blind Spots** → This analysis does not currently assess **AI fairness, environmental impact like energy & resource consumption for training** - topics for my future explorations :)
""")

st.divider()

## 💡 Personal Reflection
st.subheader("💡 What I Learned from This Project")
st.markdown("""
Building this AI landscape dashboard was a journey in **data visualization, AI analysis, and interactive storytelling**.
Some key lessons from this project include:
- 📌 **Data preprocessing** is crucial for ensuring accuracy in visualizations.
- 📌 **Interactivity enhances exploration**, making complex data more accessible.
- 📌 **AI trends reveal fascinating insights**, such as how different countries and industries contribute to AI progress.

Ultimately, this project helped me **merge my technical skills with my passion for AI research**, making AI trends **more transparent and accessible**.
""")

st.divider()

## 📌 Final Acknowledgment
st.markdown("""
🔹 **Thank you for exploring this AI dashboard!**
🔹 **Created by:** [Lily Dong](http://www.linkedin.com/in/tianjia-dong)
🔹 **Feedback?** [Email Me](lilydong@uchicago.edu)
""")
