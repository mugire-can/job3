# job 1
valeur1 = input("Veuillez entrer la première valeur")
valeur2 = input("Veuillez entrer la deuxième valeur")

if valeur1 == valeur2:
        print("Valeur1 est égal à valeur2")
else valeur1 != valeur2:
        print("Les deux valeurs ne sont pas égales")


## job 2

age = int(input("Veuillez entrer votre age"))

if age >= 18:
        print(Tu peux voter)
else age <18:
        print(Tu ne peux pas voter)


## job 3

for x in range(101):
    if x == 26 or x == 37 or x == 88:
        continue
    print(x)

## job 4

for x in range(101):
    if x % 3 == 0 and x % 5 == 0:
        print("FizzBuzz")
    elif x % 3 == 0:
        print("Fizz")
    elif x % 5 == 0:
        print("Buzz")
    else:
        print(x)


##job 5

def est_premier(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
for num in range(2, 1001):
    if est_premier(num):
        print(num)


## job 6

nombre = int(input("Veuillez entrer un nombre : "))
if nombre % 2 == 0:
    print("Le nombre {nombre} est pair")
else:
    print("Le nombre {nombre} est impair")

    
## job 7

for i in range(1, 21):  # 20 lignes pour la pyramide
    if index + i <= len(chaine):
        print(chaine[index:index + i])
        index += i
    else:
        break


## job 8

# Fonction pour vérifier si un triangle est constructible
def est_constructible(a, b, c):
    return a + b > c and a + c > b and b + c > a

# Fonction pour déterminer le type de triangle
def type_de_triangle(a, b, c):
    if a == b == c:
        return "équilatéral"
    elif a == b or b == c or a == c:
        if a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
            return "rectangle isocèle"
        return "isocèle"
    elif a**2 + b**2 == c**2 or b**2 + c**2 == a**2 or a**2 + c**2 == b**2:
        return 