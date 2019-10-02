#For testing the project builds
from logger import Logger
from simulation import Simulation
from virus import Virus

def test_create_population():
    virus = Virus("Small Cough",0.1,0.3)
    group = simulation.Simulation(10,0.5,2,virus)
    pop = group._create_population(2)
    assert len(pop) == 10
    pass
