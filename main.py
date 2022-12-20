import random


def game() -> bool:
    for bullet in range(1, 6):
        killer_bullet = random.randint(1, 6)
        input("Press enter to pull the trigger ")
        if bullet == killer_bullet:
            print("You was killed\nGame Over")
            return False
        print("You survive")
    print("You won")
    return True


if __name__ == "__main__":
    game()
