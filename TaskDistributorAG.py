import random
from numpy import *


class TaskDistributor(object):
    """The object that holds the logics to distribute tasks"""
    def __init__(self, number_tasks, population_size):
        self.size = population_size
        self.tasks = number_tasks
        self.population = numpy.empty(population_size)

    def initializePopulation(self):
        for i in range(self.size):
            self.population.append(random.randint(1,240))

    
	        
