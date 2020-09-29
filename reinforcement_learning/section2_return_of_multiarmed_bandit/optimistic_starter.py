# OPtimistic initial values 
# https://medium.com/@farbluestar/reinforcement-learning-part-03-355be5c7cae4
# In our multi-armed bandit code, we needed to give actions some initial value before we proceed with our estimation process. 
# Natural choice was to give all actions a value of zero (we used a ZeroInitializer for this — defined in initializers.py).
# The effect of choosing zero for all action values was that the first time the agent needs an action, 
# it will choose a random one. Second time, agent can still choose the same action if it made a greedy choice. 
# Wouldn’t it be better if we cycle through all actions and try each one first before we go greedy? 
# This is the idea behind optimistic initial value. 
# It promotes more exploration in the beginning until we have some estimates for action values then we can benefit from our greedy choices.

# Effect of optimal initial values
#  encourages the agent to visit all actions multiple times, resulting in early improvement in estimated action values.

from __future__ import print_function, division
from builtins import range
# Note: you may need to update your version of future
# sudo pip install -U future


import matplotlib.pyplot as plt
import numpy as np


NUM_TRIALS = 10000
EPS = 0.1
BANDIT_PROBABILITIES = [0.2, 0.5, 0.75]


class Bandit:
  def __init__(self, p):
    # p: the win rate
    self.p = p
    self.p_estimate = 5# TODO
    self.N = 1 # TODO if this is set to 0 then self.p_estimate in line 43 will be x

  def pull(self):
    # draw a 1 with probability p
    return np.random.random() < self.p

  def update(self, x):
    # TODO
    self.N += 1 
    self.p_estimate = ((self.N - 1)*self.p_estimate + x)/self.N # TODO


def experiment():
  bandits = [Bandit(p) for p in BANDIT_PROBABILITIES]

  rewards = np.zeros(NUM_TRIALS)
  for i in range(NUM_TRIALS):
    # use optimistic initial values to select the next bandit
    j = np.argmax([b.p_estimate for b in bandits]) # TODO

    # pull the arm for the bandit with the largest sample
    x = bandits[j].pull()

    # update rewards log
    rewards[i] = x

    # update the distribution for the bandit whose arm we just pulled
    bandits[j].update(x)


  # print mean estimates for each bandit
  for b in bandits:
    print("mean estimate:", b.p_estimate)

  # print total reward
  print("total reward earned:", rewards.sum())
  print("overall win rate:", rewards.sum() / NUM_TRIALS)
  print("num times selected each bandit:", [b.N for b in bandits])

  # plot the results
  cumulative_rewards = np.cumsum(rewards)
  win_rates = cumulative_rewards / (np.arange(NUM_TRIALS) + 1)
  plt.ylim([0, 1])
  plt.plot(win_rates)
  plt.plot(np.ones(NUM_TRIALS)*np.max(BANDIT_PROBABILITIES))
  plt.show()

if __name__ == "__main__":
  experiment()


# result 
# mean estimate: 0.7 <> 0.25
# mean estimate: 0.7333333333333333 <> 0.5
# mean estimate: 0.7451393064742425
# total reward earned: 7438.0
# overall win rate: 0.7438
# num times selected each bandit: [10, 15, 9978]
# algorithm didn't update when it explored 0.75 Bandit (always chooses it). 