import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

# ✅ Keep pipeline (DO NOT overwrite)
model = Pipeline([
    ('scaler', StandardScaler()),
    ('regressor', LinearRegression())
])

# Load dataset
df = pd.read_csv("kc_house_data.csv")

# Features
X = df[['sqft_living', 'bedrooms', 'bathrooms', 'grade', 'floors']]
y = df['price']

# Train model
model.fit(X, y)

# User input
print("\nEnter details to predict house price:")

sqft = float(input("Enter living area (sq ft) [1000-4000]: "))
bedrooms = int(input("Enter bedrooms [1-6]: "))
bathrooms = float(input("Enter bathrooms [1-4]: "))
grade = int(input("Enter grade (1-13): "))
floors = float(input("Enter floors (1-3): "))

# Input DataFrame
user_data = pd.DataFrame({
    'sqft_living': [sqft],
    'bedrooms': [bedrooms],
    'bathrooms': [bathrooms],
    'grade': [grade],
    'floors': [floors]
})

# Predict
predicted_price = model.predict(user_data)

# Prevent negative
predicted_price = max(0, predicted_price[0])

print("\nPredicted House Price:", round(predicted_price, 2))