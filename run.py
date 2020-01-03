import solver
import game
import numpy as np

biggest = 0
env = game.Game()
agent = solver.ConvolutionSolver(env.matrix,env.actions,iterations=100_000,decayRate=2)

for i in range(agent.iterations):
    env = game.Game()
    state = env.matrix
    action = 1
    done = False

    while not done:
        new_state, reward, done = env.step(action)

        if not done:
            action = agent.fit(state, new_state, reward)
            state = new_state

    if env.biggest > biggest:
        biggest = env.biggest
    if i % 100 == 0:
        print('iteration #: {}, biggest: {}'.format(i,np.amax(biggest)))
        print(state)