import pandas as pd
pd.options.display.max_columns = None
fish_df = pd.read_csv("scrape_test_fishing_data.csv")
fish_df2 = pd.read_csv("scrape_test_fishing_data_day_2.csv")

combo_fish_df = fish_df.append(fish_df2)
print(combo_fish_df.head)

combo_fish_df["Weight-lbs"] = round(combo_fish_df["Weight"].str[:1].astype(str).astype(int) + (combo_fish_df["Weight"].str[4:6].astype(str).astype(int)/16),2)
combo_fish_df["Weight-lbs"]

combo_fish_df.loc[combo_fish_df['Weight-lbs'] >= 2, 'Weight_Group'] = "2-2.5lbs"
combo_fish_df.loc[combo_fish_df['Weight-lbs'] >= 2.5, 'Weight_Group'] = "2.5-3lbs"
combo_fish_df.loc[combo_fish_df['Weight-lbs'] >= 3, 'Weight_Group'] = "3-3.5lbs"
combo_fish_df.loc[combo_fish_df['Weight-lbs'] >= 3.5, 'Weight_Group'] = "3.5-4lbs"
combo_fish_df.loc[combo_fish_df['Weight-lbs'] >= 4, 'Weight_Group'] = "4-4.5lbs"
combo_fish_df.loc[combo_fish_df['Weight-lbs'] >= 4.5, 'Weight_Group'] = "4.5-5lbs"
combo_fish_df.loc[combo_fish_df['Weight-lbs'] >= 5, 'Weight_Group'] = "5-5.5lbs"
combo_fish_df.loc[combo_fish_df['Weight-lbs'] >= 5.5, 'Weight_Group'] = "5.5+lbs"

combo_fish_df['Recorded_Time_24'] = pd.to_datetime(combo_fish_df['Recorded_Time'], format='%I:%M %p').dt.strftime('%H:%M')
combo_fish_df['Recorded_Time_24']
combo_fish_df['Recorded_Time_hour'] = round(combo_fish_df["Recorded_Time_24"].str[:2].astype(str).astype(int) + (combo_fish_df["Recorded_Time_24"].str[3:5].astype(str).astype(int)/60),2)
combo_fish_df['Recorded_Time_hour']

combo_fish_df.loc[combo_fish_df['Recorded_Time_hour'] >= 8, 'Time_Group'] = "Early Morning"
combo_fish_df.loc[combo_fish_df['Recorded_Time_hour'] >= 10, 'Time_Group'] = "Late Morning"
combo_fish_df.loc[combo_fish_df['Recorded_Time_hour'] >= 12, 'Time_Group'] = "Early Afternoon"
combo_fish_df.loc[combo_fish_df['Recorded_Time_hour'] >= 14, 'Time_Group'] = "Late Afternoon"

combo_fish_df
combo_fish_df.to_csv('combo_fish_data.csv', index=False)
print('saved')

combo_fish_df.nunique()



