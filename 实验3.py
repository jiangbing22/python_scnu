import random
role = {"player": [5, 2, 3, 4], "monster": [10, 1, 2]}

while role["player"][0] > 0 and role["monster"][0] > 0:
    n = random.randint(1, 2)
    choice = random.randint(1, 3)
    choice2=random.randint(1,2)
    if n==1:
        atk = role["player"][choice]
        role["monster"][0] -= atk
    else:
        atk = role["monster"][choice2]
        role["player"][0] -= atk
if role['player'][0]>0:
    print(f"player win HP:{role['player'][0]}")
else:
    print(f"monster win HP:{role['monster'][0]}")