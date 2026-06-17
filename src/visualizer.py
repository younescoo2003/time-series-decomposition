import matplotlib.pyplot as plt
import seaborn as sns


def plot_decomposition(data, result, title='Time Series Decomposition'):
    """
    Plot original + 3 components
    
    """
    fig, axes = plt.subplots(4, 1, figsize=(12, 10))
    
    axes[0].plot(data, label='Original')
    axes[0].set_title('Original')
    axes[0].legend()
    
    axes[1].plot(result.trend, label='Trend', color='green')
    axes[1].set_title('Trend')
    axes[1].legend()
    
    axes[2].plot(result.seasonal, label='Seasonal', color='orange')
    axes[2].set_title('Seasonality')
    axes[2].legend()
    
    axes[3].plot(result.resid, label='Residual', color='red')
    axes[3].set_title('Residual')
    axes[3].legend()
    
    plt.tight_layout()
    return fig

def plot_seasonal_pattern(result, title='Seasonal Pattern'):
    """
    Plot seasonal subplots
    
    """
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(result.seasonal[:12], marker='*')
    ax.set_title(title)
    return fig