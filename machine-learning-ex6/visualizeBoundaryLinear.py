import matplotlib.pyplot as plt
import numpy as np
from plotData import plot_data


def visualize_boundary_linear(X, y, model):
    """plots a linear decision boundary
       learned by the SVM and overlays the data on it
       """

    w = model.coef_.flatten()
    b = model.intercept_.flatten()
    xp = np.linspace(min(X[:, 0]), max(X[:, 0]), 100)
    yp = -(w[0] * xp + b) / w[1]
    plot_data(X, y)
    plt.plot(xp, yp, '-b')
