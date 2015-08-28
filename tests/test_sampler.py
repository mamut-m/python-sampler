import unittest
from sampler import *


class TestSampler(unittest.TestCase):

    def test_generate(self):
        class G(Sampler):
            field = Field()

        result = G().generate()
        self.assertEqual(result, {'field': None})

    def test_generate_count(self):
        class G(Sampler):
            field = Field()

        result = G().generate(2)
        self.assertEqual(len(result), 2)

    def test_context(self):
        class G(Sampler):
            field1 = Field(1337, var='x')
            field2 = Field(var='x')

        result = G().generate()
        self.assertEqual(result['field1'], result['field2'])

    def test_invisible_variable(self):
        class G(Sampler):
            _invisible = Field(1337)
            clone = CloneField('_invisible')

        result = G().generate()
        self.assertNotIn('_invisible', result)
        self.assertEqual(result['clone'], 1337)

    def test_nested(self):
        class G(Sampler):
            nested = Sampler(
                field = Field(1337)
            )

        result = G().generate()
        self.assertEqual(result, {'nested': {'field': 1337}})
