import pandas as pd

input_df = pd.read_csv('/Users/michaelroberts/Desktop/DictCsv.csv')

out_dict = input_df.set_index('Column A')['Column B'].to_dict()

print out_dict['Thing']