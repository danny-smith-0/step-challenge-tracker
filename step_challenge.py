# step_challenge.py

# generic imports
import sys
import matplotlib.pyplot as plt

# local imports
import process_step_data
import plot_step_data

# Get the filename, either the default one or use the command-line arguement if provided
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    # default filename
    filename = 'data/step_challenge_data.csv'
print('Processing step data from: ' + filename)

df_raw, df_cumulative = process_step_data.process(filename)

plot_step_data.plot_cumulative(df_cumulative)
plot_step_data.plot_daily_steps(df_raw, figure_number=2)
plt.show()
