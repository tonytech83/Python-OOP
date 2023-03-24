# Exam: 02. Test Cat
# From: Testing - Lab
# URL: https://judge.softuni.org/Contests/Practice/Index/1948#1

class Cat:

    def __init__(self, name):
        self.name = name
        self.fed = False
        self.sleepy = False
        self.size = 0

    def eat(self):
        if self.fed:
            raise Exception('Already fed.')

        self.fed = True
        self.sleepy = True
        self.size += 1

    def sleep(self):
        if not self.fed:
            raise Exception('Cannot sleep while hungry')

        self.sleepy = False


from unittest import TestCase, main


class CatTests(TestCase):

    def test_cat_initializes_correct(self):
        cat = Cat('Tom')

        self.assertEqual('Tom', cat.name)
        self.assertFalse(cat.fed)
        self.assertFalse(cat.sleepy)
        self.assertEqual(0, cat.size)

    def test_cat_size_increased_after_eating(self):
        cat = Cat('Tom')
        self.assertEqual(0, cat.size)

        cat.eat()

        self.assertEqual(1, cat.size)

    def test_cat_is_fed_after_eating(self):
        cat = Cat('Tom')
        self.assertFalse(cat.fed)

        cat.eat()

        self.assertTrue(cat.fed)

    def test_cat_cannot_eat_after_fed_raises(self):
        cat = Cat('Tom')
        cat.eat()
        self.assertTrue(cat.fed)

        with self.assertRaises(Exception) as ex:
            cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_cat_cannot_asleep_if_not_def_raises(self):
        cat = Cat('Tom')
        self.assertFalse(cat.fed)

        with self.assertRaises(Exception) as ex:
            cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_cat_is_not_sleepy_after_sleep(self):
        cat = Cat('Tom')
        self.assertFalse(cat.fed)
        self.assertFalse(cat.sleepy)

        cat.eat()
        self.assertTrue(cat.sleepy)

        cat.sleep()

        self.assertFalse(cat.sleepy)


if __name__ == '__main__':
    main()
