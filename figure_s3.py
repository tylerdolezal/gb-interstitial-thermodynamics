import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

# --- Styling ---
plt.rcParams.update({
    'grid.alpha': 0.1, 'xtick.direction': 'in', 'ytick.direction': 'in',
    'axes.grid': True, 'axes.axisbelow': True,
    'figure.figsize': [4.5, 3.5]
})

def plot_figure_s3(csv_path="data/figure_s3_delta_mu_fit.csv"):
    df = pd.read_csv(csv_path)
    
    plt.figure()
    
    # 1:1 Identity line
    min_val, max_val = df['delta_mu_actual'].min(), df['delta_mu_actual'].max()
    plt.plot([min_val - 0.05, max_val + 0.05], [min_val - 0.05, max_val + 0.05], 
             color='k', linewidth=0.5, alpha=0.5, label='1:1 Ideal Fit')
    
    # Actual vs Predicted scatter
    plt.scatter(df['delta_mu_pred'], df['delta_mu_actual'], 
                s=40, edgecolor='k', alpha=0.7, color='tab:blue')

    # Formatting
    plt.xlabel('Predicted $\Delta\mu$ (eV)')
    plt.ylabel('Actual $\Delta\mu$ (eV)')
    
    plt.xlim(0.4, 1.0)
    plt.ylim(0.4, 1.0)
    plt.xticks(np.arange(0.4, 1.1, 0.1))
    plt.xticks(np.arange(0.4, 1.0, 0.02), minor=True)
    plt.yticks(np.arange(0.4, 1.1, 0.1))
    plt.yticks(np.arange(0.4, 1.0, 0.02), minor=True)
    
    plt.tight_layout()
    plt.savefig("plots/figure_s3_delta_mu_validation.pdf", dpi=350, transparent=True)
    plt.close()
    print("Generated Figure S3 validation plot.")

if __name__ == "__main__":
    plot_figure_s3()