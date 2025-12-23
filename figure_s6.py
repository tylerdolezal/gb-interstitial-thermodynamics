import pandas as pd
import matplotlib.pyplot as plt


plt.rcParams.update({
    'grid.alpha': 0.1, 'grid.linewidth': 0.15, 'grid.color': 'black',
    'xtick.direction': 'in', 'ytick.direction': 'in',
    'axes.grid': True, 'axes.axisbelow': True,
    'figure.figsize': [3.5, 2.5], 'lines.linewidth': 1.0
})

# Style Mappings
sys_colors = {'boron': 'tab:blue', 'carbon': 'tab:orange'}
gb_markers = {'S5': 'o', 'HM': 's'}
gb_styles = {'S5': '-', 'HM': '--'}

def plot_supplemental_s6(csv_path="data/figure_2_spectral_summary.csv"):
    df = pd.read_csv(csv_path)
    
    metrics = {
        'mean_eseg': r'Weighted Average $E_{seg}$ (eV)',
        'iqr': r'Spectral Width / IQR (eV)',
        'strong_site_fraction': 'Fraction of Sites Under -2 eV',
    }

    for col, label in metrics.items():
        fig, ax = plt.subplots()
        
        # Group by system and GB type
        for (system, gb_type), group in df.groupby(['system', 'gb_type']):
            # Ensure data is sorted by concentration for clean lines
            group = group.sort_values('x_cr')
            
            ax.plot(
                group['x_cr'], 
                group[col], 
                color=sys_colors[system.lower()],
                linestyle=gb_styles.get(gb_type, '-'),
                marker=gb_markers.get(gb_type, 'o'),
                markersize=4,
                label=f"{system.capitalize()} {gb_type}"
            )
        
        ax.set_xlabel("Global Cr Concentration (at.%)")
        ax.set_ylabel(label)
        ax.set_xticks([10, 15, 20, 25])
        
        # Add zero-line for energy metrics
        if col == 'mean_eseg':
            ax.axhline(0, color='black', linestyle='--', linewidth=0.8, alpha=0.5)
            ax.set_ylim(df[col].min() - 0.2, max(0.2, df[col].max() + 0.2))
        
        if col == 'strong_site_fraction':
            ax.set_ylim(-0.05, 1.05)

        # Legend configuration (optional: can be moved to a master legend)
        # ax.legend(fontsize='small', frameon=False)

        plt.savefig(f"plots/s6_trend_{col}.pdf", dpi=350, bbox_inches="tight", transparent=True)
        plt.close()
        print(f"Generated S6 plot for {col}")

if __name__ == "__main__":
    plot_supplemental_s6()