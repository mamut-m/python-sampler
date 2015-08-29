[![Build Status](https://travis-ci.org/hyperborea/python-sampler.svg)](https://travis-ci.org/hyperborea/python-sampler)
[![Build Status](https://img.shields.io/pypi/dm/sampler.svg?style=flat)](https://pypi.python.org/pypi/sampler)
[![Build Status](https://img.shields.io/pypi/l/sampler.svg?style=flat)](https://github.com/hyperborea/python-sampler/blob/master/LICENSE)


Sampler
===================
Sample data generator for Python


Installation
-------------------
> pip install sampler


Usage
-------------------
```python
from sampler import *

class Person(Sampler):
  id = IncrementField()
  name = NameField()
  gender = ListField(['male', 'female'])
  
  job = Sampler(
    company = WeightedListField([
      ('Acme', 0.8),
      ('Super Corp', 0.2),
    ])
    salary = GaussianField(10000, 5000)
  )
  
Person().generate()
```
