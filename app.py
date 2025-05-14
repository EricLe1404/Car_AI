from core.analyzer import analyze_car
from core.data_manager import load_car_data

def main():
    car_data = load_car_data("data/car_specs.json")
    user_input = {
        "make": "Lexus",
        "model": "IS350",
        "year": 2011,
        "mileage": 202000,
        "driving_style": "sporty",
        "modifications": ["exhaust", "intake"]
    }
    recommendation = analyze_car(user_input, car_data)
    print(recommendation)

if __name__ == "__main__":
    main()
