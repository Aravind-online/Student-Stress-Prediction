# 🧠 Student Depression Prediction Using Machine Learning

## 📌 Project Overview

Student mental health has become a significant concern in educational institutions. Academic pressure, financial stress, anxiety, sleep disorders, and other personal factors can negatively impact students' mental well-being. This project aims to predict the likelihood of depression among students using Machine Learning techniques.

The system analyzes various student-related factors and predicts whether a student is at risk of depression. A Streamlit-based web application provides an easy-to-use interface for users to enter information and receive predictions instantly.

---

## 🎯 Objectives

* Predict student depression risk using Machine Learning.
* Analyze factors affecting mental health.
* Provide early identification of students who may require support.
* Create a user-friendly web application for predictions.

---

## 🚀 Features

* Student Depression Risk Prediction
* Interactive Streamlit Web Interface
* Machine Learning-Based Classification
* Real-Time Prediction Results
* Mental Health Recommendations
* Simple and User-Friendly Design

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Libraries

* Pandas
* NumPy
* Scikit-Learn
* Joblib
* Streamlit

### Machine Learning Algorithm

* Random Forest Classifier

### Development Tools

* VS Code
* Python 3.11

---

## 📊 Dataset Information

Dataset Name:
**Depression Dataset**

Source:
Kaggle Student Depression Dataset

Dataset Size:

* 604 Records
* 31 Attributes

Sample Attributes:

* Age Range
* Gender
* Education
* Professional Status
* Financial Stress
* Anxiety
* Insomnia
* Conflict
* Suicide Thoughts
* Lost Interest
* Depression Status (Target Variable)

---

## ⚙️ Project Workflow

### Step 1: Data Collection

The dataset was obtained from Kaggle and imported into Python using Pandas.

### Step 2: Data Preprocessing

* Removed missing values
* Encoded categorical features
* Converted text data into numerical format

### Step 3: Model Training

* Split data into training and testing sets
* Trained a Random Forest Classifier

### Step 4: Model Evaluation

* Evaluated model performance using Accuracy Score

### Step 5: Model Deployment

* Saved trained model using Joblib
* Developed a Streamlit-based web application

---

## 📈 Model Performance

Algorithm Used:

* Random Forest Classifier

Accuracy Achieved:

* **86.78%**

This accuracy demonstrates that the model can effectively predict depression risk based on student-related factors.

---

## ▶️ Installation

### Clone the Repository

```bash
git clone https://github.com/yourusername/student-depression-prediction.git
cd student-depression-prediction
```

### Install Dependencies

```bash
pip install pandas numpy scikit-learn streamlit joblib
```

---

## ▶️ Run the Project

### Train the Model

```bash
python train_model.py
```

### Launch the Web Application

```bash
streamlit run app.py
```

Open the browser and visit:

```text
http://localhost:8501
```

---

## 📂 Project Structure

```text
Student_Depression_Project/
│
├── dataset/
│   └── Depression Dataset.csv
│
├── train_model.py
├── app.py
├── model.pkl
├── README.md
│
└── requirements.txt
```

---

## 📷 Application Output

Input:

* Age
* Gender
* Financial Stress
* Work Pressure
* Anxiety
* Insomnia

Output:

* Depression Risk Prediction
* Mental Health Recommendations

---

## 🔮 Future Enhancements

* User Authentication
* Database Integration
* PDF Report Generation
* Advanced Data Visualization
* AI-Based Mental Health Suggestions
* Cloud Deployment
* Mobile Application Version

---

## 🎓 Educational Benefits

This project demonstrates the practical application of:

* Machine Learning
* Data Preprocessing
* Classification Algorithms
* Model Deployment
* Web Application Development

---

## 📌 Conclusion

The Student Depression Prediction System uses Machine Learning to identify students who may be at risk of depression. By analyzing various academic, social, and personal factors, the system provides quick predictions and can assist in promoting early awareness and intervention for student mental health.

---

### Developed By

Aravind P
-An ai/ml devloper
