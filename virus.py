class Virus(object):
    '''Properties and attributes of the virus used in Simulation.'''

    def __init__(self, name, repro_rate, mortality_rate):
        self.name = name
        self.repro_rate = repro_rate
        self.mortality_rate = mortality_rate


def test_virus_instantiation():
    #TODO: Create your own test that models the virus you are working with
    '''Check to make sure that the virus instantiator is working.'''
    virus = Virus("HIV", 0.8, 0.3)
    assert virus.name == "HIV"
    assert virus.repro_rate == 0.8
    assert virus.mortality_rate == 0.3

def test_virus_instantiation_2():
    virus = Virus("E. Coli", 0.15, 0.04)
    assert virus.name == "E. Coli"
    assert virus.repro_rate == 0.15
    assert virus.mortality_rate == 0.04

def test_virus_instantiation_3():
    virus = Virus("Anthrax", 0.65, 0.2)
    assert virus.name == "Anthrax"
    assert virus.repro_rate == 0.65
    assert virus.mortality_rate == 0.2
