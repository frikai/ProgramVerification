from z3 import *


s = Solver()

Prices = {
    "MF" : 215,
    "FF" : 275,
    "SS" : 335,
    "HW" : 355,
    "MS" : 420,
    "SP" : 580
}

Vars = {k: Int(k) for k in Prices.keys()}

for k in Prices.keys():
    s.add(Vars[k] >= 0)

s.add(1505 == (Vars["MF"] *Prices["MF"] +
                Vars["FF"] * Prices["FF"] +
                Vars["SS"] * Prices["SS"] +
                Vars["HW"] * Prices["HW"] + 
                Vars["MS"] * Prices["MS"] + 
                Vars["SP"] * Prices["SP"]))

while s.check() == sat:
    model = s.model()
    print(model)
    s.add(Not(And([Vars[k] == model[Vars[k]] for k in Prices.keys()])))

# Sum: 15.05

# Mixed fruit: 2.15
# French fries: 2.75
# Side salad: 3.35
# Hot wings: 3.55
# Mozzarella sticks: 4.20
# Sampler plate: 5.80





