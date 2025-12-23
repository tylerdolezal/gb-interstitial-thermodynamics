import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib import font_manager

# --- Styling & Fonts ---
font_path = '/System/Library/Fonts/HelveticaNeue.ttc'
try:
    custom_font = font_manager.FontProperties(fname=font_path)
    plt.rcParams['font.family'] = custom_font.get_name()
except:
    pass 

plt.rcParams.update({
    'grid.alpha': 0.1, 'grid.linewidth': 0.15, 'grid.color': 'black',
    'xtick.direction': 'in', 'ytick.direction': 'in',
    'axes.grid': True, 'axes.axisbelow': True,
    'figure.figsize': [4.5, 5.0], 'lines.linewidth': 1.0
})

def plot_dual_convergence(csv_path="data/mc_convergence_data.csv"):
    df = pd.read_csv(csv_path)
    
    # Systems to process for S4 and S5
    for gb in ["s5", "hm"]:
        for interstitial in ["B", "C"]:
            subset = df[(df['gb_type'] == gb) & (df['interstitial'] == interstitial)]
            if subset.empty: continue

            # Create vertical stack: Top = Energy, Bottom = Composition
            fig, (ax1, ax2) = plt.subplots(2, 1, sharex=True)
            colors = plt.cm.tab10(np.arange(0, len(subset['x_cr_nominal'].unique())))
            x_concentrations = sorted(subset['x_cr_nominal'].unique())

            for i, x in enumerate(x_concentrations):
                data = subset[subset['x_cr_nominal'] == x].sort_values('step')
                steps_k = data['step'] / 1e3
                
                # 1. Plot Energy as a continuous line (recorded frequently)
                ax1.plot(steps_k, data['energy_keV'], 
                         color=colors[i], label=f"{x} at.% Cr", alpha=0.8)
                
                # 2. Plot GB Composition as markers (sampled every 100 steps)
                # Filter out NaNs to ensure clean plotting
                valid_mask = data['x_gb_cr'].notna()
                ax2.scatter(steps_k[valid_mask], data['x_gb_cr'][valid_mask], 
                            color=colors[i], s=10, marker='o', alpha=0.6)
                
                # Optional: Add a light line through markers to guide the eye
                ax2.plot(steps_k[valid_mask], data['x_gb_cr'][valid_mask], 
                         color=colors[i], linewidth=0.5, alpha=0.3)

            # --- Formatting ---
            ax1.set_ylabel("Total Potential Energy (keV)")
            ax2.set_ylabel(r"GB Cr Concentration $X_{GB}$ (at.%)")
            ax2.set_xlabel(r"SGC-MC Step ($\times 10^3$)")
            
            # Align Y-limits for energy based on data range
            ax1.set_ylim(subset['energy_keV'].min() - 0.5, subset['energy_keV'].max() + 0.5)
            # Composition is typically between 0 and 100%
            ax2.set_ylim(0, 100)
            
            ax1.legend(loc='upper right', fontsize='x-small', ncol=2, frameon=False)
            
            # Save based on manuscript figure numbering
            fig_label = "S4" if gb == "s5" else "S5"
            plt.tight_layout()
            plt.savefig(f"plots/figure_{fig_label}_{interstitial}_convergence.pdf", 
                        dpi=350, bbox_inches='tight', transparent=True)
            plt.close()
            print(f"Generated Figure {fig_label} for {interstitial}")

if __name__ == "__main__":
    plot_dual_convergence()