import unittest
from sampler import *
from faker import Faker
import random


class TestSampler(unittest.TestCase):
    # this is called before every test
    def setUp(self):
        random.seed(1337)
        # faker uses its own seed
        Faker.seed(4321)

    def test_generate(self):
        class G(Sampler):
            field = Field()

        result = G().generate()
        self.assertEqual(result, {"field": None})

    def test_generate_count(self):
        class G(Sampler):
            field = Field()

        res1 = G().generate(2)
        res2 = G().count(2).generate()

        self.assertEqual(len(res1), 2)
        self.assertEqual(res1, res2)

    def test_context(self):
        class G(Sampler):
            field1 = Field(1337, var="x")
            field2 = Field(var="x")

        result = G().generate()
        self.assertEqual(result["field1"], result["field2"])

    def test_invisible_variable(self):
        class G(Sampler):
            _invisible = Field(1337)
            clone = CloneField("_invisible")

        result = G().generate()
        self.assertNotIn("_invisible", result)
        self.assertEqual(result["clone"], 1337)

    def test_nested(self):
        class G(Sampler):
            nested = Sampler(field=Field(1337))

        result = G().generate()
        self.assertEqual(result, {"nested": {"field": 1337}})

    def test_nested_list(self):
        class G(Sampler):
            nested = Sampler(field=Field(1337)).count(5)

        result = G().generate()
        self.assertEqual(len(result["nested"]), 5)

    def test_nested_list_random_length(self):
        class G(Sampler):
            nested = Sampler(field=Field(1337)).count(3, 7)

        result = G().generate()
        self.assertEqual(len(result["nested"]), 7)
