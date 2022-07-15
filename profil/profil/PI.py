import turtle
import random
import matplotlib.pyplot as plt
import math
## Draw point
# to visualize the random points
mypen = turtle.Turtle()
mypen.hideturtle()
mypen.speed(0)

# drawing a square
mypen.up()
mypen.setposition(-100,-100)
mypen.down()
mypen.fd(200)
mypen.left(90)
mypen.fd(200)
mypen.left(90)
mypen.fd(200)
mypen.left(90)
mypen.fd(200)
mypen.left(90)

# drawing a circle
mypen.up()
mypen.setposition(0,-100)
mypen.down()
mypen.circle(100)
# Initialization data
# to count the points inside and outside the circle
in_circle = 0
out_circle = 0

# to store the values of the PI
pi_values = []
# Main function
# running for 5 times 
for i in range(5):
    for j in range(50):
        
        # generate random numbers 
        x = random.randrange(-100,100)
        y = random.randrange(-100,100)
        
        # check if the number lies outside the circle
        
        if (x**2+y**2>100**2):
            mypen.color('black')
            mypen.up()
            mypen.goto(x,y)
            mypen.down()
            mypen.dot()
            out_circle = out_circle + 1
        else:
            mypen.color('red')
            mypen.up()
            mypen.goto(x,y)
            mypen.down()
            mypen.dot()
            in_circle = in_circle + 1
            
        # calculating the value of PI
        pi = 4.0 * in_circle/(in_circle + out_circle)
        
        # append the values of PI in list
        pi_values.append(pi)
        
        # Calculating the errors
        avg_pi_errors = [abs(math.pi - pi) for pi in pi_values]
        
    # Print the final values of PI for each iterations
    print(pi_values[-1])

# Draw image
# Plot the PI values
plt.axhline(y=math.pi,color='g',linestyle='-')
plt.plot(pi_values)
plt.xlabel('Iterations')
plt.ylabel('Values of PI')
plt.show()


plt.axhline(y = 0.0,color = 'g',linestyle='-')
plt.plot(avg_pi_errors)
plt.xlabel('Iterations')
plt.ylabel('Error')
plt.show()
    