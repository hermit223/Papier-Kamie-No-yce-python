
import random
while True:
    choises = ["kamien","papier","nozyce"]
    computer = random.choice(choises)
    player = None

    while player not in choises:
        player = input("Kamien,Papier,Nozyce?: ").lower()
    print("Ty "+player.upper())
    print("Komputer: "+computer.upper())
    if player==computer:
        print("Remis")
    elif player == "kamien":
        if computer == "papier":
            print("Przegrales")
        if computer == "nozyce":
            print("Wygrales")
    elif player == "papier":
        if computer == "kamien":
         print("Wygrales")
        if computer == "nozyce":
            print("Przegrales")
    elif player == "nozyce":
        if computer == "kamien":
            print("Przegrales")
        if computer == "papier":
            print("Wygrales")

    play_again = input("Zagraj ponownie (tak/nie)?: ").lower()
    if play_again != "tak":
        break
print("Naura")