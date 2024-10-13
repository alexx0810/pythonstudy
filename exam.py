import random
import math


class HealthError(Exception):
    pass


class MoodError(Exception):
    pass


class MoneyError(Exception):
    pass


class Person:
    def __init__(self, name, health=100, mood=100, money=0.0):
        self.name = name
        self.health = health
        self.mood = mood
        self.money = money

    def __str__(self):
        return f'=== {self.name} ===\nЗдоров\'я: {self.health}\nНастрій: {self.mood}\nКапітал: {self.money}'

    def change_state(self, health=0, mood=0, money=0.0):
        self.health += health
        self.mood += mood
        self.money += money

        if self.health < 0:
            raise HealthError("Людина померла!")
        if self.mood < 0:
            raise MoodError("Людина впала в депресію!")
        if self.money < 0:
            raise MoneyError("Людина збанкрутувала!")

    def do(self, action):
        if isinstance(action, Action):
            self.change_state(action.health, action.mood, action.money)

            if isinstance(action, Work) and self.mood > 90:
                if self.money != math.inf:
                    self.money *= 1.1

            elif isinstance(action, Rest) and self.health < 40:
                self.mood *= 0.8
        else:
            raise ValueError


class Action:
    def __init__(self, name, money, mood, health):
        self.name = name
        self.money = money
        self.mood = mood
        self.health = health


class Work(Action):
    pass


class Rest(Action):
    pass


humans = [
    Person(name='Тарас', money=0, mood=100, health=100),
    Person(name='Оля', money=50, mood=90, health=80),
    Person(name='Сергій', money=20, mood=70, health=90)
]

actions = [
    Work(name='Піти на завод', money=50, mood=-10, health=-3),
    Rest(name='Сходити в парк', money=0, mood=15, health=3)
]

while humans:
    human = random.choice(humans)
    action = random.choice(actions)
    try:
        human.do(action)
        print(human)
    except (HealthError, MoodError, MoneyError) as e:
        print(e)
        humans.remove(human)
