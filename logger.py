from person import Person




class Logger(object):
    ''' Utility class responsible for logging all interactions during the simulation. '''

    def __init__(self, file_name):

        self.file_name = file_name



    def write_metadata(self, pop_size, vacc_percentage, virus_name, mortality_rate,
                       basic_repro_num):
        '''
        The simulation class should use this method immediately to log the specific
        parameters of the simulation as the first line of the file.
        '''

        with open(self.file_name, mode = 'w') as file:
            metadata = f'Population Size: {pop_size}  Vaccination Percentage: {vacc_percentage}  Virus Name: {virus_name}  Mortality Rate: {mortality_rate}  Basic Reproduction Number: {basic_repro_num}\n'
            file.write(metadata)

    def log_interaction(self, person, random_person, random_person_sick=None,
                        random_person_vacc=None, did_infect=None):
        '''
        The Simulation object should use this method to log every interaction
        a sick person has during each time step.

        The format of the log should be: "{person.ID} infects {random_person.ID} \n"

        or the other edge cases:
            "{person.ID} didn't infect {random_person.ID} because {'vaccinated' or 'already sick'} \n"
        '''

        with open(self.file_name, mode = 'a') as file:
            file.write('Interaction Logs: \n')

            if did_infect:
                status = f'{person._id} infects {random_person._id}\n'
                file.write(status)

            elif person.is_vaccinated:
                status = f'{person._id} did not infect {random_person._id}\n'
                file.write(status)

            else:
                status = f'{person._id} did not infect {random_person._id} because {random_person._id} is already sick or vaccinated'
                file.write(status)



    def log_infection_survival(self, person, did_die_from_infection):
        ''' The Simulation object uses this method to log the results of every
        call of a Person object's .resolve_infection() method.

        The format of the log should be:
            "{person.ID} died from infection\n" or "{person.ID} survived infection.\n"
        '''

        with open(self.file_name, mode = 'a') as file:
            file.write('Infection Survival:\n')

            if did_die_from_infection:
                status = f'{person._id} died from infection\n'
                file.write(status)

            else:
                status = f'{person._id} survived infection.\n'
                file.write(status)

    def log_time_step(self, time_step_number):
        ''' STRETCH CHALLENGE DETAILS:

        If you choose to extend this method, the format of the summary statistics logged
        are up to you.

        At minimum, it should contain:
            The number of people that were infected during this specific time step.
            The number of people that died on this specific time step.
            The total number of people infected in the population, including the newly infected
            The total number of dead, including those that died during this time step.

        The format of this log should be:
            "Time step {time_step_number} ended, beginning {time_step_number + 1}\n"
        '''

        with open(self.file_name, mode = 'a') as file:

            file.write('Time Steps: ')
            status = f'Time step {time_step_number} ended, beginning {time_step_number + 1}\n'
            file.write(status)
