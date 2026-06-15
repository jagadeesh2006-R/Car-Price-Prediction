# 🚗 Car Price Prediction Using Machine Learning

## 📌 Project Overview

Car Price Prediction is a Machine Learning-based web application that predicts the selling price of a used car based on various vehicle attributes such as age, kilometers driven, fuel type, seller type, transmission type, and ownership history.

The project demonstrates the complete Machine Learning lifecycle, including data preprocessing, feature engineering, model training, evaluation, and deployment using Streamlit.

---

## 🎯 Features

* Predict used car prices in real-time
* Interactive Streamlit web application
* Data preprocessing and feature engineering
* Multiple machine learning model comparison
* Best model selection based on performance
* User-friendly interface
* Fast and accurate predictions

---

## 🛠 Technologies Used

* Python
* Pandas
* NumPy
* Scikit-Learn
* Streamlit
* Matplotlib
* Seaborn
* Pickle

---

## 📂 Project Structure

```text
Car-Price-Prediction/
│
├── app.py
├── train_model.py
├── model.pkl
├── features.pkl
├── requirements.txt
├── README.md
├── car.csv
│
└── screenshots/
    ├── home_page.png
    ├── prediction_result.png
```

---

## 📊 Dataset Features

The model was trained using the following features:

* km_driven
* Car_Age
* fuel_Diesel
* fuel_Electric
* fuel_LPG
* fuel_Petrol
* seller_type_Individual
* seller_type_Trustmark Dealer
* transmission_Manual
* owner_Fourth & Above Owner
* owner_Second Owner
* owner_Test Drive Car
* owner_Third Owner

### Target Variable

* Selling Price (`selling_price`)

---

## 🤖 Machine Learning Workflow

### 1. Data Collection

Collected historical used-car data containing vehicle specifications and selling prices.

### 2. Data Preprocessing

* Removed unnecessary columns
* Created Car_Age feature
* Encoded categorical variables

### 3. Model Training

The following models were evaluated:

* Linear Regression
* Decision Tree Regressor
* Random Forest Regressor
* Gradient Boosting Regressor
* Extra Trees Regressor

### 4. Model Evaluation

Models were compared using the R² Score metric.

### 5. Model Deployment

The best-performing model was saved using Pickle and deployed through Streamlit.

---

## 🚀 Installation

### Clone the Repository

```bash
git clone https://github.com/jagadeesh2006-R/Car-Price-Prediction.git
```

### Navigate to Project Directory

```bash
cd Car-Price-Prediction
```

### Install Required Libraries

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

## 💻 Application Usage

1. Enter the car's manufacturing year.
2. Enter kilometers driven.
3. Select fuel type.
4. Select seller type.
5. Select transmission type.
6. Select owner category.
7. Click **Predict Price**.
8. View the estimated car selling price instantly.

---

## 📈 Sample Prediction

### Input

* Manufacturing Year: 2020
* Kilometers Driven: 35,000
* Fuel Type: Petrol
* Seller Type: Individual
* Transmission: Manual
* Owner: First Owner

### Output

```text
Predicted Car Price: ₹ 3.87 Lakhs
```

---

## 📸 Screenshots

### Home Page

Add screenshot here:

```text
screenshots/home_page.png
```

### Prediction Result

Add screenshot here:

```text
screenshots/prediction_result.png
```

---

## 🔮 Future Enhancements

* Add car brand and model information
* Hyperparameter tuning
* Feature importance visualization
* Download prediction reports
* Cloud deployment
* Advanced analytics dashboard

---

## 👨‍💻 Author

**Jagadeesh Rallapalli**

B.Tech – Computer Science Engineering

Machine Learning | Data Science | Python Development

GitHub: https://github.com/jagadeesh2006-R

---

## ⭐ Support

If you found this project useful, please give it a ⭐ on GitHub.

🌐 Live Demo: https://car-price-prediction-projects.streamlit.app
