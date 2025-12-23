import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

# --- Styling ---
plt.rcParams.update({
    'grid.alpha': 0.1, 'axes.grid': True, 'figure.figsize': [4.0, 3.5],
    'xtick.direction': 'out', 'ytick.direction': 'in', 'lines.linewidth': 1.0
})

def plot_sro_ridges(csv_path="data/figure_3_sro_curves.csv"):
    df = pd.read_csv(csv_path)
    offset = 1.2
    
    # We will generate one plot per System/GB/Temp combination
    for (system, gb, T), group in df.groupby(['system', 'gb_type', 'temp']):
        if T != 300: continue # Focus on 300K for main text
        
        fig, ax = plt.subplots()
        x_concentrations = sorted(group['x_cr'].unique())
        colors = plt.cm.tab10(np.arange(0, len(x_concentrations)))
        
        for i, x in enumerate(x_concentrations):
            data = group[group['x_cr'] == x]
            y_offset = i * offset
            
            ax.fill_between(data['sro'], y_offset, y_offset + data['density_scaled'], 
                            color=colors[i], alpha=0.8, edgecolor='k', linewidth=0.5)
            ax.plot(data['sro'], y_offset + data['density_scaled'], color='k')

        ax.set_title(f"{system.capitalize()} {gb} at {T}K")
        ax.set_xlabel("Local Warren-Cowley SRO")
        ax.set_ylabel("Nominal Cr (at.%)")
        ax.set_yticks([i * offset for i in range(len(x_concentrations))])
        ax.set_yticklabels(x_concentrations)
        ax.set_xlim(-3.5, 1.5)
        ax.axvline(0, color='black', linestyle='--', alpha=0.5)
        
        plt.savefig(f"plots/fig3_sro_ridge_{system}_{gb}_{T}K.pdf", bbox_inches='tight', transparent=True)
        plt.close()

if __name__ == "__main__":
    plot_sro_ridges()