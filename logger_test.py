from person import Person
from logger import Logger
from virus import Virus
from simulation import Simulation
import pytest


def test_write_file():

    file_name = 'log.txt'
    log = Logger(file_name)

    log.write_metadata(1500, 25, 'Ebola', .5, 2)

def test_log_interaction():
    file_name = 'log.txt'
    log = Logger(file_name)

    person = Person(3, True, None)
    random_person = Person(1, False, None)

    log.log_interaction(person, random_person, True, False, True)
