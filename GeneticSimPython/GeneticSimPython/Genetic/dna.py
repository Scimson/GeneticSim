from Genetic.constants import *
import random
from collections import OrderedDict

class dna(object):
    """Object that holds genetic information as a pair of strands
       - Each strand is a dict of numbers
    """
    def __init__(self, genes=[], strands=None):
        if strands is None:
            self.strands = (OrderedDict(), OrderedDict())
            for gene in genes:
                for strand in self.strands:
                    strand[gene] = dna.random_gene_value()
        else:
            self.strands = strands

    def get_random_strand(self):
        strand = self.strands[0] if random.random() < 0.5  else self.strands[1]
        return dna.mutate_strand(strand.copy())
    
    def get(self, key):
        return (self.strands[0][key] + self.strands[1][key])/2

    def __str__(self):
        output = ""
        if VERBOSE:
            for i in range(2):
                output += '[%s]: ' % i
                for key in self.strands[i]:
                    output += dna.format_output(key, self.strands[i][key])
                if i != 1:
                    output += "|/\| "
        else:
            for key in self.strands[0]:
                output += dna.format_output(key, self.get(key))
            pass
        return output

    def __repr__(self):
        return self.__str__()

    @staticmethod
    def format_output(key, value):
        return ('[%s]: {:8.%sf} ' % (key, DECIMAL_PRECISION)).format(value)

    @staticmethod
    def mutate_strand(strand):
        for key in strand:
            if random.random() < MUTATION_PROBABILITY:
                strand[key] = (((random.random() - 0.5) * MUTATION_SIZE) + 1) * strand[key]
        return strand


    @staticmethod
    def random_gene_value():
        return (random.random() - 0.5) * INITIAL_GENE_VALUE_LIMIT
    


