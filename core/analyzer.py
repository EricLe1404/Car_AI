def analyze_car(user_input, car_data):
    make = user_input["make"]
    model = user_input["model"]
    year = user_input["year"]

    # Example analysis logic (placeholder)
    recommendations = f"For your {year} {make} {model}:\n"
    recommendations += "- Consider regular oil checks due to mileage.\n"
    recommendations += "- Fuel efficiency might be low with current mods.\n"
    return recommendations
import json
import streamlit as st

def load_market_data(filepath):
    with open(filepath, 'r') as f:
        return json.load(f)

def analyze_car(user_input, car_data):
    make = user_input["make"]
    model = user_input["model"]
    year = user_input["year"]

    recommendations = f"For your {year} {make} {model}:\n"
    recommendations += "- Consider regular oil checks due to mileage.\n"
    recommendations += "- Fuel efficiency might be low with current mods.\n\n"

    # Load and analyze market data
    market_data = load_market_data("data/market_prices.json")
    similar_cars = [car for car in market_data if car["make"].lower() == make.lower() and car["model"].lower() == model.lower()]

    if similar_cars:
        prices = [car["price"] for car in similar_cars]
        avg_price = sum(prices) / len(prices)
        recommendations += f"📊 Average Market Price: ${avg_price:,.2f}\n"

        # Show price distribution
        st.subheader("💰 Market Price Comparison")
        st.bar_chart(prices)
    else:
        recommendations += "❌ No market data found for this car.\n"

    return recommendations
