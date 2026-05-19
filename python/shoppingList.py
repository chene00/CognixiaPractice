shopList = {
    "ABCMilk" : "Dairy",
    "RedGalaApples" :" Fruit",
    "BCDCheese" : "Dairy",
    "ZCucumber" :" Vegetable",
    "HPLaptop" :" Electronics",
    "FarmFreshTomato" :" Vegetable"
}

countA = 0
countB = 0
prev = None

for item, department in shopList.items():
    if prev == department:
        countA += 1
        prev = department
    else:
        prev = department
        continue
    
print(countA)