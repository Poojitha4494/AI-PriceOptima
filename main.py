from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import joblib
import pandas as pd
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Load model and feature columns
model = joblib.load("priceoptima_model.joblib")
feature_columns = joblib.load("feature_columns.joblib")

@app.get("/")
def home():
    return {"message": "PriceOptima API is running successfully"}

@app.get("/predict")
def predict_price(
    cost: float,
    demand: float,
    inventory_level: int,
    competitor_price: float,
    is_weekend: int
):
    # Step 1: Create input dictionary
    input_data = {
        "cost": cost,
        "demand": demand,
        "inventory_level": inventory_level,
        "competitor_price": competitor_price,
        "is_weekend": is_weekend
    }

    # Step 2: Create DataFrame ✅ df is defined HERE
    df = pd.DataFrame([input_data])

    # Step 3: Align with training features
    df = df.reindex(columns=feature_columns, fill_value=0)

    # Step 4: Predict
    prediction = max(0, model.predict(df)[0])

    # Step 5: Return response
    return {
        "predicted_price": round(float(prediction), 2)
    }

