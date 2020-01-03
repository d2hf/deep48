import solver
import game

LEARNING_RATE = 0.1

DISCOUNT = 0.95
EPISODES = 25_000

env = game.Game()
agent = solver.ConvolutionSolver(env.matrix,env.actions)
state = env.matrix
action = agent.fit(env.matrix)
# done = False
# while not done:
for i in range(10):
    print(state,action)
    state, reward, done = env.step(action)

    action = agent.fit(state)