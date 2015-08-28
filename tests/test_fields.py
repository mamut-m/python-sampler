import unittest
from sampler import *


class TestSamplerFields(unittest.TestCase):
    def assertField(self, field, value):
        class G(Sampler):
            pass

        setattr(G, 'field', field)
        self.assertEqual(G().seed(1337).generate()['field'], value)


    def test_default(self):
        self.assertField(Field(), None)

    def test_field(self):
        self.assertField(Field('a'), 'a')

    def test_transform(self):
        field = Field('hello', transform=lambda x: x + ' world')
        self.assertField(field, 'hello world')

    def test_name_field(self):
        self.assertField(NameField(), 'Kinsley Hickle')

    def test_list_field(self):
        self.assertField(ListField(['foo', 'bar']), 'bar')

    def test_weighted_list_field(self):
        field = WeightedListField({
            ('foo', 1),
            ('bar', 10),
        })
        self.assertField(field, 'bar')

    def test_gaussian_field(self):
        self.assertField(GaussianField(5, 2), 3.1764934134046747)

    def test_increment_field(self):
        field = IncrementField()
        self.assertField(field, 1)
        self.assertField(field, 2)

