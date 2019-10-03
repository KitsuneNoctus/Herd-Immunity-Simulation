#For testing the project builds
from logger import Logger
from simulation import Simulation
from virus import Virus

def test_create_population():
    virus = Virus("Small Cough",0.1,0.3)
    group = Simulation(10,0.5,virus,2)
    pop = group._create_population(2)
    assert len(pop) == 10
    count_infected = 0
    count_vaccinated = 0
    for person in pop:
        if person.infection == virus:
            count_infected += 1
            print("is infected")
            assert person.infection == virus
        elif person.is_vaccinated == True:
            print("Is vacinated")
            count_vaccinated += 1
        else:
            print("Is not vaccinated or infected")

    assert count_infected == 2
    assert count_vaccinated == 5
