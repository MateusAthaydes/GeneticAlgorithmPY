import random


class TaskDistributor(object):
    """The object that holds the logics to distribute tasks"""
    def __init__(self, number_tasks, number_persons, population_size):
        self.size = population_size
        self.number_tasks = number_tasks
        self.number_persons = number_persons
        self.population = []

    def initialize_population(self):
    	"""Initialize a number of lists, according to the number received in the parameter.
           The list has a range of 100, with sorted values (between 1 and 240).
           The population represents a list of random solutions that can be applied in the problem. 
        """ 

        for z in range(self.size):  
            # Each element of the population is called chromosome
            chromosome = []
            for i in range(self.number_tasks):
                chromosome.append(random.randint(1,240))

            self.population.append(chromosome)

    def evaluate_fitness(self, chromosome):
        """Define the fitness function that will be use to compare wich one of the chromosomes are the best.
           This function consists in divide the population in equal chunks (these are going to be our persons).
           Sum the value of the each tasks for each chunk.
           Subtract the base value for each person and return that number.
           Closest that number is to zero, better is the solution (chromosome). 
        """
        person_task_list = self.slice_list(chromosome)
        person_value = 0
        for person in person_task_list:
            if person_value:
                person_value = sum(person) - person_value
            else:
                person_value = sum(person)

        return person_value

    def slice_list(self, chromosome):
        slice_size = self.number_tasks / self.number_persons
        remain = self.number_tasks % self.number_persons
        result = []
        iterator = iter(chromosome)
        for i in range(self.number_persons):
            result.append([])
            for j in range(slice_size):
                result[i].append(iterator.next())
            if remain:
                result[i].append(iterator.next())
                remain -= 1
        return result


task = TaskDistributor(25, 3, 5)
task.initialize_population()
for pop in task.population:
    print task.evaluate_fitness(pop)
