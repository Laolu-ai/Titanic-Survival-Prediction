# Titanic-Survival-Prediction
ML Project to predict titanic passenger survival with a simple web app
# 🚢 Titanic Survival Prediction Web App

A Machine Learning web application that predicts whether a passenger would survive the Titanic disaster based on input features such as age, gender, passenger class, and more.

The model is trained using the famous **Titanic dataset** and deployed as a web app.

---

## 📌 Project Overview

This project demonstrates an end-to-end machine learning workflow:

- Data preprocessing
- Feature engineering
- Model training
- Model evaluation
- Web application integration
- Cloud deployment

Users can input passenger details through a web interface and the app will predict whether the passenger would likely **Survive** or **Not Survive**.

---

## 🧠 Machine Learning Pipeline

1. Data Cleaning
2. Exploratory Data Analysis (EDA)
3. Feature Engineering
4. Model Training
5. Model Evaluation
6. Model Serialization
7. Web App Integration

---

## 🛠️ Tech Stack

**Languages & Libraries**

- Python
- Pandas
- NumPy
- Scikit-learn

**Web Framework**

- Flask 

**Visualization**

- Matplotlib and Seaborn

**Deployment**

- :contentReference[oaicite:1]{index=1}

---

## 📂 Project Structure

```
titanic-survival-app/
│
├── templates/
│   └── index.html
│
├── notebooks/
|   ├── Titanic Dataset.csv
│   └── Titanic Datasets.ipynb
│
├── models/
│   └── trained_model.pkl
│
├── app.py
|
├── utilities.py
│   
│
├── requirements.txt
├── README.md
└── Procfile
```

---

## ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/laolu-ai/titanic-survival-prediction.git
cd titanic-survival-prediction
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Mac/Linux**

```bash
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the App Locally

```bash
python app.py
```

Then open:

```
http://127.0.0.1:5000
```

---

## 🌐 Live Demo

Deployed on **:contentReference[oaicite:2]{index=2}**

👉 Add  live URL here once deployed.

```
https://your-app-name.onrender.com
```

---

## 📊 Model Features

Example inputs used for prediction:

- Passenger Class (Pclass)
- Sex
- Age
- Number of Siblings/Spouses
- Number of Parents/Children
- Fare
- Embarked Port

---

## 📈 Model Performance

| Metric | Score |
|------|------|
| Accuracy | XX% |
| Precision | XX |
| Recall | XX |

*(Replace with your real results)*

---

##  App Screenshot

Add a screenshot of the UI here.

```
![App Screenshot](images/app.png)
```

---

## 🚀 Future Improvements

- Add more advanced models
- Improve UI/UX
- Add model explainability
- Add Docker containerization
- CI/CD pipeline

---

##  Contributing

Contributions are welcome!

1. Fork the repo
2. Create a new branch
3. Commit your changes
4. Submit a pull request

---

##  License

This project is licensed under the MIT License.

---

##  Author

Ademujimi Olaoluwa

- GitHub: https://github.com/yourusername
- LinkedIn: your-linkedin

---

⭐ If you like this project, consider giving it a star!
