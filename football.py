import random
from geneticAlgorithm import *

#Each position has its own class creating a gene

class Quarterback(Gene):
    def __init__(self, _player):
        # call the parent constructor
        Gene.__init__(self)
        # choose a random value to start
        self.randomInit()
        #follow which player is selected
        self.player = _player

    def printGene(self):
        print "QB = " + str(self.qb)

    def randomInit(self):
        #select random qb
        self.qb = random.choice(["Cam Newton", "Tom Brady", "Drew Brees", "Aaron Rodgers", "Marcus Mariota", "Russell Wilson", "Andrew Luck", "Carson Palmer", "Eli Manning", "Ben Roethlisberger", "Philip Rivers", "Mathew Stafford", "Tyrod Taylor", "Derek Carr", "Jameis Winston", "Kirk Cousins", "Dak Prescott", "Blake Bortles", "Andy Dalton", "Brock Osweiler", "Alex Smith", "Ryan Fitzpatrick", "Matt Ryan", "Joe Flacco", "Sam Bradford", "Robert Girffin III"])

class Runningback(Gene):
    def __init__(self, _player):

        Gene.__init__(self)
        self.randomInit()
        self.player = _player

    def printGene(self):
        print "RB = " + str(self.rb)

    def randomInit(self):
        #select random rb
        self.rb = random.choice(["Le'Veon Bell", "DeMarco Murray", "Ezekiel Elliott", "David Johnson", "LeSean McCoy", "Todd Gurley", "Lamar Miller", "Devonta Freeman", "Adrian Peterson", "Doug Martin", "Mark Ingram","Eddie Lacy", "Spencer Ware", "Latavius Murray", "C.J Anderson", "Ryan Mathews", "Carlos Hyde", "Matt Forte", "Jeremy Hill"])

class Widereciever(Gene):
    def __init__(self, _player):

        Gene.__init__(self)
        self.randomInit()
        self.player = _player

    def printGene(self):
        print "WR = " + str(self.wr)

    def randomInit(self):
        #select random wr
        self.wr = random.choice(["Antonio Brown", "Mike Evans", "Odell Beckham", "A.J Green", "Jordy Nelson", "Julio Jones", "Allen Robinson", "DeAndre Hopkins", "Dez Bryant", "Keenan Allen", "Brandon Marshall", "Sammy Watkins", "Amari Cooper", "Alshon Jeffery", "T.Y Hilton", "Donte Moncrief", "Randall Cobb", "Marvin Jones"])

class Tightend(Gene):
    def __init__(self, _player):

        Gene.__init__(self)
        self.randomInit()
        self.player = _player

    def printGene(self):
        print "TE = " + str(self.te)

    def randomInit(self):
        #select random te
        self.te = random.choice(["Greg Olsen", "Delanie Walker", "Jordan Reed", "Martellus Bennet", "Tyler Eifert", "Gary Barnidge", "Travis Kelce", "Antonio Gates", "Jared Cook", "Julius Thomas", "Coby Fleener", "Dwayne Allen", "Zach Miller", "Zach Ertz", "Jason Witten", "Rob Gronkowski", "Eric Ebron"])

class Kicker(Gene):
    def __init__(self, _player):

        Gene.__init__(self)
        self.randomInit()
        self.player = _player

    def printGene(self):
        print "K = " + str(self.k)

    def randomInit(self):
        #select random k
        self.k = random.choice(["Cairo Santos", "Adam Vinatieri", "Stephen Gostkowski", "Dustin Hopkins", "Will Lutz", "Steven Hauschka", "Dan Bailey", "Chandler Catanzaro", "Mason Crosby", "Graham Gano", "Chris Boswell", "Justin Tucker", "Connor Barth", "Brandon McManus", "Jason Myers", "Matt Prater", "Nick Novak", "Mike Nugent", "Matt Bryant", "Roberto Aguayo"])

