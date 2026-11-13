class Character:
    def __init__(self, name, health=100, attack_power=1, defense=0):
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
