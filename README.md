# 🏠 House Price Prediction using Linear Regression

## 👤 Author

**Umang Choudhary**

---

## 📌 Overview

This project predicts house prices using a Linear Regression model based on features like:

* Living area (sqft)
* Number of bedrooms
* Number of bathrooms
* Grade (quality of construction)
* Number of floors

---

## 📂 Dataset

* File: `kc_house_data.csv`
* Contains housing data from King County, USA

---

## ⚙️ Technologies Used

* Python 3.x
* pandas
* scikit-learn

---

## 🚀 How to Run

### 1. Create Virtual Environment

```bash
python3.10 -m venv venv
```

### 2. Activate Environment

```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Program

```bash
python main.py
```

---

## 🧠 Model Details

* Algorithm: Linear Regression
* Preprocessing: StandardScaler
* Features Used:

  * sqft_living
  * bedrooms
  * bathrooms
  * grade
  * floors

---

## 📊 Example Input

```
Enter living area (sq ft): 2000
Enter bedrooms: 3
Enter bathrooms: 2
Enter grade: 7
Enter floors: 1
```

## 📈 Output

```
Predicted House Price: 450000.00
```

---

## ⚠️ Notes

* Use realistic input values for better predictions
* Model accuracy depends on selected features

---

## ✅ Conclusion

This project demonstrates how machine learning can be used to estimate house prices based on key features using a simple and efficient Linear Regression model.

---
