from characters import Enemy

ENEMY_TYPES = {
    "slime": {"name": "Slime","health": 5,"attack_power": 1,"defense": 0,"exp_reward": 1}
}

def spawn_enemy(enemy):
    data = ENEMY_TYPES[enemy.lower()]
    return Enemy(**data)
