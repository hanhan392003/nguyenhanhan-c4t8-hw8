import random
# ex 20
character = {
    "name":"Light",
    "age":17,
    "strength":8,
    "defense":10,
    "hp":100,
    "backpack":["Shield", "Bread loaf"],
    "gold":100,
    "level":2
}

# ex 21
character["gold"] += 50

# ex 22
character["backpack"].append("FlintStone")

# ex 23
character["pocket"] = ["MonsterDex", "Flashlight"]

#24
skills = [
    {
        "name":"Tackle",
        "minimum level":1,
        "damage":5,
        "hit rate":0.3
    },
    {
        "name":"Quick attack",
        "minimum level":2,
        "damage":3,
        "hit rate":0.5
    },
    {
        "name":"Strong Kick",
        "minimum level":4,
        "damage":7,
        "hit rate":0.2
    }
]

# ex 25
for skill in skills:
    print("Skill",skills.index(skill) +1)
    for (k, v) in skill.items():
        print(k, ":", v)

# ex 26
for skill in skills:
    print("Skill",skills.index(skill) +1)
    for (k, v) in skill.items():
        if k == "name":
            print(k, ":", v)

# ex 27
n = int(input("Choose the skill (1,2 or 3): "))
for (i,j) in skills[n-1].items():
    if i == "minimum level":
        if j <= character["level"]:
            print(skills[n-1]["damage"])
        
# ex 28
r = random.random()
new = int(input("Choose the skill (1,2 or 3): "))
for (x,y) in skills[new-1].items():
    if x == "minimum level":
        if y <= character["level"]:
            if r <= skills[new-1]["hit rate"]:
                print(skills[n-1]["damage"])
            else:
                print("Cant hit the target")