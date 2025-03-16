# AI Landscape Dashboard

## 📌 Overview
The **AI Landscape Dashboard** is an interactive visualization platform that provides insights into the development, deployment, and performance of AI models. This project aggregates data from various sources to help researchers, developers, and enthusiasts explore AI trends, model capabilities, and benchmark performance. Explore the [web app](https://explorethelandscapeofai.streamlit.app/)!

## 🚀 Features
- **AI Landscape & Trends** 🌎: Explore AI model distributions by country, domain, and organization type.
- **Feature Comparison** 📊: Compare model attributes like parameter count, dataset size, and training time.
- **Benchmark Performance** 🏆: Visualize AI models' performance across various benchmarks.
- **Interactive Elements** 🎛️:
  - Hover for additional insights.
  - Sidebar filters to refine data selection.
  - Log scale toggle for better trend analysis.

## 📊 Data Sources
- **Model Metadata:** [Epoch AI Large-Scale AI Models](https://epoch.ai/data/large_scale_ai_models.csv)
- **Benchmark Performance:** [Epoch AI Benchmark Dataset](https://github.com/epoch-research/epochai-python)
- **Additional Data Processing:** Airtable API integration.

## 🛠️ Installation & Usage
### 1️⃣ Clone the Repository
```bash
git clone [https://github.com/your-repo/ai-landscape-dashboard.git](https://github.com/DongTianjia/ai_datavis.git)
cd ai-landscape-dashboard
```

### 2️⃣ Set Up a Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3️⃣ Install Dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set Up Environment Variables
- Create a `.env` file in the project root directory, find instructions on how to copy Epoch AI's Airtable database and creating API key and ID [here](https://github.com/epoch-research/epochai-python/tree/main)
  ```ini
  AIRTABLE_PERSONAL_ACCESS_TOKEN=your_airtable_api_personal_access_token
  AIRTABLE_BASE_ID=your_airtable_base_id
  ```
  
### 5️⃣ Run the Application
```bash
streamlit run app.py
```

---

## 🔍 Methodology
### **Visualization Selection**
- **Bar Charts**: Used for categorical comparisons (e.g., model distribution by country).
- **Line Charts**: Show trends over time (e.g., AI model publications over time).
- **Scatter Plots**: Display feature correlations (e.g., parameter count vs. dataset size).
- **Radar Charts**: Used to visualize model performance across multiple benchmarks.

### **Data Preparation**
- Cleaned and parsed categorical values for better filtering.
- Exploded list-based fields into separate rows to improve visualization accuracy.
- Normalized benchmark scores for consistent comparison.

---

## 🔬 Critical Analysis
### **Limitations**
- Some models lack metadata, affecting visualization completeness.
- Benchmark scores may vary based on dataset versions and evaluation metrics.
- Compute and energy consumption data are often estimated rather than precise.

### **Future Improvements**
- Expand the dataset to include more AI models from different sources.
- Enhance interactivity with dynamic user-generated queries.
- Integrate real-time AI performance tracking from benchmark platforms.

---

## 🤝 About the Creator
This project was created by **Lily Dong**, an innovation-driven researcher passionate about AI, technology, and data visualization. Inspired by the evolving landscape of AI, this project aims to bridge the gap between technical insights and public understanding.

