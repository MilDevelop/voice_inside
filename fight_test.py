import logger

# Сделать логирование


class Location:  # Сделать, доработать
    def __init__(self, name):
        self.name = name
        self.places = {}
        self.connected_locations = {}
        self.npcs = {"enemys": []}  # НаВеРнОе сделать словарём

    def exit(self):
        pass


class Enemy:
    def __init__(self, name):
        self.name = name

    def take_damage(self, damage):
        self.health = max(self.health - damage, 0)


class Clot(Enemy):
    def __init__(self, hp=50, atk=5):
        super().__init__("Сlot")
        self.health = hp
        self.attack = atk

    def main(self):
        pass


class Player:
    def __init__(self, name):
        self.name = name
        self.health = 1
        self.attack = 15

    def take_damage(self, damage):
        self.health = max(self.health - damage, 0)


class Master:

    @staticmethod
    def fight(player: Player, enemy: Enemy):
        tick = 2
        while tick != 0:
            logger.debug(f"Здоровье врага: {enemy.health}")
            logger.debug(f"Здоровье игрока: {player.health}")
            if player.health > 0 and enemy.health > 0:
                if tick % 2 == 0:
                    print("Выберите действие:", "1) Атака", "2) Ничего", sep='\n')
                    answer = int(input())
                    if answer == 1:
                        print(f"Игрок атакует с силой равной {player.attack}")
                        enemy.take_damage(player.attack)
                    elif answer == 2:
                        pass
                else:
                    print(f"Противник атакует с силой равной {enemy.attack}")
                    player.take_damage(enemy.attack)
                tick += 1
            else:
                if player.health <= 0:
                    print("Поражение манекена")
                elif enemy.health <= 0:
                    print("Противник погиб")
                tick = 0


player1 = Player("Манекен")
enemy1 = Clot()
master = Master()
print(enemy1.name)
master.fight(player1, enemy1)

# Обновление кода от 11.05 с утра
