from Utils import *
import random



class Node:
    def __init__(self, layer, value=0):
        self.layer = layer
        self.bias = 0
        self.value = value
        self.weights = []
        self.prevLayerValues = []
        self.biasMax = 200
        self.biasMin = -200

        self.smallMutateValue = 1
        self.smallMutateChance = 0.2


    def getPrevLayerValues(self, nodes):
        self.prevLayerValues = []
        for node in nodes:
            if node.layer + 1 == self.layer:
                self.prevLayerValues.append(node.value)

    def initWeights(self):
        for val in self.prevLayerValues:
            self.weights.append(0)


    # Mutates weights at barin init
    def mutateWeights(self):
        for i, weight in enumerate(self.weights):
            weight += random.uniform(-1, 1)
            weight = min(weight, 1)
            weight = max(weight, -1)
            self.weights[i] = weight


    def calculateValue(self):
        a = 0
        for i, weight in enumerate(self.weights):
            a += self.weights[i] * self.prevLayerValues[i]

        self.value = a + self.bias

        self.value = ReLU(self.value)
        if self.layer == 2:
            if self.value > 1:
                self.value = 1
            else:
                self.value = int(self.value)


    # Mutates weights at a small rate
    def smallMutateWeights(self):
        for i, weight in enumerate(self.weights):
            # Has a self.smallMutateChance % chance of mutating weights
            if random.uniform(0, 1) <= self.smallMutateChance:
                self.weights[i] += random.uniform(-self.smallMutateValue, self.smallMutateValue)
                self.weights[i] = min(self.weights[i], 1)
                self.weights[i] = max(self.weights[i], -1)


    def smallMutateBias(self):
        # Has a 10% chance of mutating the bias
        if random.uniform(0, 1) <= 0.1:
            self.bias += random.randint(-100, 100)
            self.bias = min(self.bias, self.biasMax)
            self.bias = max(self.bias, self.biasMin)


