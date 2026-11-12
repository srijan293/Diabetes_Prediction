# 🩺 Diabetes Prediction System

A Machine Learning-based web application that predicts the possibility of diabetes based on user-provided medical parameters.

## 🚀 Project Overview

The Diabetes Prediction System is a web application built using Python, Flask, and Machine Learning. Users can enter medical information such as glucose level, blood pressure, BMI, age, and other health parameters to receive a prediction.

## ✨ Features

- Diabetes prediction using a trained Machine Learning model.
- Simple and user-friendly interface.
- Professional healthcare-themed UI.
- Light Mode and Dark Mode.
- Instant prediction results.

## 🛠️ Technologies Used

- **Frontend:** HTML, CSS, JavaScript
- **Backend:** Python, Flask
- **Machine Learning:** Scikit-learn
- **Model:** Pickle (`model1.pkl`)

## 📋 Input Parameters

The application uses the following eight parameters:

1. Pregnancies
2. Glucose
3. Blood Pressure
4. Skin Thickness
5. Insulin
6. BMI
7. Diabetes Pedigree Function
8. Age

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/YOUR-USERNAME/Diabetes-Prediction.git
```

### 2. Navigate to the project folder

```bash
cd Diabetes-Prediction
```

### 3. Create a virtual environment (optional)

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 4. Install dependencies

```bash
pip install -r requirements.txt
```

### 5. Run the application

```bash
python app.py
```

Open your browser and visit:

```text
http://127.0.0.1:5000/
```

## 📂 Project Structure

```text
Diabetes-Prediction/
│
├── static/
│   ├── css/
│   ├── js/
│   └── diabets.jpeg
│
├── templates/
│   ├── index.html
│   └── result.html
│
├── app.py
├── model1.pkl
├── requirements.txt
└── README.md
```

*The folder structure may vary depending on your actual project files.*

## 🌐 Deployment

The application can be deployed using Render by connecting the GitHub repository.

## ⚠️ Disclaimer

This project is developed for educational purposes only. Predictions are not a substitute for professional medical diagnosis or advice.

## 👨‍💻 Author

**Srijan Ghosh**

B.Tech – Artificial Intelligence and Machine Learning
