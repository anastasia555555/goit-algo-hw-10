from pulp import LpMaximize, LpProblem, LpVariable

model = LpProblem("Drink_Production_Optimization", LpMaximize)

lemonade = LpVariable("Lemonade", lowBound=0, cat="Integer")
juice = LpVariable("Fruit_Juice", lowBound=0, cat="Integer")

model += lemonade + juice, "Maximize_total_drinks"

model += 2 * lemonade + 1 * juice <= 100, "Water_constraint"
model += lemonade <= 50, "Sugar_constraint"
model += lemonade <= 30, "Lemon_juice_constraint"
model += 2 * juice <= 40, "Fruit_puree_constraint"

model.solve()

print("Лимонад:", int(lemonade.value()))
print("Фруктовий сік:", int(juice.value()))
print("Загальна кількість продуктів:", int(lemonade.value() + juice.value()))
