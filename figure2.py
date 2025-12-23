import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# --- Styling ---
plt.rcParams.update({
    'grid.alpha': 0.1, 'axes.grid': True, 'figure.figsize': [4.0, 3.5],
    'xtick.direction': 'out', 'ytick.direction': 'in'
})

def plot_ridge_plots(csv_path="data/figure_2_kde_curves.csv"):
    df = pd.read_csv(csv_path)
    offset = 1.2
    
    for (system, gb), group in df.groupby(['system', 'gb_type']):
        fig, ax = plt.subplots()
        x_concentrations = sorted(group['x_cr'].unique())
        colors = plt.cm.tab10(np.arange(0, len(x_concentrations)))
        
        for i, x in enumerate(x_concentrations):
            data = group[group['x_cr'] == x]
            y_offset = i * offset
            
            # Recreate the Ridge Plot
            ax.fill_between(data['energy'], y_offset, y_offset + data['density_scaled'], 
                            color=colors[i], alpha=0.8, edgecolor='k', linewidth=0.5)
            ax.plot(data['energy'], y_offset + data['density_scaled'], color='k', lw=1)

        # Formatting
        ax.set_title(f"{system.capitalize()} - {gb}")
        ax.set_xlabel(r"Segregation Energy $E_{seg}$ (eV)")
        ax.set_ylabel("Bulk Cr Concentration (at.%)")
        ax.set_yticks([i * offset for i in range(len(x_concentrations))])
        ax.set_yticklabels(x_concentrations)
        ax.set_xlim(-3.5, 0.5)
        ax.axvline(0, color='black', linestyle='--', alpha=0.5)
        
        plt.savefig(f"plots/fig2_ridge_{system}_{gb}.pdf", bbox_inches='tight', transparent=True)
        plt.close()

if __name__ == "__main__":
    plot_ridge_plots()