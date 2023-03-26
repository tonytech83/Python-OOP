from unittest import TestCase, main
from project.hero import Hero


class HeroTests(TestCase):

    def setUp(self) -> None:
        self.hero = Hero('Astarot', 99, 100, 10)
        self.enemy_hero = Hero('Azazel', 80, 80, 10)

    def test_hero_constructor(self):
        username = 'Ivan'
        level = 100
        health = 82.5
        damage = 10.12

        hero = Hero(username, level, health, damage)

        self.assertEqual(username, hero.username)
        self.assertEqual(level, hero.level)
        self.assertEqual(health, hero.health)
        self.assertEqual(damage, hero.damage)

    def test_battle_method_when_hero_attacks_himself_raises(self):
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual('You cannot fight yourself', str(ex.exception))

    def test_battle_method_when_hero_health_is_less_or_equal_to_zero_raises(self):
        for health in [0, -1]:
            self.hero.health = health

            with self.assertRaises(Exception) as ex:
                self.hero.battle(self.enemy_hero)

            self.assertEqual('Your health is lower than or equal to 0. You need to rest', str(ex.exception))

    def test_battle_method_when_enemy_hero_health_is_less_or_equal_to_zero_raises(self):
        for health in [0, -2]:
            self.enemy_hero.health = health

            with self.assertRaises(Exception) as ex:
                self.hero.battle(self.enemy_hero)

            self.assertEqual('You cannot fight Azazel. He needs to rest', str(ex.exception))

    def test_battle_method_when_both_heroes_are_with_health_greater_than_zero(self):
        hero_damage = self.hero.damage * self.hero.level
        enemy_hero_damage = self.enemy_hero.damage * self.enemy_hero.level

        hero_health_expected = self.hero.health - enemy_hero_damage
        enemy_hero_health_expected = self.enemy_hero.health - hero_damage

        self.hero.battle(self.enemy_hero)
        hero_health_actual = self.hero.health
        enemy_hero_health_actual = self.enemy_hero.health

        self.assertEqual(hero_health_expected, hero_health_actual)
        self.assertEqual(enemy_hero_health_expected, enemy_hero_health_actual)

    def test_battle_method_when_both_heroes_health_less_than_zero(self):
        battle_result = self.hero.battle(self.enemy_hero)

        self.assertEqual('Draw', battle_result)

    def test_battle_method_when_both_heroes_health_equal_to_zero(self):
        hero = Hero('A', 1, 1, 1)
        enemy_hero = Hero('B', 1, 1, 1)

        battle_result = hero.battle(enemy_hero)

        self.assertEqual('Draw', battle_result)

    def test_battle_method_when_enemy_hero_health_under_zero_after_battle(self):
        enemy_hero = Hero('B', 1, 1, 1)

        expected_hero_health = self.hero.health + 5 - enemy_hero.damage
        expected_hero_level = self.hero.level + 1
        expected_hero_damage = self.hero.damage + 5

        battle_result = self.hero.battle(enemy_hero)

        self.assertEqual('You win', battle_result)
        self.assertEqual(expected_hero_health, self.hero.health)
        self.assertEqual(expected_hero_level, self.hero.level)
        self.assertEqual(expected_hero_damage, self.hero.damage)

    def test_battle_method_when_enemy_hero_health_equal_zero_after_battle(self):
        self.enemy_hero.level, self.enemy_hero.health, self.enemy_hero.damage = 1, 990, 1

        battle_result = self.hero.battle(self.enemy_hero)

        self.assertEqual('You win', battle_result)

    def test_battle_method_when_hero_health_under_zero_after_battle(self):
        enemy_hero = Hero('B', 100, 1001, 10)
        expected_enemy_hero_level = enemy_hero.level + 1
        expected_enemy_hero_damage = enemy_hero.damage + 5

        battle_result = self.hero.battle(enemy_hero)

        expected_enemy_hero_health = enemy_hero.health

        self.assertEqual('You lose', battle_result)

        self.assertEqual(expected_enemy_hero_level, enemy_hero.level)
        self.assertEqual(expected_enemy_hero_health, enemy_hero.health)
        self.assertEqual(expected_enemy_hero_damage, enemy_hero.damage)

    def test_str_of_hero_object(self):
        expected = "Hero Astarot: 99 lvl\n" \
                   "Health: 100\n" \
                   "Damage: 10\n"

        actual = str(self.hero)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    main()
