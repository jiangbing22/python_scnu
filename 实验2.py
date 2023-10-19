import random

store = {"apple": 1, "banana": 2, "watermelon": 3, "orange": 4, 'cherry': 5, 'pear': 6}
stock = list(store.keys())
stock.append('lemon')
for i in range(int(len(stock)/2)):
    num = random.randint(0, 10)
    choice =random.choice(stock)
    if choice in store.keys():
        store[choice]+=num
    else:
        store[choice]=num

result=sorted(store.values())
print(store)