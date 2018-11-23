'''
		GENETIC ALGORITHIM THAT WILL GUESS A PASSWORD 
		Created using the help of the book: Gentic Algorithims with python
		www.amazon.com/Genetic-Algorithms-Python-Clinton-Sheppard/dp/1732029806/
'''
import random as rand

class passwordCracker:

	def __init__(self):
		#set up gene
		self.geneSet = " abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!.1234567890"

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
target = "Hello Wolrd! 89"
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
	
