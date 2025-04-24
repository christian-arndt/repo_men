import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np


def plot_predicted_vs_true(y_pred, y_test, figsize=(6, 6)):

    # Create the figure and axis
    f, ax = plt.subplots(1, 1, figsize=figsize)

    # Scatter plot of true vs predicted values
    ax.scatter(y_test, y_pred, color="maroon", s=2, label="Predictions")

    # Get limits for the diagonal reference line
    min_val = min(np.min(y_test), np.min(y_pred))
    max_val = max(np.max(y_test), np.max(y_pred))

    # Plot the black dashed diagonal line
    ax.plot([min_val, max_val], [min_val, max_val], 'k--', linewidth=1, label="Ideal Fit")

    # Set labels
    ax.set_xlabel("Target variable")
    ax.set_ylabel("Model Prediction")

    # Remove top and right spines
    sns.despine(ax=ax)

    # Add legend
    ax.legend()

    return f