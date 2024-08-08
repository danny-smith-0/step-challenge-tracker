# step_challenge.py

import process_step_data
import plot_step_data

step_challenge_data_filename = 'step_challenge_data.csv'

df_raw, df_cumulative = process_step_data.process(step_challenge_data_filename)

plot_step_data.plot_cumulative(df_cumulative)
