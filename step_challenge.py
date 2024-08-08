# step_challenge.py

import process_step_data
import plot_step_data
import sys

# Get the filename, either the default one or use the command-line arguement if provided
if len(sys.argv) > 1:
    filename = sys.argv[1]
else:
    # default filename
    filename = 'step_challenge_data.csv'
print('Processing step data from: ' + filename)

df_raw, df_cumulative = process_step_data.process(filename)

plot_step_data.plot_cumulative(df_cumulative)
