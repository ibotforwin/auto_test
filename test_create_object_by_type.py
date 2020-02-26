import unittest
import create_object_by_type


class TestObjectCreationMethods(unittest.TestCase):
    def test_create_int(self):
        self.assertIsInstance(create_object_by_type.create_object(int), int)

    def test_create_float(self):
        self.assertIsInstance(create_object_by_type.create_object(float), float)

    def test_create_string(self):
        self.assertIsInstance(create_object_by_type.create_object(str), str)

    def test_create_datetime_valid(self):
        import datetime
        self.assertIsInstance(create_object_by_type.create_object(datetime.datetime), datetime.datetime)


if __name__ == '__main__':
    unittest.main()
