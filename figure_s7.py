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
    'lines.linewidth': 1.0
})

# Style Mappings
sys_colors = {'boron': 'tab:blue', 'carbon': 'tab:orange'}
gb_markers = {'S5': 'o', 'HM': 's'}
gb_styles = {'S5': '-', 'HM': '--'}

def plot_supplemental_s7(csv_path="data/figure_3_sro_summary.csv"):
    df = pd.read_csv(csv_path)
    
    # Define metrics
    metrics = {
        'mean_sro': 'Weighted Average SRO',
        'iqr_sro': 'Spectral Width / IQR',
        'strong_order_fraction': r'Fraction of Sites with $\alpha \leq -1.0$',
    }

    target_temps = [300, 900]

    for col, label in metrics.items():
        # Create a 1x2 subplot layout [300K | 900K]
        fig, axes = plt.subplots(1, 2, figsize=(7.0, 2.5), sharey=True)
        
        for idx, T in enumerate(target_temps):
            ax = axes[idx]
            ax.set_title(f"{T} K", fontsize=10)
            
            # Filter for specific temperature
            t_df = df[df['temp'] == T]
            
            # Group by system and GB type
            for (system, gb_type), group in t_df.groupby(['system', 'gb_type']):
                group = group.sort_values('x_cr')
                
                ax.plot(
                    group['x_cr'], 
                    group[col], 
                    color=sys_colors[system.lower()],
                    linestyle=gb_styles.get(gb_type.upper(), '-'),
                    marker=gb_markers.get(gb_type.upper(), 'o'),
                    markersize=4,
                    label=f"{system.capitalize()} {gb_type}" if idx == 0 else ""
                )
            
            ax.set_xlabel("Bulk Cr (at.%)")
            ax.set_xticks([10, 15, 20, 25])
            
            if col == 'mean_sro':
                ax.axhline(0, color='black', linestyle='--', linewidth=0.8, alpha=0.5)
                # Ensure zero is visible in both plots
                ax.set_ylim(df[col].min() - 0.2, 1.25)
            
            if col == 'strong_order_fraction':
                ax.set_ylim(-0.05, 1.05)

        # Labels for the whole figure
        axes[0].set_ylabel(label)
        
        # Add legend to the first plot
        axes[0].legend(fontsize='x-small', frameon=False, loc='lower left')

        plt.tight_layout()
        plt.savefig(f"plots/s7_sro_{col}.pdf", dpi=350, bbox_inches="tight", transparent=True)
        plt.close()
        print(f"Generated S7 side-by-side plot for {col}")

if __name__ == "__main__":
    plot_supplemental_s7()