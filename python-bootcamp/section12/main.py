# Scope
# enemies = 1


# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside function: {enemies}")  # 2


# increase_enemies()
# print(f"enemies outside function: {enemies}")  # 1


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


# Modifying Global Scope
enemies = 1


def increase_enemies():
    # global enemies
    print(f"enemies inside function: {enemies}")  # 2
    return enemies + 1


enemies = increase_enemies()
print(f"enemies outside function: {enemies}")  # 1


# Modifying Local Scope Test
def test_outter():
    local_test = 1

    def test_inner():
        # nonlocal local_test
        print(f"local_test : {local_test}")
        return local_test + 1
    local_test = test_inner()
    print(f"outter_test : {local_test}")


test_outter()


# Global Constants
PI = 3.14159
URL = "https://www.google.com"


def global_constant():
    return PI - 1


print(global_constant())
print(PI)
