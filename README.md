# 🏦 Bank Reviews & Complaints Analysis

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat-square&logo=python)
![NLP](https://img.shields.io/badge/NLP-TF--IDF%20%7C%20Sentiment%20Analysis-purple?style=flat-square)
![Flask](https://img.shields.io/badge/Deployed-Flask%20App-green?style=flat-square&logo=flask)
![Docker](https://img.shields.io/badge/Container-Docker-blue?style=flat-square&logo=docker)
![Stars](https://img.shields.io/github/stars/vicky60629/Bank-Reviews-Complaints-Analysis?style=flat-square)

> **An end-to-end NLP system that analyses customer reviews across multiple banks — classifying sentiment, predicting star ratings (1–5), and identifying key complaint themes — deployed as a live Flask web application.**

---

## 📌 Problem Statement

Banks receive thousands of customer reviews and complaints daily. Reading each one manually is impossible at scale. This project builds an **automated NLP pipeline** that:

- Classifies reviews as **positive, negative, or neutral**
- Predicts the **star rating (1–5)** from raw review text alone
- Identifies **recurring complaint themes** (service, waiting time, fees, etc.)
- Performs **intent analysis** to understand what customers actually want

This enables banks to prioritise critical complaints, monitor satisfaction trends, and improve customer service — all without manual effort.

---

## 🎯 Business Impact

- **Customer Service Teams** can auto-triage high-priority complaints
- **Bank Managers** get data-driven insights into which services are failing
- **Marketing Teams** can identify what customers love and amplify it
- Scales to handle **thousands of reviews per minute** once deployed

---

## 📊 Dataset

| Feature | Description |
|---------|-------------|
| `Date` | Day the review was posted |
| `Stars` | 1–5 rating given by the customer |
| `Reviews` | Raw text of the customer review/complaint |
| `BankName` | Name of the bank being reviewed |

- ~500 customer reviews and complaints across multiple banks
- Multi-class target: Star ratings 1 through 5
- Real-world noisy text — abbreviations, typos, mixed case, punctuation

---

## 🏗️ Project Architecture

```
Bank-Reviews-Complaints-Analysis/
├── results/
│   ├── 2020-06-21 16_52_49-Window.png
│   ├── 2020-06-21 16_53_18-Window.png
│   ├── 2020-06-21 16_53_57-Window.png
│   └── 2020-06-21 16_58_01-Window.png
├── static/
│   └── styles.css
├── templates/
│   ├── home.html
│   └── result.html
├── Bank Reviews-Complaints Analysis.ipynb   # Full EDA + Modelling
├── app.py                                   # Flask application
├── nlp_model.pkl                            # Trained classification model
├── transform.pkl                            # Label encoder / transformer
├── tfidf_transform.pkl                      # Fitted TF-IDF vectorizer
├── Dockerfile
├── Procfile
├── requirements.txt
└── README.md
```

---

## 🔍 Approach

### 1. Text Preprocessing & Feature Engineering
Extensive NLP feature engineering was applied to extract signal from raw text:

- **Basic text stats:** word count, character count, sentence count
- **Linguistic features:** uppercase words, lowercase words, title-case words
- **Punctuation density:** count of punctuation marks as a noise/emotion proxy
- **Stopword analysis:** stopword count to identify filler-heavy reviews
- **Custom pattern features:**
  - Words ending with specific suffixes (e.g., `et`)
  - Words starting with specific prefixes (e.g., `no`) — a strong negative signal
  - Word frequency dictionaries per review

```python
df["count_punctuations"] = df["Reviews"].apply(
    lambda x: len([c for c in str(x) if c in string.punctuation])
)
df["count_words_upper"] = df["Reviews"].apply(
    lambda x: len([w for w in str(x).split() if w.isupper()])
)
df['words_start_with_no'] = df['Reviews'].apply(
    lambda x: len([w for w in x.lower().split() if w.startswith('no')])
)
```

### 2. Text Vectorisation
- Applied **TF-IDF (Term Frequency–Inverse Document Frequency)** to convert review text into numerical feature vectors
- Serialized the fitted vectorizer (`tfidf_transform.pkl`) so the same transformation is applied at inference time

### 3. NLP Analysis Tasks
| Task | Method |
|------|--------|
| Sentiment Classification | Positive / Negative / Neutral labels |
| Star Rating Prediction | Multi-class classification (1–5) |
| Keyword Extraction | Most frequent positive/negative words |
| Topic Modelling | Clustering to identify complaint themes |
| Intent Analysis | Understanding customer intent from text |

### 4. Model Training
- Trained a multi-class classification model to predict star ratings directly from review text
- Serialized trained model as `nlp_model.pkl` for production inference

### 5. Deployment
- Built a **Flask web application** for real-time star rating prediction
- User inputs any review text → model predicts a rating from 1 to 5
- Containerized using **Docker** for portability
- Originally deployed on Heroku (migrating to Render — see below)

---

## 📈 Results & Insights

**Key findings from the analysis:**

- Reviews with **high punctuation counts** (e.g., multiple `!` or `?`) are strongly correlated with 1-star ratings
- Words starting with **"no"** (no service, not helpful, nowhere) are the top negative signal
- **Uppercase word density** is a proxy for customer frustration
- Most complaints cluster around: long wait times, poor customer service, hidden fees, and account issues
- 4 and 5-star reviews consistently mention: staff helpfulness, speed, digital banking ease

---

## 🛠️ Tech Stack

| Category | Tools |
|----------|-------|
| Language | Python 3.8+ |
| NLP & Text Processing | NLTK, RegEx, String |
| Feature Engineering | Pandas, NumPy |
| Vectorisation | Scikit-learn TF-IDF |
| Modelling | Scikit-learn |
| Visualisation | Matplotlib, Seaborn, WordCloud |
| Web Framework | Flask |
| Serialization | Pickle |
| Containerization | Docker |
| Deployment | Heroku → Render |

---

## 🚀 Running Locally

### Option 1: Standard Setup
```bash
# Clone the repository
git clone https://github.com/vicky60629/Bank-Reviews-Complaints-Analysis.git
cd Bank-Reviews-Complaints-Analysis

# Install dependencies
pip install -r requirements.txt

# Run the Flask app
python app.py
```
Open `http://localhost:5000` in your browser.

### Option 2: Docker
```bash
docker build -t bank-reviews-app .
docker run -p 5000:5000 bank-reviews-app
```

---

## 🖥️ How to Use the App

1. Open the web app in your browser
2. Type or paste any bank review text into the input box
3. Click **"Predict"**
4. Get an instant star rating prediction (1–5) based on your review

**Example Input:**
> *"The staff was extremely rude and I waited 45 minutes just to speak to someone. Totally unacceptable."*

**Predicted Output:** ⭐ 1 Star

---

## 📸 App Preview

| Home Screen | Prediction Result |
|------------|------------------|
| ![Home](results/2020-06-21%2016_52_49-Window.png) | ![Result](results/2020-06-21%2016_53_57-Window.png) |

---

## 💡 Key Learnings & Future Improvements

**What worked well:**
- TF-IDF combined with engineered text features gave a strong signal beyond just word frequencies
- Custom features like "words starting with no" proved surprisingly effective as negative sentiment indicators
- End-to-end deployment validated the full ML lifecycle — not just model training

**Future enhancements:**
- [ ] Replace TF-IDF with **BERT / sentence-transformers** for deeper semantic understanding
- [ ] Add **aspect-based sentiment analysis** (e.g., separate scores for service, speed, fees)
- [ ] Build real-time **complaint dashboard** using Streamlit or Plotly Dash
- [ ] Train on larger datasets (e.g., Trustpilot, Google Reviews scrape)
- [ ] Add **multilingual support** for Indian regional languages
- [ ] Integrate with **MLflow** for experiment tracking

---

## 👨‍💻 About the Author

**Vicky Gupta** — Data Engineering Analyst @ Accenture (4.5 years) | Aspiring Data Scientist

Passionate about NLP and building end-to-end ML systems that solve real business problems. Experienced in PySpark, ETL pipelines, and deploying ML models to production.

🔗 [LinkedIn](https://www.linkedin.com/in/vicky-gupta-583016168/) | [GitHub](https://github.com/vicky60629)

📧 vg60629@gmail.com

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

⭐ **If you found this project useful, please star the repository — it helps others discover it!**
