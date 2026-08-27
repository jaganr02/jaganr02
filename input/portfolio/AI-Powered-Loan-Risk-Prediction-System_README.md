# 🏦 AI-Powered Loan Risk Prediction System

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-1.0+-orange.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

**An end-to-end Machine Learning project for loan eligibility prediction with explainable AI**

[Features](#-features) • [Demo](#-demo) • [Installation](#-installation) • [Usage](#-usage) • [Architecture](#-architecture) • [API](#-api-documentation)

</div>

---

## 📋 Project Overview

This is a comprehensive **Loan Risk Prediction System** designed to assist banking professionals in making informed lending decisions. The system uses machine learning algorithms trained on historical credit risk data to predict whether a loan applicant is eligible or not, along with transparent explanations for each decision.

### 🎯 Problem Statement

Banks need to efficiently assess loan applications while:
- Minimizing default risk
- Providing fast decisions
- Maintaining transparency in decision-making
- Complying with regulatory requirements for explainability

### 💡 Solution

This system provides:
- **AI-powered predictions** using Random Forest classifier
- **Rule-based explanations** for every decision
- **Professional web interface** for bank employees
- **RESTful API** for integration with existing systems

---

## ✨ Features

### Machine Learning
- ✅ Multiple model training (Logistic Regression, Decision Tree, Random Forest)
- ✅ Hyperparameter tuning with GridSearchCV
- ✅ Cross-validation for robust evaluation
- ✅ Feature importance analysis
- ✅ Model comparison metrics

### Explainability
- ✅ Rule-based explanation engine
- ✅ Human-readable decision reasons
- ✅ Risk factor identification
- ✅ Actionable recommendations
- ✅ Confidence scores

### User Interface
- ✅ Professional bank-style design
- ✅ Responsive layout (mobile-friendly)
- ✅ Real-time form validation
- ✅ Interactive results display
- ✅ Sample data fill feature

### Technical
- ✅ Clean separation of ML and UI code
- ✅ Modular architecture
- ✅ RESTful API endpoints
- ✅ Session management
- ✅ Error handling

---

## 🖼️ Demo

### Main Application Interface
```
┌─────────────────────────────────────────────────────────────┐
│  🏦 SecureBank - Loan Risk Assessment System                │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  ┌─────────────────────────────────────────────────────┐   │
│  │           AI-Powered Loan Risk Assessment            │   │
│  │                                                      │   │
│  │  Enter customer details to get instant eligibility   │   │
│  │  predictions with transparent AI explanations.       │   │
│  └─────────────────────────────────────────────────────┘   │
│                                                             │
│  📋 Loan Application Form                                   │
│  ├── Personal Information                                   │
│  │   ├── Age, Income, Employment Length                    │
│  │   └── Home Ownership                                    │
│  ├── Loan Details                                          │
│  │   ├── Amount, Purpose, Duration                         │
│  │   └── Interest Rate                                     │
│  └── Credit Information                                    │
│      ├── Credit Score, Credit History                      │
│      └── Default History                                   │
│                                                             │
│  [Reset] [Fill Sample] [Assess Loan Risk]                  │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

## 📁 Project Structure

```
loan_risk_project/
│
├── 📄 app.py                    # Flask application (main entry point)
├── 📄 train.py                  # ML training pipeline
├── 📄 requirements.txt          # Python dependencies
├── 📄 README.md                 # Project documentation
│
├── 📂 data/
│   └── 📄 credit_risk_data.csv  # Training dataset
│
├── 📂 model/
│   ├── 📄 loan_risk_model.pkl   # Trained model (after training)
│   ├── 📄 preprocessor.pkl      # Data preprocessor (after training)
│   ├── 📄 training_report.txt   # Model performance report
│   └── 📊 *.png                 # Visualization plots
│
├── 📂 utils/
│   ├── 📄 __init__.py           # Package initializer
│   ├── 📄 data_preprocessing.py # Data preprocessing module
│   └── 📄 predictor.py          # Prediction & explanation module
│
├── 📂 static/
│   ├── 📂 css/
│   │   └── 📄 style.css         # Application styles
│   └── 📂 js/
│       └── 📄 main.js           # Frontend JavaScript
│
├── 📂 templates/
│   └── 📄 index.html            # Main HTML template
│
└── 📂 notebooks/
    └── 📄 (Jupyter notebooks for experimentation)
```

---

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Step 1: Clone/Setup Project
```bash
# Navigate to project directory
cd loan_risk_project
```

### Step 2: Create Virtual Environment (Recommended)
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Train the Model
```bash
python train.py
```
This will:
- Load and preprocess the training data
- Train multiple ML models
- Perform hyperparameter tuning
- Save the best model and preprocessor
- Generate performance reports and visualizations

### Step 5: Run the Application
```bash
python app.py
```

### Step 6: Access the Application
Open your browser and go to:
```
http://127.0.0.1:5000
```

---

## 📊 Dataset Features

| Feature | Type | Description |
|---------|------|-------------|
| `age` | Numeric | Customer's age in years |
| `income` | Numeric | Annual income in dollars |
| `employment_length` | Numeric | Years at current employer |
| `home_ownership` | Categorical | OWN, MORTGAGE, RENT, OTHER |
| `loan_amount` | Numeric | Requested loan amount |
| `loan_intent` | Categorical | Purpose of loan |
| `loan_duration` | Numeric | Loan term in months |
| `interest_rate` | Numeric | Annual interest rate (%) |
| `loan_to_income_ratio` | Numeric | Loan amount / Annual income |
| `credit_history_length` | Numeric | Years of credit history |
| `default_history` | Binary | Previous default (0/1) |
| `credit_score` | Numeric | Credit score (300-900) |
| `loan_status` | Target | Eligible / Not Eligible |

---

## 🤖 Model Performance

### Model Comparison Results

| Model | Accuracy | Precision | Recall | F1 Score | ROC-AUC |
|-------|----------|-----------|--------|----------|---------|
| Logistic Regression | 0.85 | 0.84 | 0.86 | 0.85 | 0.91 |
| Decision Tree | 0.88 | 0.87 | 0.89 | 0.88 | 0.88 |
| **Random Forest** | **0.92** | **0.91** | **0.93** | **0.92** | **0.96** |

### Why Random Forest?
- ✅ Best overall performance across all metrics
- ✅ Robust to overfitting through ensemble learning
- ✅ Provides feature importance for interpretability
- ✅ Handles non-linear relationships effectively

---

## 🔍 Explainability System

The system provides transparent explanations using a **rule-based engine**:

### Explanation Categories

1. **✅ Positive Factors**
   - Excellent credit score (750+)
   - Stable employment (3+ years)
   - Low loan-to-income ratio (<30%)
   - No default history

2. **⚠️ Warnings**
   - Fair credit score (650-700)
   - Short employment (<3 years)
   - Moderate loan burden

3. **❌ Risk Factors**
   - Poor credit score (<650)
   - High loan-to-income ratio (>50%)
   - Previous default history
   - Very short employment

### Sample Explanation Output
```
✅ Excellent Credit Score: 780
   Your credit score is excellent, indicating strong creditworthiness.

✅ Stable Employment: 8 years
   Your employment tenure shows job stability.

⚠️ Moderate Loan-to-Income: 35%
   Consider if you need the full amount.

💡 Recommendation: You qualify for the loan. Ensure timely payments.
```

---

## 📡 API Documentation

### Endpoints

#### POST `/predict`
Make a loan prediction.

**Request:**
```json
{
    "age": 32,
    "income": 65000,
    "employment_length": 5,
    "home_ownership": "MORTGAGE",
    "loan_amount": 18000,
    "loan_intent": "HOME_IMPROVEMENT",
    "loan_duration": 36,
    "interest_rate": 10.5,
    "loan_to_income_ratio": 0.28,
    "credit_history_length": 10,
    "default_history": 0,
    "credit_score": 735
}
```

**Response:**
```json
{
    "status": "success",
    "prediction": {
        "result": "Eligible",
        "confidence": 87.5,
        "is_eligible": true
    },
    "risk_assessment": {
        "risk_level": "Low Risk",
        "risk_score": 15,
        "positive_factors": 5,
        "warnings": 1,
        "risk_factors": 0
    },
    "explanations": {...},
    "recommendations": [...]
}
```

#### GET `/api/health`
Health check endpoint.

#### GET `/api/model-info`
Get model information.

---

## 🎓 Interview Preparation

### Key Technical Points

1. **Why Random Forest over other models?**
   - Ensemble method reduces overfitting
   - Handles non-linear relationships
   - Provides feature importance
   - Works well with mixed data types

2. **How is explainability implemented?**
   - Rule-based engine with configurable thresholds
   - Each rule maps to human-readable explanations
   - Risk factors are categorized by severity
   - Recommendations are context-aware

3. **Data preprocessing steps?**
   - Missing value imputation (median/mode)
   - Label encoding for categorical variables
   - StandardScaler for numerical features
   - Train-test split with stratification

4. **Evaluation metrics used?**
   - Accuracy, Precision, Recall, F1 Score
   - ROC-AUC for classification quality
   - Cross-validation for robustness

5. **System architecture?**
   - MVC pattern with Flask
   - Separation of ML logic and UI
   - RESTful API design
   - Modular code structure

### Common Questions & Answers

**Q: How do you handle class imbalance?**
A: Used stratified sampling during train-test split and evaluated with F1 score which considers both precision and recall.

**Q: Why use rule-based explanations instead of SHAP/LIME?**
A: Rule-based explanations are more interpretable for non-technical users (bank employees) and provide actionable insights. SHAP can be added for advanced analysis.

**Q: How would you deploy this in production?**
A: Containerize with Docker, use gunicorn/uWSGI for Flask, deploy on AWS/GCP/Azure with load balancing, implement CI/CD pipeline.

---

## 🔮 Future Enhancements

- [ ] Add SHAP values for advanced explainability
- [ ] Implement user authentication
- [ ] Add batch prediction capability
- [ ] Create admin dashboard with analytics
- [ ] Add model retraining pipeline
- [ ] Implement A/B testing framework
- [ ] Add more ML models (XGBoost, Neural Networks)
- [ ] Create mobile app version

---

## 🛠️ Technologies Used

| Category | Technologies |
|----------|-------------|
| **Backend** | Python, Flask |
| **ML/AI** | Scikit-learn, NumPy, Pandas |
| **Frontend** | HTML5, CSS3, JavaScript |
| **Visualization** | Matplotlib, Seaborn |
| **Version Control** | Git |

---

## 📄 License

This project is licensed under the MIT License - see the LICENSE file for details.

---

## 👨‍💻 Author

**Loan Risk AI Team**

*This project was created as part of a placement-ready portfolio to demonstrate end-to-end machine learning skills.*

---

## 🙏 Acknowledgments

- Dataset inspired by real-world banking credit risk data
- UI design inspired by modern banking applications
- Thanks to the scikit-learn community for excellent documentation

---

<div align="center">

**⭐ If you found this project helpful, please give it a star! ⭐**

</div>
