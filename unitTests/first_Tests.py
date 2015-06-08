import unittest


from cell import Cell
from entity import Entity
from hero import Hero
from monster import Monster


class testCell(unittest.TestCase):

    def test_coords(self):
        cell = Cell()
        self.assertEqual(cell.coords, (0, 0))
        cell.coords = (12, 41)
        self.assertEqual(cell.coords, (12, 41))

    def test_type(self):
        cell = Cell()
        self.assertEqual(cell.type, '')
        cell.type = 'tree'
        self.assertEqual(cell.type, 'tree')


class testEntity(unittest.TestCase):

    def test_name(self):
        ent = Entity('bai ivan', 1, 10, 0)
        self.assertEqual(ent.name, 'bai ivan')

    def test_attack(self):
        ent = Entity('golem', 10, 10, 10)
        self.assertEqual(ent.attack, 10)

    def test_defence(self):
        ent = Entity('garga', 25, 110, 0)
        self.assertEqual(ent.defence, 110)

    def test_agility(self):
        ent = Entity('Medusa', 10, 10, 50)
        self.assertEqual(ent.agility, 50)


class testHero(unittest.TestCase):

    def test_health(self):
        hero = Hero('bai ivan', 10, 10, 10)
        self.assertEqual(hero.health, 100)
        hero.health -= 25
        self.assertEqual(hero.health, 75)


class testMonster(unittest.TestCase):

    def test_health(self):
        monster = Monster('karakondjul', 10, 10, 10, 2500)
        self.assertEqual(monster.health, 2500)
        monster.health -= 500
        self.assertEqual(monster.health, 2000)


if __name__ == '__main__':
    unittest.main()
