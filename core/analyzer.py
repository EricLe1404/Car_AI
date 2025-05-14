def analyze_car(user_input, car_data):
    make = user_input["make"]
    model = user_input["model"]
    year = user_input["year"]

    # Example analysis logic (placeholder)
    recommendations = f"For your {year} {make} {model}:\n"
    recommendations += "- Consider regular oil checks due to mileage.\n"
    recommendations += "- Fuel efficiency might be low with current mods.\n"
    return recommendations
