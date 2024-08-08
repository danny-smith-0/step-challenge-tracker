# plot_step_data

import matplotlib.pyplot as plt
import matplotlib.dates as mdates

# plot the cumulative steps each person has walked in the month by day
def plot_cumulative(df_cumulative):
    # set the figure size
    plt.figure(figsize=(10, 6))

    # Plot each person's steps
    for person in df_cumulative.columns:
        plt.plot(df_cumulative.index, df_cumulative[person], label=person, marker='o')

    # Add labels and title
    plt.xlabel('Date')
    plt.ylabel('Cumulative Steps')
    plt.title('Cumulative Steps by Person')

    # Format how the dates along the x-axis appear
    ax = plt.gca()
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%a %m/%d'))  # e.g., "Mon 01/01"
    plt.xticks(rotation=45)

    # Add legend
    plt.legend()

    # show the plot
    plt.tight_layout()
    plt.show()
