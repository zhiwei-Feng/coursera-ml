import numpy as np
import matplotlib.pyplot as plt

# ================ Part 1: Feature Normalization ================
import featureNormalize
import gradientDescentMulti
import normlEqn

print('Loading data ...')

# Load Data
data = np.loadtxt('ex1data2.txt', delimiter=',')
X = data[:, :2]
y = data[:, 2]
m = y.size

# Print out some data points
print('First 10 examples from the dataset:')
for i in range(10):
    print('x = {}, y = {}'.format(X[i], y[i]))

input('Program paused. Press enter to continue.\n')

# Scale features and set them to zero mean
print('Normalizing Features ...')

(X, mu, sigma) = featureNormalize.feature_normalize(X)

# Add intercept term to X
X = np.c_[np.ones(m), X]

# ================ Part 2: Gradient Descent ================

# ====================== YOUR CODE HERE ======================
# Instructions: We have provided you with the following starter
#               code that runs gradient descent with a particular
#               learning rate (alpha). 
#
#               Your task is to first make sure that your functions - 
#               computeCost and gradientDescent already work with 
#               this starter code and support multiple variables.
#
#               After that, try running gradient descent with 
#               different values of alpha and see which one gives
#               you the best result.
#
#               Finally, you should complete the code at the end
#               to predict the price of a 1650 sq-ft, 3 br house.
#
# Hint: By using the 'hold on' command, you can plot multiple
#       graphs on the same figure.
#
# Hint: At prediction, make sure you do the same feature normalization.
#

print('Running gradient descent ...')

# Choose some alpha value
alpha = 0.03
num_iters = 400

# Init Theta and Run Gradient Descent
theta = np.zeros(3)
(theta, J_history) = gradientDescentMulti.gradient_descent_multi(X, y, theta, alpha, num_iters)

# Plot the convergence graph
plt.plot(np.arange(J_history.size), J_history)
plt.xlabel('Number of iterations')
plt.ylabel('Cost J')
plt.show()

# Display gradient descent's result
print('Theta computed from gradient descent : \n{}'.format(theta))

# Estimate the price of a 1650 sq-ft, 3 br house
# ====================== YOUR CODE HERE ======================
# Recall that the first column of X is all-ones. Thus, it does
# not need to be normalized.
predict = np.array([1650, 3])
predict = (predict - mu) / sigma
predict = np.r_[1, predict]
price = np.sum(predict * theta)  # You should change this

# ==========================================================
print('Predicted price of a 1650 sq-ft, 3 br house (using gradient descent) : {:0.3f}'.format(price))
input('Program paused. Press ENTER to continue')

# ================ Part 3: Normal Equations ================

# ====================== YOUR CODE HERE ======================
# Instructions: The following code computes the closed form 
#               solution for linear regression using the normal
#               equations. You should complete the code in 
#               normalEqn.m
#
#               After doing so, you should complete this code 
#               to predict the price of a 1650 sq-ft, 3 br house.
#
# Load data
data = np.loadtxt('ex1data2.txt', delimiter=',')
X = data[:, :2]
y = data[:, 2]
m = y.size

# Add intercept term to X
X = np.c_[np.ones(m), X]

# Calculate the parameters from the normal equation
theta = normlEqn.norml_eqn(X, y)
# Display normal equation's result
print('Theta computed from the normal equations : \n{}'.format(theta))

# Estimate the price of a 1650 sq-ft, 3 br house
# ===================== Your Code Here =====================
predict = np.array([1, 1650, 3])
price = np.sum(predict * theta)

# ==========================================================

print('Predicted price of a 1650 sq-ft, 3 br house (using normal equations) : {:0.3f}'.format(price))
input('ex1_multi Finished. Press ENTER to exit')
