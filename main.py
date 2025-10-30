from character import Character

def main():
    hero = Character("Knight", 30, 5)
    enemy = Character("Goblin", 20, 3)
    enemy2 = Character("Zombie", 15, 2)

    print(hero)
    print(enemy)
    print(enemy2)

    while hero.is_alive() and (enemy.is_alive() or enemy2.is_alive()):
        if enemy.is_alive():
            hero.attack(enemy)
            enemy.attack(hero)
        if enemy2.is_alive():
            hero.attack(enemy2)
            enemy2.attack(hero)
        print(hero)
        print(enemy)
        print(enemy2)

    print("Battle over!")
    if hero.is_alive():
        print(f"{hero.name} wins!")
    else:
        print(f"{enemy.name} & {enemy2.name} wins!")

if __name__ == "__main__":
    main()
