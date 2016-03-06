from Genetic.dna import dna
from Genetic.constants import *
import random

class population(object):
    def __init__(self, genes):
        self.genes = genes
        self.individuals = list()
        self.generation = 0
        for i in range(GENERATION_SIZE):
            self.individuals.append(dna(genes=self.genes))

    def reproduce(self, DNA_tuple):
        strands = (DNA_tuple[0].get_random_strand(), DNA_tuple[1].get_random_strand())
        return dna(strands=strands)

    def next_generation(self, function):
        # TODO insertion sort
        scored_individuals = list()
        for individual in self.individuals:
            genes_values = dict()
            for gene in self.genes:
                genes_values[gene] = individual.get(gene)
            score = function(**genes_values)
            scored_individuals.append((score, individual))
        scored_individuals.sort(key=lambda x: x[0], reverse=True)
        self.individuals = list()
        survivors_size = int((GENERATION_SIZE-1)/2)
        survivors = scored_individuals[:survivors_size]
        for i in range(GENERATION_SIZE-1):           
            parents = list(map(lambda x: x[1], random.sample(survivors, 2)))
            self.individuals.append(self.reproduce(parents))
        # Keep best survivor
        self.individuals.append(survivors[0][1])
        population.display(scored_individuals, self.generation)
        self.generation += 1

    def next_n_generation(self, function, n):
        for i in range(n):
            self.next_generation(function)

    @staticmethod
    def maximize_function(function, n=100):
        pop = population(list(function.__code__.co_varnames))
        pop.next_n_generation(function, n)

    @staticmethod
    def display(scored_individuals, gen):
        print("GENERATION: %s" % gen)
        for scored_individual in scored_individuals:
            score = scored_individual[0]
            individual = scored_individual[1]
            output = ("{:10.%sf} - " % DECIMAL_PRECISION).format(score)
            output += str(individual)
            print(output)
        print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
