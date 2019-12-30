import numpy as np
import random

class Game:
    def __init__(self,n=4):
        self.size = n
        self.game_state = 0

        self._start_matrix()


    def _start_matrix(self):
        self.matrix = np.zeros(shape=(self.size,self.size))
        self.add_number()
        self.add_number()

    def add_number(self):
        add_numbers = [2,4]
        if self.game_state != 2:
            avlb = np.where(self.matrix == 0)
            idx = random.randint(0, len(avlb[0]) - 1)

            self.matrix[avlb[0][idx],avlb[1][idx]] = random.choice(add_numbers)

    def sum_left(self):
        if self.game_state != 2:
            added = False
            for row in range(self.matrix.shape[0]):
                nzeros = np.where(self.matrix[row] !=0)

                if len(nzeros[0])>1: # sum
                    for jdx in range(len(nzeros[0])):
                        if jdx+1 < len(nzeros[0]):

                            idx = nzeros[0][jdx]
                            idx2 = nzeros[0][jdx+1]

                            if self.matrix[row][idx] == self.matrix[row][idx2]:
                                self.matrix[row][idx] *= 2
                                self.matrix[row][idx2] = 0
                                added= True
            self.slide_left(added)

    def slide_left(self,add):
        slided = add
        for row in range(self.matrix.shape[0]):
            nzeros = np.where(self.matrix[row])
            for jdx in range(len(nzeros[0])):
                idx = nzeros[0][jdx]
                self.matrix[row,jdx] = self.matrix[row, idx]
                if idx != jdx:
                    self.matrix[row, idx] = 0
                    slided = True
        if slided:
            self.add_number()

    def check_state(self):
        size = self.matrix.shape[0]

        if len(np.where(self.matrix == 0)[0]) > 0:
            return

        # check if there is equal numbers on the y axis
        for row in range(size):
            for item in range(size):
                if item + 1 < size:
                    if self.matrix[row,item] == self.matrix[row,item+1]:
                        return
        for col in range(size):
            for item in range(size):
                if item + 1 < size:
                    if self.matrix[item,col] == self.matrix[item+1,col]:
                        return

        self.game_state = 2




    def up(self):
        self.matrix = np.transpose(self.matrix)

        self.sum_left()

        self.matrix = np.transpose(self.matrix)

    def left(self):
        self.sum_left()

    def right(self):
        self.matrix = np.fliplr(self.matrix)

        self.sum_left()

        self.matrix = np.fliplr(self.matrix)

    def down(self):
        self.matrix = np.transpose(self.matrix)
        self.matrix = np.fliplr(self.matrix)

        self.sum_left()

        self.matrix = np.fliplr(self.matrix)
        self.matrix = np.transpose(self.matrix)

    def step(self,direction):
        if direction in [0,1,2,3]:
            if direction == 0:
                self.left()
            elif direction == 1:
                self.right()
            elif direction == 2:
                self.up()
            elif direction == 3:
                self.down()
            self.check_state()
            print(self.matrix)
        else:
            print('movement not allowed')

moves = [0,1,2,3]
g =  Game()
while (g.game_state != 2):
    g.step(random.choice(moves))