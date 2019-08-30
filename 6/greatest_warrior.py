#!usr/bin/python3.5
# -*- coding: utf-8 -*-
"""Greatest warrior."""


class Warrior:
    RANKS = [
        "Pushover",
        "Novice",
        "Fighter",
        "Warrior",
        "Veteran",
        "Sage",
        "Elite",
        "Conqueror",
        "Champion",
        "Master",
        "Greatest",
    ]

    def __init__(self):
        self.level = 1
        self.experience = 100
        self.rank = self.RANKS[0]
        self.achievements = []

    def increment_experience(self, experience):
        if self.experience + experience <= 10000:
            self.experience += experience
        else:
            self.experience = 10000
        self.increment_level()
        self.increment_rank()

    def increment_level(self):
        self.level = self.experience // 100

    def increment_rank(self):
        self.rank = self.RANKS[self.experience // 1000]

    def battle(self, enemy_level):
        if 1 <= self.level <= 100:
            if self.level // 10 < enemy_level // 10 and enemy_level - self.level >= 5:
                return "You've been defeated"
            else:
                if self.level == enemy_level:
                    self.increment_experience(10)
                    return "A good fight"
                elif self.level - enemy_level == 1:
                    self.increment_experience(5)
                    return "A good fight"
                elif self.level - enemy_level >= 2:
                    return "Easy fight"
                elif enemy_level - self.level >= 1:
                    self.increment_experience(20 * (enemy_level - self.level) ** 2)
                    return "An intense fight"
        return "Invalid level"

    def print_status(self):
        print("experience:", self.experience)
        print("level:", self.level)
        print("rank:", self.rank)
        print("achievements:", self.achievements)

    def training(self, training_name, experience, required_level):
        if self.level >= required_level:
            self.increment_experience(experience)
            self.achievements.append(training_name)
            return training_name
        else:
            return "Not strong enough"


if __name__ == "__main__":
    my_warrior = Warrior()
    my_warrior.print_status()

    print("\n---\n", my_warrior.training("Defeated Chuck Norris", 100, 1))
    my_warrior.print_status()
    print("\n---\n", my_warrior.battle(9))
    my_warrior.print_status()

    print("\n---\n", my_warrior.training("Defeated Chuck Norris", 9000, 9))
    print("\n---\n", my_warrior.battle(15))
    my_warrior.print_status()
