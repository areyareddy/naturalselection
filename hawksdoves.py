import random 
import matplotlib.pyplot as plt 

'''class Dove():
    species = 'D'
    def init(self, Hawkmatchup):
        self.Hawkmatchup = Hawkmatchup

class Hawk():
    species = 'H'
    def init(self, Dovematchup):
        self.Dovematchup = Dovematchup

class Shifter():
    species = 'S'
    def init(self, Dovematchup, Hawkmatchup):
        self.Dovematchup = Dovematchup
        self.Hawkmatchup = Hawkmatchup

class Randomer():
    species = 'R'
    def init(self, Doveodds, Hawkodds, Dovematchup, Hawkmatchup):
        self.Doveodds = Doveodds
        self.Hawkodds = Hawkodds
        self.Dovematchup = Dovematchup  
        self.Hawkmatchup = Hawkmatchup'''

def payoff_matrix(creature1, creature2):
    #reduced payoff for shifters, multiplicative
    sval = 0.70
    randomval = random.random()
    #convert Randomers to Hawk/Dove
    if creature1 == 'R':
        if randomval < 0.5:
            creature1 = 'D'
        else:
            creature1 = 'H'
    if creature2 == 'R':
        if randomval < 0.5:
            creature2 = 'D'
        else:
            creature2 = 'H'

    if creature1 == creature2:
        #50-50!
        if creature1 == 'D':
            return (1, 1)
        #hawks fight each other and lose a lot of energy.
        if creature1 == 'H':
            return (0, 0)
        #both shifters.
        if creature1 == 'S':
            return (1*sval, 1*sval)
    else:
        #shifters
        if creature1 == 'S':
            #become a Hawk-ish if it's a Dove
            if creature2 == 'D':
                return (1.5*sval, 0.5)
            #become a Dove-ish if it's a Hawk 
            if creature2 == 'H':
                return (0.5*sval, 1.5)
        #same shifter logic but for creature2 first
        elif creature2 == 'S':
            if creature1 == 'D':
                return (0.5, 1.5*sval)
            if creature1 == 'H':
                return (1.5, 0.5*sval)
        #not shifters
        else:
        #hawk takes 1/2 of dove's piece and eats it before eating its own piece
            if creature1 == 'D':
                return (0.5, 1.5)
            if creature1 == 'H':
                return (1.5, 0.5)
            
#arbitrary number
init_creatures = 200

num_creatures = init_creatures

#initialize list
creature_list = []
doves = 0
hawks = 0
shifters = 200
randoms = init_creatures-doves-hawks-shifters
for _ in range(doves):
    creature_list.append('D')
for _ in range(hawks):
    creature_list.append('H')
for _ in range(shifters):
    creature_list.append('S')
for _ in range(randoms):
    creature_list.append('R')

#basically, the doves are doves (nice and split equally)
#hawks are hawks (unfair and take more for themselves, but hawk vs hawk is bad)
#shifters are smart shifters (shifts into best outcome, but pays cost for maintaining big brain)
#randomers are dumb shifters (randomly 50/50s it)

'''for i in range(init_creatures):
    chancevariable = random.random()
    #half and half append D or H 
    #if chancevariable < 0.5:
    if 0 < chancevariable < 1/4: 
        creature_list.append('D')
        doves += 1
    elif 1/4 < chancevariable < 2/4:
        creature_list.append('H')
        hawks += 1
    elif 2/4 < chancevariable < 3/4:
        creature_list.append('R')
        randoms += 1 
    else:
        creature_list.append('S')
        shifters += 1
    if 0 < i < 5:
        creature_list.append('D')
        doves += 1
    if 5 < i < 10:
        creature_list.append('H')
        hawks += 1
    if 10 < i < 15: 
        creature_list.append('S')
        shifters += 1
    else:
        creature_list.append('R')
        randoms += 1 '''
    
days = []
dove_counts = []
hawk_counts = []
shifter_counts = []
random_counts = []
all_creature_types = ['D', 'H', 'S', 'R']
meeting_chance_init = 0.95
for i in range(1, 200):
    
    #gen_scores
    #print(creature_list)
    num_creatures = len(creature_list)
    payoff_list = [0]*num_creatures

    #set up random matches
    shuffled_indices = list(range(num_creatures))
    random.shuffle(shuffled_indices)

    for counter in range(0, num_creatures-1, 2):
        #chance of meeting another creature
        creaturetype1 = shuffled_indices[counter]
        creaturetype2 = shuffled_indices[counter+1]
        #95% of creatures meet each other, multiplied by num_creatures/200.
        if random.random() < num_creatures/(200/meeting_chance_init):
            #make the payoff tuple
            payoffs = payoff_matrix(
                creature_list[creaturetype1], 
                creature_list[creaturetype2])
            #save the values at the indexes for the CREATURES we paired. 
            payoff_list[creaturetype1] = payoffs[0]
            payoff_list[creaturetype2] = payoffs[1]
        else:
            #these lucky creatures get their box of 2 food all to themselves.
            payoff_list[creaturetype1] = 2
            payoff_list[creaturetype2] = 2

    #evolve
    new_creature_list = []
    mutation_rate = 0.001 
    for pre_replication_creature in range(len(creature_list)):
        payoff = float(payoff_list[pre_replication_creature])
        reproduction_rate = max(0, payoff)
        while reproduction_rate > 0:
            if random.random() < reproduction_rate:
                if random.random() < mutation_rate:
                    mutated_creature = random.choice(all_creature_types)
                    new_creature_list.append(mutated_creature)
                else:
                    new_creature_list.append(creature_list[pre_replication_creature])
            reproduction_rate -= 1
    random.shuffle(new_creature_list)
    days.append(i)
    dove_counts.append(new_creature_list.count('D'))
    hawk_counts.append(new_creature_list.count('H'))
    shifter_counts.append(new_creature_list.count('S'))
    random_counts.append(new_creature_list.count('R'))
    creature_list = new_creature_list
    
# after the simulation loop finishes:
plt.figure()

plt.stackplot(days,
              dove_counts,
              hawk_counts,
              shifter_counts,
              random_counts,
              labels=['Doves','Hawks','Shifters','Randoms'])

plt.xlabel('Days')
plt.ylabel('Creatures')
plt.title('Evolution Simulation')
plt.legend(loc='upper right')

plt.show()

