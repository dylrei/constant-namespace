# constant-namespace
A Python base class that promotes cleanly-namespaced constant syntax

## installation
```bash
python -m pip install git+https://github.com/dylrei/constant-namespace.git
```

## purpose and usage
ConstantNamespace makes namespaced constants less clunky. 

Instead of:
```python
SOME_DOMAIN_VALUE_ONE = 'value_one'
SOME_DOMAIN_VALUE_TWO = 'value_two'

def value_in_some_domain(value):
    return value in [SOME_DOMAIN_VALUE_ONE, SOME_DOMAIN_VALUE_TWO]

def value_is_value_one(value):
    return value == SOME_DOMAIN_VALUE_ONE
```

Use ConstantNamespace:
```python
# file: path/to/constants.py
# ==========================
from constant_namespace import ConstantNamespace


class SomeDomain(ConstantNamespace):
    VALUE_ONE = 'value_one'
    VALUE_TWO = 'value_two'

    
# file: path/to/lib.py
# ====================
from constants import SomeDomain


def value_in_some_domain(value):
    return value in SomeDomain.values()

def value_is_value_one(value):
    return value == SomeDomain.VALUE_ONE
```

## other examples
Use it for validation
```python
# file: path/to/constants.py
# ==========================
from constant_namespace import ConstantNamespace


class RequiredField(ConstantNamespace):
    NAME = 'name'
    TITLE = 'title'
    EMAIL = 'email'
    
# file: path/to/validators.py
# ===========================
from path.to.constants import RequiredField

def validate_data(data):
    for field in RequiredField.values():
        if data.get(field) is None:
            raise ValidationError(f'Field {field} is required')
```

Use it for configuring Django CharField choices and default
```python
# file: path/to/constants.py
# ==========================
from constant_namespace import ConstantNamespace


class AcceptableAnimalType(ConstantNamespace):
    DOG = 'dog'
    CAT = 'cat'
    TURTLE = 'turtle'
    

class KennelSize(ConstantNamespace):
    SMALL = '6X8'
    MEDIUM = '8X10'
    LARGE = '10X12'

# file: path/to/models.py
from path.to.constants import AcceptableAnimalType, KennelSize


class BoardingStay(models.Model):
    kennel_size = models.CharField(max_length=25, 
                                   default=KennelSize.MEDIUM)
    animal_type = models.CharField(max_length=50, 
                                   choices=AcceptableAnimalType.choices())
```

Create an API endpoint that exposes constant namespaces and key/value pairs to your front end
```python
from path.to.consants import AcceptableAnimalType, KennelSize, ServiceType

public_namespaces = [AcceptableAnimalType, KennelSize, ServiceType]

def get_constants(request):
    return JSONResponse({ns.document() for ns in public_namespaces})
```