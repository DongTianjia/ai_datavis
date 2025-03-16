import streamlit as st
import pandas as pd
import ssl
from epochai.airtable.models import MLModel, BenchmarkRun, Score

ssl._create_default_https_context = ssl._create_stdlib_context

# CSV Data URL
DATA_URL = 'https://epoch.ai/data/large_scale_ai_models.csv'


# ✅ Cache CSV Data for 24 Hours
@st.cache_data(ttl=86400)
def load_data():
    """Load AI model dataset from CSV."""
    df = pd.read_csv(DATA_URL)
    return df

# ✅ Cache Benchmark Data for 24 Hours
@st.cache_data(ttl=86400)
def load_benchmark_data():
    # Fetch data from Airtable
    models = MLModel.all(memoize=True)
    benchmark_runs = BenchmarkRun.all(memoize=True)
    scores = Score.all(memoize=True)

    # Map models to their benchmark scores
    model_scores = {}
    for run in benchmark_runs:
        # ✅ Use `model_id` instead of `name`
        if run.model and run.model.model_id:
            model_name = run.model.model_id
        else:
            model_name = f"Unknown Model ({run.id})"  # Debugging info

        if model_name not in model_scores:
            model_scores[model_name] = {}  # Ensure key exists

        # ✅ Ensure correct benchmark-score mapping
        for score in scores:
            if score.benchmark_run.id == run.id:
                benchmark_name = getattr(score.benchmark_run.task, "path", "Unknown Benchmark")

                # ✅ Only store valid scores
                if score.mean is not None:
                    model_scores[model_name][benchmark_name] = score.mean
                else:
                    model_scores[model_name][benchmark_name] = 0  # Default if no score

    return model_scores
