war = "Евразия"
peace = "Остазия"

for i in range(int(input())):
    inp = input()
    if inp == "С кем война?":
        print(war)
    elif inp == "С кем мир?":
        print(peace)
    else:
        war, peace = peace, war
