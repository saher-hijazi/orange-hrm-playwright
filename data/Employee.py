from dataclasses import dataclass
from faker import Faker
faker = Faker(['ar_PS'])

@dataclass
class Employee:
    first: str = faker.first_name()
    middle: str =  faker.city()
    last: str =  faker.last_name()

