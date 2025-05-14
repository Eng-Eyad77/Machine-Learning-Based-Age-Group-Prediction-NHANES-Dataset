# 🧠 Machine-Learning-Based-Age-Group-Prediction-NHANES-Dataset
---

## 📌 Project Overview

This project predicts whether an individual is a **Senior (1)** or **Adult (0)** based on several health-related metrics. It leverages a cleaned dataset derived from the **NHANES 2013–2014 Age Prediction Dataset** and applies machine learning models for binary classification.

---

## 🧾 Dataset Description

**Source:** [Kaggle Dataset – Age Prediction (Binary Classification)](https://www.kaggle.com/datasets/prishasawhney/age-prediction-dataset-binary-classification)

The dataset contains 6 features:

| Feature   | Description |
|-----------|-------------|
| `PAQ605`  | Weekly engagement in moderate/vigorous physical activity |
| `BMXBMI`  | Body Mass Index |
| `LBXGLU`  | Fasting Blood Glucose |
| `LBXGLT`  | Oral Glucose Tolerance |
| `LBXIN`   | Blood Insulin Levels |
| `age_group` | Target (0: Adult, 1: Senior) |

---

## 🧹 Data Preparation

- **Missing values** were filled with column means.
- **Outliers** removed using IQR method.
- **Duplicates** were dropped.
- **SMOTE** was applied to balance the classes in training data.
- Features were scaled using **MinMaxScaler**.

All preprocessing was performed using the custom `dataPreperation()` function in [`dataPrep.py`](./dataPrep.py).

---

## 🧪 Machine Learning Models

Five classification models were trained and evaluated:

- **Logistic Regression**
- **Decision Tree**
- **Random Forest**
- **K-Nearest Neighbors**
- **XGBoost**

Each model was tested across:
- Original split data
- Scaled data
- SMOTE-balanced data

Model evaluation was based on:
- Accuracy
- Confusion Matrix
- Prediction Probabilities

---

## 🔍 Best Results (After SMOTE + Scaling)

| Model                 | Train Accuracy | Test Accuracy |
|----------------------|----------------|---------------|
| Logistic Regression  | 67.7%          | 65.3%         |
| Decision Tree        | 100%           | 74.3%         |
| XGBoost              | 100%           | **79.2%**     |
| KNN                  | 82.9%          | 71.3%         |
| Random Forest        | 100%           | **81.7%**     |

🎯 **Random Forest** achieved the highest test accuracy.

---

## 📊 Visualizations

- Confusion matrices were visualized using `seaborn` heatmaps.
- Final predictions were organized into a dataframe (`df_both`) containing:
  - Model predictions
  - Predicted probabilities

---

## 🗂️ Code Structure

- `FinalProject-F&T.ipynb`: Main notebook containing all code and experiments.
- `dataPrep.py`: Function for cleaning and preparing the dataset.

---

## 👥 Author

This project was designed, implemented, and evaluated by:

**Eyad Maccawy**

---

