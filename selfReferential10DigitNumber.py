from random import randint,random
import numpy as np

#the answer is (['6', '2', '1', '0', '0', '0', '1', '0', '0', '0'], 0)

ints = ['0','1','2','3','4','5','6','7','8','9']
pop_size = 10000
class creature(object):
    """docstring for gene"""
    def __init__(self, genome):
        super(creature, self).__init__()
        self.genome = genome
        self.get_cost()
    def mutate(self):
        if randint(0,100)<3:
            idx = randint(0,9)
            r = random()
            if random>.5:
                n = 1
            else:
                n = -1
            self.genome[idx]= str((int(self.genome[idx])+n)%10)

    def mate(self,other):
        idx = randint(0,9)
        children = []
        child1 = creature(self.genome[0:idx]+other.genome[idx:13])
        children.append(child1)
        children.append(creature(other.genome[0:idx]+self.genome[idx:13]))
        return(children)

    def get_cost(self):
        self.cost =0
        for i,n in enumerate(self.genome):
            n = int(n)
            k = self.genome.count(str(i))
            self.cost+= (n-k)**2


population = [creature(list(str(randint(1000000000, 9999999999)))) for individual in range(pop_size)]


mating_pool_size = pop_size/4

number_of_generations = 1000



for generation in range(number_of_generations):
    population.sort(key=lambda x: x.cost, reverse=False)
    mating_pool = population[0:mating_pool_size]
    viability = np.array([1/(float(c.cost)+.000001)for c in mating_pool])
    viability = viability/np.sum(viability)
    print(population[0].genome,population[0].cost)
    if population[0].cost == 0:
        break
    for i in range(mating_pool_size):
        luck = random()
        i2 = np.random.choice(range(mating_pool_size),p = viability)
        if i2 == i:
            i2 = i+1
        new_kids = population[i].mate(population[i2])
        population[-2-i] = new_kids[0]
        population[-1-i] = new_kids[1]


    for c in population:
        c.mutate()
        c.get_cost()
