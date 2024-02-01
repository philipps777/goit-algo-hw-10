import pulp


model = pulp.LpProblem("Maximize Production", pulp.LpMaximize)


Lemonade = pulp.LpVariable('Lemonade', lowBound=0,
                           cat='Integer')

Fruit_juice = pulp.LpVariable('Fruit_juice', lowBound=0, cat='Integer')


model += Lemonade + Fruit_juice, "Total Production"


model += 2 * Lemonade + Fruit_juice <= 100
model += Lemonade <= 50
model += Lemonade <= 30
model += 2 * Fruit_juice <= 40

model.solve()

print("Виробляти лимонаду:", Lemonade.varValue)
print("Виробляти фруктового соку:", Fruit_juice.varValue)
print("Сума:", Lemonade.varValue + Fruit_juice.varValue)
