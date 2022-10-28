#!/usr/bin/python3
""" """
from tests.test_models.test_base_model import test_basemodel
from models.state import State


class test_state(test_basemodel):
    """ """

    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "State"
        self.value = State

    def test_name3(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)

    def test_create(self):
        """ Test create """
        import MySQLdb
        db = MySQLdb.connect(
            host="localhost", user="Bety",
            passwd="My#dam11Gech", port=3306, db="test")
        cur = db.cursor()
        res1 = cur.execute("SELECT * FROM states where name='California'")
        cur.execute("INSERT INTO states (name) values('California')")
        res2 = cur.execute("SELECT * FROM states where name='California'")
        self.assertEqual(res1 + 1, res2)
