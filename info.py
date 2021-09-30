def info(name, age):
    print("Hallo " + name + ", je bent " + age + " jaar oud.")
answer = 1
while answer != "stop":
    name = input("Name: ")
    age = input("Age: ")
    info(name, age)
    answer = input('Typ "stop" om the stoppen: ')
