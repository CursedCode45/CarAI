from Utils import *
from Player import Player
from Brain import Brain
import copy


class Population:
    def __init__(self):
        self.brains = []
        self.players = []
        self.bestPlayerWeights = None
        self.bestPlayer = None
        self.bestScore = 0


        for i in range(NUMBER_OF_PLAYERS):
            self.players.append(Player())

        for i in range(NUMBER_OF_PLAYERS):
            self.brains.append(Brain())
            self.brains[i].fitness = 0
            self.brains[i].nodes.clear()
            self.brains[i].appendNodes()
            self.brains[i].initAllNodes()


    def updatePlayersMovement(self):
        for i, player in enumerate(self.players):
            if i == self.findBestCurrentPlayer():
                self.players[i].drawWinner()
            self.players[i].moveF()
            self.players[i].calcSpeed()
            self.players[i].rotatePoints()
            self.players[i].calcRaycast()
            self.players[i].draw()


    # Checks dead players and respawns them
    def checkIfPlayersDied(self):
        for i, brain in enumerate(self.brains):
            if self.players[i].hitWall():
                self.players[i].drawNormal()
                brain.fitness = 0
                brain.nodes.clear()
                brain.appendNodes()
                brain.initAllNodes()
                if self.bestPlayerWeights:
                    brain.changeAllNodes(self.bestPlayerWeights)
                    brain.mutateNodesWeights()


    def updateAllPlayersBrain(self):
        for i, brain in enumerate(self.brains):
            brain.updateInputNodes(self.players[i])
            brain.calculateNodesValue()
            brain.fitness += 0.01


    def calculateBrainOutput(self):
        for i, brain in enumerate(self.brains):
            if brain.nodes[len(brain.nodes) - 2].value == 1:
                self.players[i].rotate(True, False)

            elif brain.nodes[len(brain.nodes) - 1].value == 1:
                self.players[i].rotate(False, True)


    def calculateBestScore(self):
        for i in range(len(self.brains)):
            if self.bestScore < self.brains[i].fitness:
                self.bestScore = self.brains[i].fitness
                self.bestPlayer = i
                self.bestPlayerWeights = self.brains[i].allWeights[:]

    def findBestCurrentPlayer(self):
        best = []
        for i, brain in enumerate(self.brains):
            best.append(brain.fitness)

        thePlayer = max(best)
        return best.index(thePlayer)

