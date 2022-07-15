import random 
import numpy as np
import matplotlib.pyplot as plt
## Coin function
def coin_filp():
    
    return random.randint(0,1) # Generate 01 random number
## Monte Carlo Simulation

prob_list1 = [] # An empty list stores probability values

def monte_carlo(n):
    """
    n Is the number of simulations
    """
    results = 0
    for i in range(n):
        flip_result = coin_filp()
        results =results + flip_result
        
        # Calculating probability value
        prob_value = results/(i+1)
        
        # append the probability values to the list
        prob_list1.append(prob_value)
        
        # plot the results
        plt.axhline(y = 0.5,color = 'red',linestyle='-')
        plt.xlabel('Iterations')
        plt.ylabel('Probability')
        plt.plot(prob_list1)
    
    return results/n
        
# calling the function

answer = monte_carlo(5000)
print('Final value:',answer)
plt.show()