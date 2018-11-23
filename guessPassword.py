'''
		GENETIC ALGORITHIM THAT WILL GUESS A PASSWORD 
		Created using the help of the book: Gentic Algorithims with python
		www.amazon.com/Genetic-Algorithms-Python-Clinton-Sheppard/dp/1732029806/
'''
import random as rand

class passwordCracker:

	def __init__(self):
		#set up gene
		self.geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!?.1234567890-,"

	#generate a random string from the genes set
	def generateParent(self, length ):
		genes = []
		while len(genes) < length:
			sample = min(length - len(genes), len(self.geneSet))
			genes.extend(rand.sample(self.geneSet, sample))
		return ''.join(genes)

	def getFitness(self, guess, target):
		return sum(1 for expected, actual in zip(target, guess) if expected == actual)
	
	def mutate(self, parent):
		index = rand.randrange(0, len(parent))
		childGenes = list(parent)
		newGene, alternate = rand.sample( self.geneSet, 2)
		childGenes[index] = alternate if newGene == childGenes[index] else newGene
		return ''.join(childGenes)
		

crack = passwordCracker()
target = "I am Daniel. I am Sam. Sam I am. That Sam-I-am. That Sam-I-am!. I do not like. That Sam-I-am. Do you like. Green eggs and ham. I do not like them. Sam-I-am. I do not like Green eggs and ham. Would you like them Here or there? I would not like them Here or there. I would not like them Anywhere. I do not like Green eggs and ham. I do not like them, Sam-I-am Would you like them In a house? Would you like them With a mouse? I do not like them In a house. I do not like them With a mouse. I do not like them Here or there. I do not like them Anywhere. I do not like green eggs and ham. I do not like them, Sam-I-am. Would you eat them In a box? Would you eat them With a fox?"
rand.seed()

bestParent = crack.generateParent(len(target))
bestFitness = crack.getFitness(bestParent, target)

while True:
	child = crack.mutate(bestParent)
	childFitness = crack.getFitness(child, target)
	if bestFitness >= childFitness:
		continue
	print("guess is: " , child, " with a fitness of: ", childFitness)
	if childFitness >= len(bestParent):
		break
	bestFitness = childFitness
	bestParent = child

