import random


class TaskDistributor(object):
    """The object that holds the logics to distribute tasks"""
    def __init__(self, number_tasks, number_persons, population_size):
        self.population_size = population_size
        self.number_tasks = number_tasks
        self.number_persons = number_persons
        self.population = []
        self.intermediate_population = []

    def initialize_population(self):
    	"""Initialize a number of lists, according to the number received in the parameter.
           The list has a range of 100, with sorted values (between 1 and 240).
           The population represents a list of random solutions that can be applied in the problem. 
        """ 

        for z in range(self.population_size):  
            # Each element of the population is called chromosome
            chromosome = []
            for i in range(self.number_tasks):
                chromosome.append(random.randint(1,240))

            self.population.append(chromosome)

    def evaluate_fitness(self, chromosome):
        """Define the fitness function that will be used to compare wich one of the chromosomes are the best.
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

    def selection_by_electism(self, person_evaluation):
        """The selection by eletism consists in get the best list (using the value in the evaluate_fitness function)
           and write it to another list, the intermediate population list        
        """
        for i in self.population_size:
            if person_evaluation[i] < person_evaluation[i + 1]:
                best_chromosome = person_evaluation[i]
            else:
                best_chromosome = person_evaluation[i + 1]

        return person_evaluation.index(best_chromosome)

    def selection_by_tournament(self, person_evaluation):
        """The selection by tournament consists in choosing randomly two fathers 
            (one will be chosen by evaluate_fitness function) and two mothers (same as father).
            From the chosen father and mother, using one-point crossover method, we got two sons, 
            these will be added to the intermediate population
        """
        option_father_1 = self.population[random.randint(0, self.population_size)]
        option_father_2 = self.population[random.randint(0, self.population_size)]

        if person_evaluation[self.population.index(option_father_1)] < person_evaluation[self.population.index(option_father_2)]:
            father = self.population.index(option_father_1)
        else:
            father = self.population.index(option_father_2)

        option_mother_1 = self.population[random.randint(0, self.population_size)]
        option_mother_2 = self.population[random.randint(0, self.population_size)]

        if person_evaluation[self.population.index(option_father_1)] < person_evaluation[self.population.index(option_father_2)]:
            mother = self.population.index(option_mother_1)
        else:
            mother = self.population.index(option_mother_2)

        self.one_point_crossover(father, mother)

    def one_point_crossover(self, father, mother):
        """
            This type of reprodution consists in marking one random point in the arrays and
            merge the first part of the cut of the father with the last of the mother, vice-versa. 
        """
        random_cut_index = random.randint(1, self.population_size) - 1
        sun_1 = father[:random_cut_index] + mother[-random_cut_index:]
        sun_2 = mother[:random_cut_index] + father[-random_cut_index:]
        self.intermediate_population.append(sun_1)
        self.intermediate_population.append(sun_2)


task = TaskDistributor(number_tasks=25, number_persons=3, population_size=5)
task.initialize_population()
person_evaluation = []
print "Initial population: "
for pop in task.population:
    print pop

    person_task = task.evaluate_fitness(pop)
    if person_task == 0:
        return "Solução ótima"
    person_evaluation.append(person_task)

elite_chromosome_index = person_evaluation.append(person_evaluation)
task.intermediate_population.append(task.population[elite_chromosome_index])

# complete the intermediate population with tournament selection
while len(task.intermediate_population) < task.population_size:
    task.selection_by_tournament(person_evaluation)