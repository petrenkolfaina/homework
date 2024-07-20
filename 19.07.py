#task 1
def menu(dict, key):

    if key in dict:
        return True
    else:
        return False
dict = {
    "name": "Jane",
    "number": "5"
}
print(menu(dict, "name"))

#task2
def fun(mydict, value):
    keys =[]
    for k, v in mydict.items():
        if v == value:
            keys.append(k)
    return keys

mydict={"a": 1,
        "b": 3,
        "c": 1
        }
print(fun(mydict,value=1))

#task3
mydict = {
    "Ім'я": "Анна",
    "Прізвище": "Мірошніченко",
    "Вік": 20,
    "Факультет":"Інформатика"
}
print(mydict["Ім'я"])
print(mydict["Факультет"])

mydict["середній бал"] = 10

print("Оновлений список", mydict)
