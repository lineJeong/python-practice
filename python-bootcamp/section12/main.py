# Scope
enemies = 1


def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")  # 2


increase_enemies()
print(f"enemies outside function: {enemies}")  # 1


# Local Scope
def drink_potion():
    potion_strenth = 2
    print(f"Local Scope : {potion_strenth}")


drink_potion()
# print(potion_strenth)


# Global Scope
player_health = 10


def game():
    def print_health():
        print(player_health)

    print_health()


game()
print(player_health)
