class Character:
    def __init__(self, name="noname", health=100, attack_power=1, defense=0):
        self.name = name
        self.max_health = health
        self.health = health
        self.attack_power = attack_power
        self.defense = defense

    def is_alive(self):
        return self.health > 0

    def attack(self, target):
        damage_dealt = max(0, self.attack_power - target.defense)
        target.health = target.health - damage_dealt
        print(f"{self.name} hits {target.name} for {damage_dealt}!")
        print(f"{target.name} has {target.health}/{target.max_health} HP")


class Player(Character):
    def __init__(self,name, health=100, attack_power=1, defense=0):
        super().__init__(name, health, attack_power, defense)
        self.level = 1
        self.exp = 0
        self.exp_to_level = 1

    def gain_exp(self, amount):
        self.exp += amount
        print(f"{self.name} has gained {amount} experience! ({self.exp}/{self.exp_to_level})")

        while self.exp >= self.exp_to_level:
            self.level_up()

    def level_up(self):
        self.exp -= self.exp_to_level
        self.level += 1
        self.exp_to_level = int(self.exp_to_level + 1)

        self.max_health += 1
        self.health = self.max_health
        self.attack_power += 1
        self.defense += 1

        print(f"{self.name} is now level {self.level}!")
        print(f"health increaed by 1")
        print(f"attack power increased by 1")
        print(f"defense increased by 1")

class Enemy(Character):
    def __init__(self, name="noname", health=10, attack_power=1, defense=0, exp_reward=1):
        super().__init__(name, health, attack_power, defense)
        self.exp_reward = exp_reward
