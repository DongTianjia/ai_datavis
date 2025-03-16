import streamlit as st

st.set_page_config(
    page_title="Explore the Landscape of AI",
    page_icon="🚀",
)

# 📊📈📉🧠

# Define the pages with improved titles and icons
main_page = st.Page("page_modules/homepage.py", title="Welcome", icon="🏡")
page_2 = st.Page("page_modules/dashboard.py", title="AI Landscape Dashboard", icon="🌎")
page_3 = st.Page("page_modules/feature_comparison_vis.py", title="AI Feature Comparison", icon="📊")
page_4 = st.Page("page_modules/benchmark_comparison_vis.py", title="AI Benchmark Performance", icon="🏆")
page_5 = st.Page("page_modules/conclusion.py", title="Reflections", icon="🤔")

# Set up navigation
pg = st.navigation([main_page, page_2, page_3, page_4, page_5])

# Run the selected page
pg.run()
