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

# There is no Block Scope
# 둘러싼 함수와 같은 스코프를 가짐, 둘러싼 함수가 없으면 전역 스코프를 가짐

if 3 > 2:
    a_variable = 10
    print(f"a_variable : {a_variable}")


game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)
