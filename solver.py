import numpy as np

class ConvolutionSolver:
    def __init__(self,state,actions,learningRate = 0.01, discount = 0.95):
        self.matrix = np.array(state)
        self.shape = self.matrix.shape[0]
        self._createTable(actions)
        self.numFits = 0

        self.learningRate = learningRate
        self.discount = discount

    def _createTable(self,actions):
        size = self.shape * (self.shape - 1)
        actions = actions

        self.table = np.random.uniform(low=-2, high=0, size=([size,size] + [len(actions)]))

    def _filter(self,slice):
        if len(np.where(slice==0)[0])>0:
            return 0
        elif slice[0] == slice[1]:
            return 1
        else:
            return 0

    def discretize(self,state):
        h = _horizontalConvolution()
        v = _verticalConvolution()

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

    def maxFutureQ(self,nextState):


    def fit(self,state):
        self.discretize(state)
        self.numFits +=1

        return np.argmax(self.table[self.horizontal,self.vertical])

# x = np.array([[2,2,4,8],[4,2,2,8],[32,16,8,2],[256,64,32,8]])
# c = ConvolutionSolver(x,[0,1,2,3])
#
# q_table = np.random.uniform(low=-2, high=0, size=([12,12] + [4]))
# #print(q_table)
#
# print(c.fit(x))