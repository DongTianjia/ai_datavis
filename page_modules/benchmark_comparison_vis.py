import streamlit as st
import plotly.graph_objects as go
import pandas as pd
from data_loader import load_benchmark_data

# Load cached benchmark data
model_scores = load_benchmark_data()

# Ensure at least one model exists
if not model_scores:
    st.error("❌ No benchmark data found. Check your Airtable permissions and API setup.")
    st.stop()

# 🔍 Dynamically get all available benchmark tasks
all_benchmarks = set()
for model in model_scores.values():
    all_benchmarks.update(model.keys())  # Collect all unique benchmark task names

# **Manually define readable names & descriptions for benchmarks**
benchmark_info = {
    "bench.task.hendrycks_math.hendrycks_math_lvl_5": {
        "name": "Hendrycks Math (Lvl 5)",
        "description": "A challenging mathematical reasoning test for AI, evaluating complex problem-solving skills in algebra, calculus, and geometry."
    },
    "bench.task.gpqa.gpqa_diamond": {
        "name": "GPQA Diamond",
        "description": "Generalized Question-Answering benchmark designed to test AI reasoning across multiple domains, including history, science, and logic."
    },
    "bench.task.otis_mock_aime.otis_mock_aime_24_25": {
        "name": "OTIS Mock AIME",
        "description": "A simulated American Invitational Mathematics Examination (AIME) test used for evaluating mathematical aptitude in high school-level AI models."
    },
    "bench.task.frontiermath.frontiermath_2025_02_28_private": {
        "name": "FrontierMath (Private)",
        "description": "A private leaderboard for high-stakes mathematical reasoning challenges, testing AI performance on cutting-edge mathematical research problems."
    },
    "bench.task.frontiermath.frontiermath_2025_02_28_public": {
        "name": "FrontierMath (Public)",
        "description": "A public benchmark that evaluates AI models on complex mathematical reasoning using recent competition-grade problem sets."
    },
    # Add more mappings as needed
}

# Convert set to a sorted list
benchmark_metrics = sorted(list(all_benchmarks))

# Sort model names alphabetically
sorted_model_list = sorted(model_scores.keys())

# **Replace technical names with readable names**
readable_benchmarks = [benchmark_info.get(metric, {"name": metric})["name"] for metric in benchmark_metrics]

# Streamlit UI
st.title("📊 AI Model Benchmark Performance Radar Chart")
st.markdown("AI benchmarks are different ways to evaluate the performance of AI mmodels. The aim is to provide more transparent, systematic, and up-to-date evaluations of AI model capabilities. See below for descriptions of different benchmarks we use here:")

# **🔎 Display Benchmark Descriptions for Context**
st.subheader("Benchmark Descriptions")
for metric in benchmark_metrics:
    readable_name = benchmark_info.get(metric, {"name": metric})["name"]
    description = benchmark_info.get(metric, {"description": "No description available."})["description"]

    st.markdown(f"**{readable_name}**: {description}")

# 👉 Move selection to Sidebar with sorted options
st.sidebar.header("Model Selection")
model_selection = st.sidebar.selectbox("Select AI Model:", sorted_model_list, index=0)

# Prepare Data for Radar Chart
selected_scores = [model_scores[model_selection].get(metric, 0) for metric in benchmark_metrics]

# Convert scores to **strings** to prevent ArrowTypeError
display_scores = [("Unavailable" if score == 0 else f"{score:.4f}") for score in selected_scores]

# Create Radar Chart with **Readable Labels**
fig = go.Figure()
fig.add_trace(go.Scatterpolar(
    r=selected_scores,
    theta=readable_benchmarks,  # ✅ Show human-readable benchmark names
    fill='toself',
    name=model_selection
))

fig.update_layout(
    polar=dict(radialaxis=dict(visible=True, range=[0, 1])),
    showlegend=True
)

st.subheader(f"Performance of {model_selection}")
st.markdown("Select the model name you want to test benchmark performance for in the sidebar on the left.")
# Display Radar Chart
st.plotly_chart(fig)

# **Display Model Scores as Table with Readable Labels**
st.subheader(f"Benchmark Scores for {model_selection}")
df_scores = pd.DataFrame({
    "Benchmark": readable_benchmarks,  # ✅ Show readable benchmark names
    "Score": display_scores
}, dtype=str)  # ✅ Explicitly define column type as string

st.dataframe(df_scores)
st.markdown("📌 **Data Source:** [Epoch AI Benchmark Performance](https://github.com/epoch-research/epochai-python)")
