from personService import PersonService
import unittest
from person import Person


class test_classes(unittest.TestCase):

    def test_add(self):
        per1 = Person()
        per1._name = 'oooo'
        per1._surname = 'gn'
        per1._age = 8
        perserv = PersonService()
        perserv.add_person(per1)
        self.assertTrue(perserv.get_personList())

    def test_modif(self):
        per1 = Person()
        per1._name = 'oo'
        per1._surname = 'gn'
        per1._age = 8
        key = 0
        perserv = PersonService()
        perserv.update_person(0, per1)
        self.assertTrue(perserv.get_personList())

    def test_delete(self):
        perserv = PersonService()
        perserv.delete_person(0)
        self.assertEqual(perserv.get_personList(), second={})


if __name__ == "__main__":
    unittest.main()
