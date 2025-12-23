import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Plotting aesthetics
plt.rcParams.update({
    'grid.alpha': 0.1, 'xtick.direction': 'in', 'ytick.direction': 'in',
    'axes.grid': True, 'figure.figsize': [9.0, 3.5], 'lines.linewidth': 1.0
})

def plot_figure_s2(csv_path="data/figure_s2_history.csv"):
    df = pd.read_csv(csv_path)
    colors = plt.cm.tab10(np.arange(0, 4))
    
    for T in sorted(df['temp_K'].unique()):
        fig, (ax1, ax2) = plt.subplots(1, 2)
        t_df = df[df['temp_K'] == T]

        for i, x in enumerate([10, 15, 20, 25]):
            # Subset for energy (Full length)
            e_data = t_df[(t_df['x_nom'] == x) & (t_df['type'] == 'energy')].sort_values('step')
            ax1.plot(e_data['step']/1000, e_data['value'], color=colors[i], label=f"{x}%")
            
            # Subset for xsolute (Length = energies / 200)
            x_data = t_df[(t_df['x_nom'] == x) & (t_df['type'] == 'xsolute')].sort_values('step')
            ax2.plot(x_data['step']/1000, x_data['value'], color=colors[i])
            
            # Add mean line for concentration
            ax2.axhline(y=x_data['value'].mean(), color=colors[i], linestyle='--', alpha=0.4)

        ax1.set_ylabel("Energy (eV/atom)")
        ax1.set_xlabel(r"SGC-MC Step ($\times 10^3$)")
        ax1.set_ylim(5.10, 5.25)
        ax1.set_title(f"Total Energy ({T} K)")
        ax1.legend(fontsize='x-small', ncol=2)

        ax2.set_ylabel("Solute Concentration (at.%)")
        ax2.set_xlabel(r"SGC-MC Step ($\times 10^3$)")
        ax2.set_ylim(5, 35)
        ax2.set_title(f"Chemical Equilibrium ({T} K)")

        plt.tight_layout()
        plt.savefig(f"plots/s2_convergence_{T}K.pdf", dpi=350, transparent=True)
        plt.close()

if __name__ == "__main__":
    plot_figure_s2()