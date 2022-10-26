import pandas as pd
import psycopg2
from sqlalchemy import create_engine
from configparser import ConfigParser

#import db_pw from config
config_1 = ConfigParser()
config_1.read('config.ini')

db_password=config_1['db']['db_password']


#connect to postgresql
import pandas as pd
import psycopg2
from sqlalchemy import create_engine


db_string = f"postgresql://postgres:{db_password}@127.0.0.1:5432/Fish_Catch_Data"
print(db_string)
#create engine instance
engine = create_engine(db_string)

df = pd.read_sql_query('select * from "Scraped_Fish_Data"',con=engine)
df.tail()



#clean data
combo_fish_df = df

combo_fish_df["Weight-lbs"] = round(combo_fish_df["Weight"].str[:1].astype(str).astype(int) + (combo_fish_df["Weight"].str[4:6].astype(str).astype(int)/16),2)
combo_fish_df["Weight-lbs"]
#make weight groups
combo_fish_df.loc[combo_fish_df['Weight-lbs'] >= 2, 'Weight_Group'] = "2-2.5lbs"
combo_fish_df.loc[combo_fish_df['Weight-lbs'] >= 2.5, 'Weight_Group'] = "2.5-3lbs"
combo_fish_df.loc[combo_fish_df['Weight-lbs'] >= 3, 'Weight_Group'] = "3-3.5lbs"
combo_fish_df.loc[combo_fish_df['Weight-lbs'] >= 3.5, 'Weight_Group'] = "3.5-4lbs"
combo_fish_df.loc[combo_fish_df['Weight-lbs'] >= 4, 'Weight_Group'] = "4-4.5lbs"
combo_fish_df.loc[combo_fish_df['Weight-lbs'] >= 4.5, 'Weight_Group'] = "4.5-5lbs"
combo_fish_df.loc[combo_fish_df['Weight-lbs'] >= 5, 'Weight_Group'] = "5-5.5lbs"
combo_fish_df.loc[combo_fish_df['Weight-lbs'] >= 5.5, 'Weight_Group'] = "5.5+lbs"
#convert time to hours
combo_fish_df['Recorded_Time_24'] = pd.to_datetime(combo_fish_df['Recorded_Time'], format='%I:%M %p').dt.strftime('%H:%M')
combo_fish_df['Recorded_Time_24']
combo_fish_df['Recorded_Time_hour'] = round(combo_fish_df["Recorded_Time_24"].str[:2].astype(str).astype(int) + (combo_fish_df["Recorded_Time_24"].str[3:5].astype(str).astype(int)/60),2)
combo_fish_df['Recorded_Time_hour']
#group time slots
combo_fish_df.loc[combo_fish_df['Recorded_Time_hour'] >= 8, 'Time_Group'] = "Early Morning"
combo_fish_df.loc[combo_fish_df['Recorded_Time_hour'] >= 10, 'Time_Group'] = "Late Morning"
combo_fish_df.loc[combo_fish_df['Recorded_Time_hour'] >= 12, 'Time_Group'] = "Early Afternoon"
combo_fish_df.loc[combo_fish_df['Recorded_Time_hour'] >= 14, 'Time_Group'] = "Late Afternoon"
#save fish data to csv
combo_fish_df
combo_fish_df.to_csv('combo_fish_data.csv', index=False)
print('saved')
#bring back in fish data
combo_fish_df = pd.read_csv("combo_fish_data.csv")