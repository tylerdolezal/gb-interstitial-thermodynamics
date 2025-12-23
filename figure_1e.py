import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

plt.rcParams.update({
    'grid.alpha': 0.1, 'grid.linewidth': 0.15, 'grid.color': 'black',
    'xtick.direction': 'in', 'ytick.direction': 'in',
    'axes.grid': True, 'axes.axisbelow': True,
    'figure.figsize': [3.5, 2.5], 'lines.linewidth': 1.0
})

def plot_manuscript_figure_1e(csv_path="data/figure_1e_thermodynamics.csv"):
    df = pd.read_csv(csv_path)
    
    # Define combinations to plot
    systems = df['interstitial'].unique()
    gb_types = df['gb_type'].unique()
    temps = sorted(df['temperature_K'].unique())
    colors = plt.cm.tab10(np.arange(0, len(temps)))

    for system in systems:
        for gb in gb_types:
            subset = df[(df['interstitial'] == system) & (df['gb_type'] == gb)]
            
            # 1. Plot Grand Potential Excess (Omega)
            fig, ax = plt.subplots()
            for i, T in enumerate(temps):
                t_data = subset[subset['temperature_K'] == T]
                ax.errorbar(t_data['global_x_cr'], t_data['omega_jm2_mean'], 
                             yerr=t_data['omega_jm2_std'], label=f"{T} K",
                             marker='o', capsize=3, color=colors[i])
            
            ax.set_xlabel("Bulk Cr Concentration (at.%)")
            ax.set_ylabel(r"Grand Potential Excess $\tilde{\Omega}_{ex}$ (J/m²)")
            ax.axhline(0, color='black', linestyle='--', alpha=0.5)
            plt.ylim(-4.25, 0.5)
            plt.yticks(np.arange(-4, 0.5, 0.25),minor=True)
            plt.savefig(f"plots/fig1e_omega_{system}_{gb}.pdf", bbox_inches='tight', transparent=True)
            plt.close()

            # 2a. Plot Interfacial Excess (Gamma_Cr)
            fig, ax = plt.subplots()
            for i, T in enumerate(temps):
                t_data = subset[subset['temperature_K'] == T]
                # Plotting Gamma for Cr as the primary example
                ax.errorbar(t_data['global_x_cr'], t_data['gamma_cr_mean'], 
                             yerr=t_data['gamma_cr_std'], label=f"{T} K",
                             marker='s', capsize=3, color=colors[i])
                
            ax.set_xlabel("Bulk Cr Concentration (at.%)")
            ax.set_ylabel(r"Interfacial Excess $\Gamma_{Cr}$ (at/Å²)")
            plt.ylim(-0.15, 0.28)
            plt.yticks(np.arange(-0.15, 0.26, 0.025), minor=True)
            plt.savefig(f"plots/fig1e_gamma_{system}_Cr_{gb}.pdf", bbox_inches='tight', transparent=True)
            plt.close()

            # 2b. Plot Interfacial Excess (Gamma_B/C)
            fig, ax = plt.subplots()
            for i, T in enumerate(temps):
                t_data = subset[subset['temperature_K'] == T]
                # Plotting Gamma for Cr as the primary example
                ax.errorbar(t_data['global_x_cr'], t_data['gamma_interstitial_mean'], 
                             yerr=t_data['gamma_interstitial_std'], label=f"{T} K",
                             marker='s', capsize=3, color=colors[i])
                
            ax.set_xlabel("Bulk Cr Concentration (at.%)")
            ax.set_ylabel(fr"Interfacial Excess $\Gamma_{{{system}}}$ (at/Å²)")
            plt.ylim(-0.15, 0.28)
            plt.yticks(np.arange(-0.15, 0.26, 0.025), minor=True)
            plt.savefig(f"plots/fig1e_gamma_{system}_{gb}.pdf", bbox_inches='tight', transparent=True)
            plt.close()

            # 3. Plot GB Width
            fig, ax = plt.subplots()
            for i, T in enumerate(temps):
                t_data = subset[subset['temperature_K'] == T]
                ax.errorbar(t_data['global_x_cr'], t_data['width_A_mean'], 
                             yerr=t_data['width_A_std'], label=f"{T} K",
                             marker='^', capsize=3, color=colors[i])
                
            ax.set_xlabel("Bulk Cr Concentration (at.%)")
            ax.set_ylabel(r"GB Width ($\AA$)")
            plt.ylim(2.8, 11)
            plt.yticks(np.arange(4, 11, 1.0))
            plt.yticks(np.arange(3, 11, 0.25), minor=True)
            plt.savefig(f"plots/fig1e_width_{system}_{gb}.pdf", bbox_inches='tight', transparent=True)
            plt.close()

if __name__ == "__main__":
    plot_manuscript_figure_1e()