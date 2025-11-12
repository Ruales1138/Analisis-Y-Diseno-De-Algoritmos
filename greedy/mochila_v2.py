def backpack(val, wt, capacity):
    value_per_kg = []
    for j in range(len(val)):
        value_per_kg.append(val[j] / wt[j])
    objects = sorted(zip(value_per_kg, val, wt), reverse=True)
    max_value = 0
    for obj in objects:
        value = obj[1]
        weight = obj[2]
        if capacity - weight > 0:
            capacity -= weight
            max_value += value
        else:
            fraction = capacity / weight
            max_value += value * fraction
    return max_value

val = [60, 100, 120] 
wt = [10, 20, 30] 
capacity = 50

val_2 = [500] 
wt_2 = [30] 
capacity_2 = 10

print(backpack(val, wt, capacity)) # -> 240
print(backpack(val_2, wt_2, capacity_2)) # -> 166.667