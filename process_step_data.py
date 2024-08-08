import pandas as pd
from datetime import datetime

def process(step_challenge_data_filename):

    # load in the data into a data frame
    df_raw = pd.read_csv(step_challenge_data_filename)

    # remove the last row because it contains totals, not raw data
    df_raw = df_raw[:-1]

    # convert the date strings into datetime objects
    df_raw['Date'] = pd.to_datetime(df_raw['Date'])
    df_raw['Date'].dt.strftime('%m/%d/%Y')

    # add a row of zeros at the beginning
    people = df_raw.columns.to_list()[1:] # skip the column named 'Date'
    row_of_zeros = pd.DataFrame(
        {
            'Date': (df_raw['Date'][0] - pd.DateOffset(days=1)).to_pydatetime(),
            **{person: [0] for person in people}
        }
    )
    df_raw = pd.concat([row_of_zeros, df_raw], ignore_index=True)

    # remove all rows where the data is for today or later
    now = datetime.today()
    today = now.replace(hour=0, minute=0, second=0, microsecond=0)
    # print(today)
    df_raw = df_raw[df_raw['Date'] < today]
    print(df_raw)

    # Calculate the cumulative sum for each person (column) across the dates
    df_cumulative = df_raw.set_index('Date').cumsum()
    print(df_cumulative)

    return df_raw, df_cumulative
