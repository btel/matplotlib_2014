"""
"""
import numpy as np
import matplotlib.pyplot as plt


cmaps = {'sequential': [('gray', 256),
                        ('Blues', 256),
                        ('hot', 256)],
         'diverging' : [('seismic', 256)],
         'cyclic' : [('hsv', 256)],
         'qualitative' : [('hsv', 6),
                          ('Set1', 6)]}


nrows =sum(map( len, cmaps.values()))+len(cmaps)

def plot_color_gradients(cmap_list):
    fig, axes = plt.subplots(nrows=nrows, figsize=(6, 2))
    fig.subplots_adjust(top=0.95, bottom=0.01, left=0.1, right=0.99)

    i = 0
    for k,v in cmap_list.items():
        ax = axes[i]
        ax.text(0.5,0.5, k, ha='center', va='center',
                transform=ax.transAxes)
        i+=1
        for name, levels in v: 
            ax = axes[i]
            gradient = np.linspace(0, 1, levels)
            gradient = np.vstack((gradient, gradient))
            ax.imshow(gradient, aspect='auto', cmap=plt.get_cmap(name), interpolation='nearest')
            pos = list(ax.get_position().bounds)
            x_text = pos[0] - 0.01
            y_text = pos[1] + pos[3]/2.
            fig.text(x_text, y_text, name, va='center', ha='right', fontsize=10)
            i+=1

    # Turn off *all* ticks & spines, not just the ones with colormaps.
    for ax in axes:
        ax.set_axis_off()

plot_color_gradients(cmaps)

plt.savefig('figures/colormaps_reference.svg', transparent=True)
