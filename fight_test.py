class Enemy:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack = 10

    def take_damage(self, damage):  # Дописать и использовать
        self.health -= damage
        if self.health < 0:
            self.health = 0


class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.attack = 15

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0

    # def attack_enemy(self, enemy):
    #     enemy.take_damage(self.attack)
    # def f_menu(self, enemy_hp):
    #     print("Выберите действие:", "1) Атака", "2) Ничего", sep='\n')
    #     answer = int(input())
    #     if answer == 1:
    #         print(enemy_hp)
    #         print(self.attack)
    #         enemy_hp -= self.attack
    #     else:
    #         pass

    # def take_damage(self, damage):  # Дописать и использовать
    #     self.health -= damage
    #     if self.health < 0:
    #         self.health = 0


class Master:

    @staticmethod
    def fight(player: Player, enemy: Enemy):
        tick = 2
        while tick != 0:
            if player.health > 0 and enemy.health > 0:
                if tick % 2 == 0:
                    print("Выберите действие:", "1) Атака", "2) Ничего", sep='\n')
                    answer = int(input())
                    if answer == 1:
                        print(enemy.health)
                        print(player.attack)
                        enemy.take_damage(player.attack)
                    else:
                        pass
                else:
                    player.take_damage(enemy.attack)
                tick += 1
            else:
                if player.health <= 0:
                    print("game over")
                elif enemy.health <= 0:
                    print("The opponent lost ")
                tick = 0
            # print(player.health)
            # print(enemy.health)
    # @staticmethod
    # def fight_menu(player, enemy):
    #     print("Выберите действие:", "1) Атака", "2) Ничего", sep='\n')
    #     answer = int(input())
    #     if answer == 1:
    #         print(enemy.health)
    #         print(player.attack)
    #         enemy.take_damage(player.attack)
    #     else:
    #         pass


player1 = Player("Маникен")
enemy1 = Enemy("Тестовый враг")
master = Master
master.fight(player1, enemy1)
