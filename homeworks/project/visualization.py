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


def plot_loss(history, title: str = None, figsize=(8, 5)):
    """
    Plots training and validation loss from a Keras History object.

    Parameters:
    -----------
    history : keras.callbacks.History
        The History object returned by model.fit().
    figsize : tuple
        Size of the plot.
    """

    if title is None: 
        title = 'Model Loss Over Epochs'

    plt.figure(figsize=figsize)
    
    # Plot training loss
    plt.plot(history.history['loss'], label='Training Loss', color='blue')

    # Plot validation loss if available
    if 'val_loss' in history.history:
        plt.plot(history.history['val_loss'], label='Validation Loss', color='orange')

    plt.title(title)
    plt.xlabel('Epoch')
    plt.ylabel('Loss')
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
