import random
import matplotlib.pyplot as plt

# 1 = car
# 2 = goat
doors = ['goat','goat','car']

switch_win_probability = []
stick_win_probability = []

plt.axhline(y = 0.66666,color = 'r',linestyle='-')
plt.axhline(y = 0.33333,color = 'g',linestyle='-')
def monte_carlo(n):
    
    # calculating switch and stick wins:
    switch_wins = 0
    stick_wins = 0

    for i in range(n):
        # randomly placing the car and goats behind three doors
        random.shuffle(doors)

        # contestant's choice
        k = random.randrange(2)

        # If the contestant doesn't get car
        if doors[k] != 'car':
            switch_wins += 1
        else:
            stick_wins += 1

        # updatating the list values
        switch_win_probability.append(switch_wins/(i+1))
        stick_win_probability.append(stick_wins/(i+1))
        
        # plotting the data
        plt.plot(switch_win_probability)
        plt.plot(stick_win_probability)
        
    # print the probability values
    print('Winning probability if you always switch',switch_win_probability[-1])
    print('Winning probability if you always stick to your original choice:',stick_win_probability[-1])

monte_carlo(1000)
plt.axhline(y = 0.66666,color = 'r',linestyle='-')
plt.axhline(y = 0.33333,color = 'g',linestyle='-')
plt.show()