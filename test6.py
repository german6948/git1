# easy
# Задача1
class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.stop = name
        self.is_police = is_police

    def go(self):
        print('Машина {} поехала'.format(self.speed))


    def stop(self):
        print('Машина {} остановилась'.format(self.stop))

    def turn(self, direction):
        print('Машина {} повернула'.format(self.stop, direction))


class SportCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        Car.__init__(self, speed, color, name, is_police=False)

class WorkCar(Car):
    def __init__(self, speed, color, name, is_police=False):
        Car.__init__(self, speed, color, name, is_police=False)

class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police=True):
        Car.__init__(self, speed, color, name, is_police=True)

# Задача№2
Car1 = WorkCar(60, 'black', 'Kamaz')
Car2 = SportCar(200, 'red', 'BMW')


# normal
# Задача 1
import random


class Person:
    def __init__(self, name, health, damage, armor):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor

    def _income_damage(self, damage):
        if self.armor > 0:
            self.armor = self.armor - int(damage*random.uniform(0.1, 1.0))
            if self.armor <= 0:
                self.armor = 0
        else:
            self.health = self.health - int(damage*random.uniform(0.1, 1.0))
            if self.health <= 0:
                self.health = 0

        print('{} получил урон и теперь имеет {} здоровья, {} армора'.format(self.name, self.health, self.armor))

    def punch(self, person):
        person._income_damage(self.damage)


class Player(Person):
    можно использовать pass
    def __init__(self, name, health, damage, armor):
        Person.__init__(self, name, health, damage, armor)


class Enemy(Person):
    можно использовать pass
    def __init__(self, name, health, damage, armor):
        Person.__init__(self, name, health, damage, armor)


class Fight:
    def __init__(self, person1, person2):
        self.person1 = person1
        self.person2 = person2

    def start(self, person1, person2):
        while person1.health > 0 and person2.health > 0:
            person1.punch(person2)
            if person2.health == 0:
                print(' {} победил!'.format(person1.name))
                break
            person2.punch(person1)
            if person1.health == 0:
                print(' {} победил!'.format(person2.name))


player = Player('Давид Геранович', 100, 10, 50)
enemy = Enemy('Владислав Гермаонвич', 100, 10, 50)

new_fight = Fight(player, enemy)
new_fight.start(player, enemy)

# Hard
# задача
class Toy:

    def __init__(self, name, color):
        self.name = name
        self.color = color


class ToyAnimal(Toy):

    def __init__(self, name, color):
        Toy.__init__(self, name, color)
        self.type = 'Животное'


class ToyMult(Toy):

    def __init__(self, name, color):
        Toy.__init__(self, name, color)
        self.type = 'Мультфильм'


class ToyFactory:

    def create_toy(self, name, color, toy_type):
        self._buy_raw_materials()
        self._sewing()
        self._set_color()
        if toy_type == 'animal':
            return ToyAnimal(name, color)
        elif toy_type == 'mult':
            return ToyMult(name, color)

    def _buy_raw_materials(self):
        print('Закупка материалов.')

    def _sewing(self):
        print('Пошивка игрушки.')

    def _set_color(self):
        print('Окраска игрушки.')



