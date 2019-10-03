#For testing the project builds
from logger import Logger
from simulation import Simulation
from virus import Virus
from person import Person

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

def test_simulation_should_continue():
    virus = Virus("Small Cough",0.1,0.3)
    subject_1 = Person(0,False,None)
    subject_1.is_alive = False
    subject_2 = Person(1,False,None)
    subject_2.is_alive = True
    subject_3 = Person(2,False,None)
    subject_3.is_alive = False

    test = Simulation(3,0,virus,0)
    test.population.append(subject_1)
    test.population.append(subject_2)
    test.population.append(subject_3)
    some_survive = test._simulation_should_continue()
    assert some_survive == True

def test_simulation():
    virus = Virus("Ebola", 0.3, 0.4)
    sim = Simulation(50, 0.7, virus, 5)
    # assert sim.run() == 'The simulation has ended after 5 turns.'
    pass
