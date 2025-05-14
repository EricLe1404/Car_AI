import streamlit as st
from core.analyzer import analyze_car
from core.data_manager import load_car_data

def main():
    st.title("🚗 Car AI Advisor")

    st.subheader("Enter Your Car Details:")

    make = st.text_input("Make", "Lexus")
    model = st.text_input("Model", "IS350")
    year = st.number_input("Year", min_value=1980, max_value=2025, value=2011)
    mileage = st.number_input("Mileage (km)", min_value=0, value=202000)
    driving_style = st.selectbox("Driving Style", ["calm", "normal", "sporty"])
    modifications = st.multiselect(
        "Modifications",
        ["exhaust", "intake", "ECU tune", "turbo", "supercharger"],
    )

    if st.button("Analyze"):
        user_input = {
            "make": make,
            "model": model,
            "year": int(year),
            "mileage": int(mileage),
            "driving_style": driving_style,
            "modifications": modifications
        }

        car_data = load_car_data("data/car_specs.json")
        recommendation = analyze_car(user_input, car_data)
        st.subheader("📋 Recommendations:")
        st.text(recommendation)

if __name__ == "__main__":
    main()
