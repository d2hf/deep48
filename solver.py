import numpy as np
import random

class ConvolutionSolver:
    def __init__(self,state,actions,learningRate = 0.01, discount = 0.95, decayRate = 4, decayStart = 1,
                 iterations = 1_000, epsilon = 1):
        self.matrix = np.array(state)
        self.shape = self.matrix.shape[0]
        self._createTable(actions)
        self.numFits = 0
        self.actions = actions

        self.epsilon = epsilon
        self.learningRate = learningRate
        self.discount = discount
        self.iterations = iterations

        self.decayRate = decayRate
        self.decayStart = decayStart
        self.decayEnd = iterations // self.decayRate
        self.epsilonDecay = self.epsilon / (self.decayEnd - self.decayStart)

    def _createTable(self,actions):
        size = self.shape * (self.shape - 1)
        actions = actions

        self.table = np.random.uniform(low=-2, high=0, size=([size,size] + [len(actions)]))

    def _filter(self,slice):
        if slice[0] == slice[1]:
            return 1
        else:
            return 0

    def discretize(self,state):
        h = self._horizontalConvolution()
        v = self._verticalConvolution()

        return h,v

    def _horizontalConvolution(self):
        sum = 0
        for i in range(self.shape):
            for j in range(self.shape):
                if j + 1 < 4:
                    slice = self.matrix[i,j:j+2]

                    sum += self._filter(slice)
        return sum

    def _verticalConvolution(self):
        sum = 0
        for i in range(self.shape):
            for j in range(self.shape):
                if j + 1 < 4:
                    slice = self.matrix[j:j+2,i]

                    sum += self._filter(slice)
        return sum

    def _maxFutureQ(self,nextState):
        h,v = self.discretize(nextState)

        return np.max(self.table[h,v])
    def _decayEpsilon(self):
        if self.epsilon >0:
            return

        if self.decayEnd >= self.numFits >= self.decayStart:
            self.epsilon -= self.epsilonDecay

    def _pickaction(self):
        self._decayEpsilon()
        if np.random.random() > self.epsilon:
            action = np.argmax(self.table[self.horizontal,self.vertical])
        else:
            action = random.choice(self.actions)
        return action

    def fit(self,state,new_state,reward):
        self.horizontal, self.vertical = self.discretize(state)
        max_future_q = self._maxFutureQ(new_state)

        action = self._pickaction()

        current_q = self.table[self.horizontal,self.vertical,action]

        #Updates Q table
        new_q = (1 - self.learningRate) * current_q + self.learningRate * (reward + self.discount * max_future_q)
        self.table[self.horizontal,self.vertical,action] = new_q

        self.numFits +=1

        return action
# x = np.array([[2,2,4,8],[4,2,2,8],[32,16,8,2],[256,64,32,8]])
# c = ConvolutionSolver(x,[0,1,2,3])
#
# q_table = np.random.uniform(low=-2, high=0, size=([12,12] + [4]))
# #print(q_table)
#
# print(c.fit(x))