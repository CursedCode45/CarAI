from Node import Node


class Brain:
    def __init__(self):
        self.nodes = []
        self.allWeights = []
        self.allBiases = []
        self.fitness = 0

        self.num_of_input_Nodes = 5
        self.num_of_hidden_Nodes = 6
        self.num_of_output_Nodes = 2


    def appendNodes(self):
        # Appends input nodes and set's node value to car ray cast distance
        for i in range(self.num_of_input_Nodes):
            self.nodes.append(Node(0))

        # Appends hidden nodes and set's it's layer to 1
        for i in range(self.num_of_hidden_Nodes):
            self.nodes.append(Node(1))

        # Appends output nodes and set's it's layer to 2
        for i in range(self.num_of_output_Nodes):
            self.nodes.append(Node(2))


    # Gets and saves the value of input nodes it's connected to and their weights
    # Supposed to use at the start of the game
    def initAllNodes(self):
        # Empty's the weights and biases, so it can fill them up again fresh
        self.allWeights.clear()
        # weights in a single 1D array
        weights = []

        for x, node in enumerate(self.nodes):
            if node.layer != 0:
                node.getPrevLayerValues(self.nodes)
                node.initWeights()
                node.mutateWeights()
                for weight in node.weights:
                    weights.append(weight)

        self.allWeights = weights
        weights = []


    # Sets Input nodes equal to car ray cast distance
    def updateInputNodes(self, car):
        for i in range(self.num_of_input_Nodes):
            self.nodes[i].value = car.rays[i]


    # Calculates nodes value using the weights and value of nodes it's connected to
    def calculateNodesValue(self):
        for i, node in enumerate(self.nodes):
            if node.layer != 0:
                node.getPrevLayerValues(self.nodes)
                node.calculateValue()



    # Changes every node weights to self.allWeights
    def changeAllNodes(self, newWeights):
        arr = newWeights[:]
        self.allWeights = newWeights[:]
        for i, node in enumerate(self.nodes):
            if node.layer == 0:
                continue
            for j, weight in enumerate(node.weights):
                node.weights[j] = arr[0]
                arr.pop(0)



    def mutateNodesWeights(self):
        arr = self.allWeights[:]
        weightsArr = []
        for x, node in enumerate(self.nodes):
            if node.layer != 0:
                for weight in node.weights:
                    weight = arr[0]
                    arr.pop(0)
                node.smallMutateWeights()
                for weight in node.weights:
                    weightsArr.append(weight)

        self.allWeights = weightsArr[:]
        weightsArr = []



    def getAllWeights(self):
        return self.allWeights
