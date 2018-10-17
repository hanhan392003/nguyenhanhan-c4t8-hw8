# ex 1
computers = {
    "HP":20,
    "DELL":50,
    "MACBOOK":12,
    "ASUS":30
}

# ex 2
print(computers["MACBOOK"])

# ex 3
n = input("Enter the label of the computer ").upper()
if n in computers.keys():
    print(computers[n])
else:
    print("The store doesnt have this label of computer")

# ex 4
computers["TOSHIBA"] = 10

# ex 5
new_computer = input("Enter the label of the computer ").upper()
numbers_of_new_computers = int(input("enter the number of new computers "))
computers[new_computer] = numbers_of_new_computers

# ex 6
computers["DELL"] += 10
computers["MACBOOK"] =2

# ex 7
for k, v in computers.items():
    print(k, ":", v)

# ex 8
total_number_of_computers = 0
for v in computers.values():
    total_number_of_computers += v
print(total_number_of_computers)

# ex 9
computers["FUJISU"] = 15
computers["ALIENWARE"] = 5

# ex 10
total_number_of_computers = 0
for v in computers.values():
    total_number_of_computers += v
print(total_number_of_computers)

# ex 11
price ={
    "HP":600,
    "DELL":650,
    "MACBOOK":12000,
    "ASUS":400,
    "ACER":350,
    "TOSHIBA":600,
    "FUJISU":900,
    "ALIENWARE":1000
}

# ex 12
print(price["ASUS"])

# ex 13
p = input("Enter the label of the computer ").upper()
if p in price.keys():
    print(price[n])
else:
    print("The store doesnt have this label of computer")

# ex 14
print("Total price =", price["ASUS"]*5)

# ex 15
label = input("Enter the label of the computer ").upper()
if label in price.keys():
    number = int(input("Enter the numbers of the computers "))
    print("Total price =", price[label]*number)
else:
    print("The store doesnt have this label of computer")

# ex 16
if label in price.keys() and label in computers.keys():
    computers[label] -= number
else:
    print("The store doesnt have this label of computer")

# ex 17
new = input("Enter the label and number of the computer, split by : ")
new_list = new.split(":")
for i in new_list:
    if i.isdigit():
        new_list.remove(i)
        i = int(i)
        new_number = i
    elif i.isalpha():
        new_label = i.upper()
if new_label in price.keys() and new_label in computers.keys():
    computers[new_label] -= new_number
else:
    print("The store doesnt have this label of computer")

# ex 18
for key in computers.keys():
    if key in price.keys():
        print("total price of", key, price[key]*computers[key])

# ex 19
total_price = 0
for key in computers.keys():
    if key in price.keys():
        c_price = price[key]*computers[key]
        total_price += c_price
print(total_price)