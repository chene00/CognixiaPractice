class Car:
    def __init__(self, year:int, color: str, make:str, model:str):
        self.year = year
        self.color = color
        self.make = make
        self.model = model

def countAllColors(cars : list[Car]):
    colors = {}
    for car in cars:
        if car.color in colors:
            colors[car.color] += 1
        else:
            colors[car.color] = 1
    return colors

if __name__ == "__main__":
    list_of_cars = [
        Car(2026, "black", "toyota", "RAV4"),
        Car(2020, "pink", "honda", "crv"),
        Car(2022, "blue", "toyota", "RAV4"),
        Car(2023, "green", "honda", "crv"),
        Car(2024, "grey", "toyota", "camery"),
        Car(2025, "green", "mitsubishi", "eclipse cross")
    ]

    colors = countAllColors(list_of_cars)

    # .items() returns (key, value) pairs
    for color, amount in colors.items():
        print(f"{color} : {amount}")