import random
import json

# Generálj egy véletlen számot
random_number = random.randint(1, 100)

# Kérj be a felhasználótól egy számot és írd ki, hogy a beírt szám kisebb-e vagy nagyobb-e, mint a véletlen szám
while True:
    user_input = int(input("Adj meg egy számot: "))
    if user_input < random_number:
        print("A beírt szám kisebb, mint a véletlen szám.")
    elif user_input > random_number:
        print("A beírt szám nagyobb, mint a véletlen szám.")
    else:
        print("Eltaláltad a véletlen számot!")
        break

# Ismétlés:
tomb = [2, 7, 3, 5, 1, 9, 4]

# Írasd ki a legkisebb elemet
print("A legkisebb elem:", min(tomb))

# Írasd ki a páros számokat
print("Páros számok:", [num for num in tomb if num % 2 == 0])

# JSON feldolgozás
def game_categories(file_path):
    with open(file_path, "r") as file:
        pyobj = json.load(file)
    categories = []
    for game in pyobj["games"]:
        if game["category"] not in categories:
            games_in_category = [gamelisting["name"] for gamelisting in pyobj["games"] if gamelisting["category"] == game["category"]]
            yield game["category"], games_in_category
            categories.append(game["category"])

# Használat
for category, games in game_categories("gyakorlo.json"):
    print(f"{category}:")
    for game in games:
        print(f"\t{game}")