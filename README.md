[![Build Status](https://travis-ci.org/hyperborea/python-sampler.svg)](https://travis-ci.org/hyperborea/python-sampler)
[![PyPi](https://img.shields.io/pypi/dm/sampler.svg?style=flat)](https://pypi.python.org/pypi/sampler)
[![License](https://img.shields.io/pypi/l/sampler.svg?style=flat)](https://github.com/hyperborea/python-sampler/blob/master/LICENSE)


Sampler
===================
_Sampler_ is a random data generator written in Python supporting a variety of fields and nested data structures. 

Sampler is available through pip, to install it simply:
> pip install sampler


Basic Usage
-------------------
The desired data schema is defined in Python by subclassing the `Sampler` class and adding `Field` instances. Note that you can nest as many `Sampler` instances as you like to form complex data structures.

```python
from sampler import *

class Person(Sampler):
    id = IncrementField()
    name = NameField()
    gender = ListField(['male', 'female'])
  
    job = Sampler(
        company = WeightedListField([
          ('Acme', 0.8),
          ('Super Corp', 0.2)
        ]),
      salary = GaussianField(10000, 5000)
    )
  
Person().generate()
```

The above snippet will generate exemplary:
```python
{
  'id': 1,
  'name': 'Lloyd Jerde'
  'gender': 'male',
  'job': {
    'company': 'Acme',
    'salary': 15935.377898698585
  }
}
```

By default `generate()` only creates a single instance, but you can pass a number to return a list of instances instead, e.g. `Person.generate(10)` which is the same as `Person.count(10).generate()`.

If you don't know the number of instances you'd like to create in advance you can also pass two numbers to `count(min, max)` which will randomize the batch size.

```python
from sampler import *

class Order(Sampler):
    id = IncrementField()

    items = Sampler(
        description = ListField([
          'Spaceship Superior',
          'Candy Deluxe',
          'Fluffy Ball'
        ]),
        quantity = ListField(range(1, 15))
    ).count(1, 5)

Order().generate(3)
```
This code will generate 3 orders with between 1 and 5 items each.