class fantasyfootballChromosome(Chromosome):
    def __init__(self, length):
        # call the parent constructor
        Chromosome.__init__(self,length)
        # choose random values for the chromosome
        self.randomInit()
        # initialize fitness score
        self.fitness = self.fitnessFunction()

    def randomInit(self):
        #ADD qb players to chromosome
        for qb in range(0, 2):
            newGene = Quarterback(qb)
            self.genes.append(newGene)
            #if same player is selected re-try and select different player
            if newGene == newGene:
                self.genes.remove(newGene)
                newGene = Quarterback(qb)
                self.genes.append(newGene)
        #ADD rb players to chromosome
        for rb in range(0, 4):
            newGene = Runningback(rb)
            self.genes.append(newGene)
            # if same player is selected re-try and select different player
            if newGene == newGene:
                self.genes.remove(newGene)
                newGene = Runningback(rb)
                self.genes.append(newGene)

        #ADD wr players to chromosome
        for wr in range(0, 4):
            newGene = Widereciever(wr)
            self.genes.append(newGene)

        #ADD te playeres to chromosome
        for te in range(0,2):
            newGene = Tightend(te)
            self.genes.append(newGene)

        #Add k player to chromosome
        newGene = Kicker(1)
        self.genes.append(newGene)

    def fitnessFunction(self):
        fitness = 0
        for i in range(0, 5):
            #QB players
            if Quarterback(0) == 'Tom Brady':
                fitness += 1
            if Quarterback(1) == 'Tom Brady':
                fitness += 1
            if self.genes[i].player == 'Aaron Rodgers':
                fitness += 2
            if self.genes[i].player == 'Drew Brees':
                fitness += 3
            if self.genes[i].player == 'Marcus Mariota':
                fitness += 4
            if self.genes[i].player == 'Russell Wilson':
                fitness += 5
            if self.genes[i].player == 'Andrew Luck':
                fitness += 6
            if self.genes[i].player == 'Carson Palmer':
                fitness += 7
            #RB players
            if self.genes[i].player == 'DeMarco Murray':
                fitness += 1
            if self.genes[i].player == 'Ezekiel Elliot':
                fitness += 2
            if self.genes[i].player == 'David Johnson':
                fitness += 3
            if self.genes[i].player == 'LeSean McCoy':
                fitness += 4
            if self.genes[i].player == 'Todd Gurley':
                fitness += 5
            if self.genes[i].player == 'Lamar Miller':
                fitness += 6
            if self.genes[i].player == 'Devonta Freeman':
                fitness += 7
            #WR players
            if self.genes[i].player == 'Mike Evans':
                fitness += 1
            if self.genes[i].player == 'Odell Beckham':
                fitness += 2
            if self.genes[i].player == 'A.J Green':
                fitness += 3
            if self.genes[i].player == 'Jordy Nelson':
                fitness += 4
            #TE players
            if self.genes[i].player == 'Delanie Walker':
                fitness += 1
            if self.genes[i].player == 'Jordan Reed':
                fitness += 2
            if self.genes[i].player == 'Martellus Bennet':
                fitness += 3
            if self.genes[i].player == 'Tyler Eifert':
                fitness += 4
            #K players
            if self.genes[i].player == 'Adam Vinatieri':
                fitness += 1
            if self.genes[i].player == 'Stephen Gostkowski':
                fitness += 2
            if self.genes[i].player == 'Dustin Hopkins':
                fitness += 3
            if self.genes[i].player == 'Will Lutz':
                fitness += 4
        return fitness

class fantasyFootballPopulation(Population):
    def __init__(self, populationSize, chromosomeSize):
        # call the parent constructor
        Population.__init__(self, populationSize)
        # create a random population
        self.randomPopulation(chromosomeSize)

    def randomPopulation(self, chromosomeSize):
        for i in range(0, self.populationSize):
            self.generation.put(fantasyfootballChromosome(chromosomeSize))

geneticAlgorithm(fantasyFootballPopulation(5,5))


"""
PlayersList = {'QB': ["Cam Newton", "Tom Brady", "Drew Brees", "Aaron Rodgers","Marcus Mariota"],
                       "RB": ["Le'Veon Bell", "DeMarco Murray", "Ezekiel Elliott", "David Johnson", "LeSean McCoy"],
                       "WR": ["Antonio Brown", "Mike Evans", "Odell Beckham", "A.J Green", "Jordy Nelson"],
                       "TE": ["Greg Olsen", "Delanie Walker", "Jordan Reed", "Martellus Bennet", "Tyler Eifert"],
                       "K":  ["Cairo Santos", "Adam Vinatieri", "Stephen Gostkowski", "Dustin Hopkins", "Will Lutz"]}
"""

"""
class fantasyfootball(Gene):
    def __init__(self,_position):# _qub, _rub, _wir, _tie, _ki):

        Gene.__init__(self)

        self.randomInit()
        self.position = _position
        #self.qub = _qub
        #self.rub = _rub
        #self.wir = _wir
        #self.tie = _tie
        #self.ki = _ki


    def printGene(self):

        print 'QB: ' + self.qb
        print 'RB: ' + self.rb
        print 'WR: ' + self.wr
        print 'TE: ' + self.te
        print 'K: ' + self.k

        #1-2 QB
        #print self.qub  + str(self.qb)
        #2-5 RB
        #print self.rub + str(self.rb)
        #print self.wir + str(self.wr)
        #print self.tie + str(self.te)
        #print self.ki + str(self.k)



    def randomInit(self):
        self.qb = random.choice(["Cam Newton", "Tom Brady", "Drew Brees", "Aaron Rodgers","Marcus Mariota"])
        self.rb = random.choice(["Le'Veon Bell", "DeMarco Murray", "Ezekiel Elliott", "David Johnson", "LeSean McCoy"])
        self.wr = random.choice(["Antonio Brown", "Mike Evans", "Odell Beckham", "A.J Green", "Jordy Nelson"])
        self.te = random.choice(["Greg Olsen", "Delanie Walker", "Jordan Reed", "Martellus Bennet", "Tyler Eifert"])
        self.k = random.choice(["Cairo Santos", "Adam Vinatieri", "Stephen Gostkowski", "Dustin Hopkins", "Will Lutz"])

                rb = ["Le'Veon Bell", "DeMarco Murray", "Ezekiel Elliott", "David Johnson", "LeSean McCoy"]
        #loop through positions
        for player in range(0, 5):
            #loop through players of each position

            #add to gene
            newGene = quarterback(qb[player])
            self.genes.append(newGene)

        for player in range(0, 5):
            newGene = runningback(rb[player])
            self.genes.append(newGene)

"""