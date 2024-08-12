# plot_step_data

import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import numpy as np

# plot the cumulative steps each person has walked in the month by day
def plot_cumulative(df_cumulative):
    # set the figure size
    plt.figure(figsize=(14, 10.5))

    cmap = plt.get_cmap('jet')
    colors = cmap(np.linspace(0, 1, len(df_cumulative.columns)))

    # Plot each person's steps
    for ii, person in enumerate(df_cumulative.columns):
        plt.plot(df_cumulative.index, df_cumulative[person], label=person, marker='o', color=colors[ii])
        last_valid_index = np.argwhere(~np.isnan(df_cumulative[person])).flatten()[-1]
        x_last = df_cumulative.index[last_valid_index]
        y_last = int(df_cumulative[person][last_valid_index])
        plt.annotate(f'{person}: {y_last}',
                    xy=(x_last, y_last), xytext=(x_last, y_last + 10),
                    horizontalalignment='right', verticalalignment='bottom')

    # Add labels and title
    plt.xlabel('Date')
    plt.ylabel('Cumulative Steps')
    plt.title('Cumulative Steps by Person')

    # Format how the dates along the x-axis appear
    ax = plt.gca()
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%a %m/%d'))  # e.g., "Mon 01/01"
    plt.xticks(rotation=45)

    # More formatting
    plt.grid(axis='y', color='lightgray', linestyle='-', linewidth=0.7)
    plt.ylim(bottom = 0)

    # Add legend
    plt.legend()

    # show the plot
    plt.tight_layout()
    plt.show()
