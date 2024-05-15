edad = int(input("Introduce tu edad: "))

if edad < 12:
    print("Eres un niño.")
elif edad >= 12 and edad < 18:
    print("Eres un adolescente.")
elif edad >= 18 and edad < 65:
    print("Eres un adulto.")
else:
    print("Eres un adulto mayor.")
