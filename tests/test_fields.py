import unittest
from datetime import datetime, date
from sampler import *
from random import Random
from unittest.mock import patch
from faker import Faker

class TestSamplerFields(unittest.TestCase):
    
    # this is called before every test
    def setUp(self):
        random.seed(1337)
        # faker uses its own seed
        Faker.seed(4321)

    
    def assertField(self, field, value):
        class G(Sampler):
            pass
        
        setattr(G, 'field', field)
        self.assertEqual(G().generate()['field'], value)

    
    def test_default(self):
        self.assertField(Field(), None)

    def test_field(self):
        self.assertField(Field("a"), "a")

    def test_transform(self):
        field = Field("hello", transform=lambda x: x + " world")
        self.assertField(field, "hello world")

    def test_name_field(self):
        self.assertField(NameField(), "Jason Brown")

    def test_list_field(self):
        self.assertField(ListField(["foo", "bar"]), "foo")

    def test_weighted_list_field(self):
        field = WeightedListField(
            {
                ("foo", 1),
                ("bar", 10),
            }
        )
        self.assertField(field, "bar")

    def test_gaussian_field(self):
        self.assertField(GaussianField(5, 2),   2.072253837086404 )

    def test_increment_field(self):
        field = IncrementField()
        self.assertField(field, 1)
        self.assertField(field, 2)

    def test_date_field_default(self):
        self.assertField(DateField(), date.today())

    def test_date_field(self):
        min_date = date(2015, 1, 1)
        max_date = date(2016, 1, 1)
        self.assertField(DateField(min_date, max_date), date(2015, 8, 10))

    def test_date_field_format(self):
        d = date(2000, 1, 1)
        self.assertField(
            DateField(d, d, format="%s", transform=int), int(d.strftime("%s"))
        )

    def test_datetime_field(self):
        min_date = datetime(2015, 1, 1)
        max_date = datetime(2016, 1, 1)
        self.assertField(
            DateTimeField(min_date, max_date), datetime(2015, 8, 10, 17, 54, 35)
        )
