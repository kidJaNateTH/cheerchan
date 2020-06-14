import json
def save(idd, data):
    with open('users.json', 'r') as f:
        users = json.load(f)
    with open('users.json', 'w') as f:
        users[str(idd)] = data
        json.dump(users, f, sort_keys=True, indent=4, ensure_ascii=False)
iddd = int(input("your id"))
data = input("your data")
save(iddd,data)

