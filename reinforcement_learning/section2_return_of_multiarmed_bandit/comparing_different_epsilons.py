import numpy as np 
import matplotlib.pyplot as plt 

NUM_TRIAL = 100000
EPS = 0.1
BANDIT_PROBABILITIES = [0.2, 0.5, 0.75]

class Bandit:
    def __init__(self, p):
        self.p = p 
        self.p_estimate = 0.
        self.N = 0 
    
    def pull(self):
        return np.random.randn() + self.p
    
    def update(self, x):
        self.N += 1
        self.p_estimate = ((self.N - 1)*self.p_estimate + x)/self.N 


def experiment(m1, m2, m3, eps, N):
    bandits = [Bandit(p) for p in BANDIT_PROBABILITIES]
    bandits = [Bandit(m1), Bandit(m2), Bandit(m3)]

    means = np.array([m1, m2, m3])
    true_best = np.argmax(means)
    count_suboptimal = 0 
    rewards = np.zeros(N)

    num_times_explored = 0 
    num_times_exploited = 0 
    num_optimal = 0 
    optimal_j = np.argmax([b.p for b in bandits])
    print('optimal j:', optimal_j)

    for i in range(N):
        if np.random.random() < eps:
            num_times_explored += 1
            j = np.random.randint(len(bandits))
        else:
            num_times_exploited += 1 
            j = np.argmax([b.p_estimate for b in bandits])

        if j != true_best:
            count_suboptimal += 1 

        if j == true_best:
            num_optimal += 1 
        
        x = bandits[j].pull()

        rewards[i] = x

        bandits[j].update(x)

    for b in bandits:
        print('mean estimate:', b.p_estimate)
    
    print('total reward earned', rewards.sum())
    print('overall winrate', rewards.sum()/NUM_TRIAL)
    print('num time explored', num_times_explored)
    print('num time exploited', num_times_exploited)
    print('num time selected optimal bandit:', num_optimal)

    cumulative_rewards = np.cumsum(rewards)
    win_rates = cumulative_rewards / (np.arange(N) + 1)
    plt.plot(win_rates)
    plt.plot(np.ones(N) * m1)
    plt.plot(np.ones(N) * m2)
    plt.plot(np.ones(N) * m3)
    plt.xscale('log')
    plt.plot(np.ones(N) * np.max(means))
    plt.show()

    return win_rates

if __name__ == '__main__':
    m1, m2, m3 = 1.5, 2.5, 3.5
    c1 = experiment(m1, m2, m3, 0.1, NUM_TRIAL)
    c2 = experiment(m1, m2, m3, 0.01, NUM_TRIAL)
    c3 = experiment(m1, m2, m3, 0.05, NUM_TRIAL)

    plt.plot(c1, label='eps=0.1')
    plt.plot(c2, label='eps=0.01')
    plt.plot(c3, label='eps=0.05')
    plt.legend()
    plt.show()

'''
big eps makes reward converge faster at the begining but still makes terrible in the future
small eps makes reward converge slowly
--> have to find optimal eps
''' 