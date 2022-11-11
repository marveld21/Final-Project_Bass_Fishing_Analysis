# model 0.2.1 is attempting to improve accuracy above 0.581


import pandas as pd
import psycopg2
from sqlalchemy import create_engine
import io
from configparser import ConfigParser
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler,OneHotEncoder
import tensorflow as tf
from sklearn.ensemble import RandomForestClassifier
pd.options.display.max_columns = None



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

df = pd.read_sql_query('select * from "Cleaned_Fish_Data"',con=engine)
df.tail()


df.nunique()
#drop not needed columns
fish_df = df.drop(['Angler_Name','Species','Weight','Recorded_Time','Tournament_Day','Weight_Group','Recorded_Time_24','Recorded_Time_hour','Weight-lbs'],axis=1)
# attempt model using Bait to predict Weight Group
fish_df.columns



# #simplify bait column ----binning # removing for 0.2.1
# bait_count = fish_df.Bait.value_counts()
# bait_count

# bait_count.plot.density()

# replace_bait = list(bait_count[bait_count<10].index)

# # Replace in dataframe
# for app in replace_bait:
#     fish_df.Bait = fish_df.Bait.replace(app,"Other")
    
# # Check to make sure binning was successful
# fish_df.Bait.value_counts()

# #simplify Cover column ----binning # removing for 0.2.1
# fish_df.nunique()

# cover_count = fish_df.Cover.value_counts()
# cover_count

# cover_count.plot.density()

# replace_cover = list(cover_count[cover_count<7].index)

# # Replace in dataframe
# for app in replace_cover:
#     fish_df.Cover = fish_df.Cover.replace(app,"Other")
    
# # Check to make sure binning was successful
# fish_df.Cover.value_counts()


fish_df.nunique()


#split target and features
fish_df_features = fish_df.drop(['Fish_Size'],axis=1)
fish_df_target = fish_df['Fish_Size']
fish_df_target
fish_df_features


#encode categorical variables
# Generate our categorical variable lists
fish_cat = fish_df_features.dtypes[fish_df_features.dtypes == "object"].index.tolist()
fish_cat


fish_df_features[fish_cat]

# Create a OneHotEncoder instance
enc = OneHotEncoder(sparse=False)

# Fit and transform the OneHotEncoder using the categorical variable list
encode_df = pd.DataFrame(enc.fit_transform(fish_df_features[fish_cat]))

# Add the encoded variable names to the dataframe
encode_df.columns = enc.get_feature_names(fish_cat)
encode_df



#simple encode for target
target_encode_df = fish_df_target.replace(('Big Fish', 'Small Fish'), (1, 0))
target_encode_df.head()









# Merge one-hot encoded features and drop the originals
# fish_df= fish_df.merge(encode_df,left_index=True,right_index=True)
# fish_df = fish_df.drop(columns = fish_cat)
# fish_df['Fish_Size']


#all of the data is catagorical

# Split our preprocessed data into our features and target arrays
y = target_encode_df
X = encode_df

# Split the preprocessed data into a training and testing dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)


# Create a StandardScaler instances
scaler = StandardScaler()

# Fit the StandardScaler
X_scaler = scaler.fit(X_train)

# Scale the data
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)


X_train_scaled.shape
y_train.shape

#### logistical regression

from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(solver='lbfgs',
                                max_iter=200,
                                random_state=1)

classifier.fit(X_train, y_train)


y_pred = classifier.predict(X_test)
results = pd.DataFrame({"Prediction": y_pred, "Actual": y_test}).reset_index(drop=True)
results.head(20)


from sklearn.metrics import accuracy_score
print(accuracy_score(y_test, y_pred))

#trying feature importance

feature_importance = classifier.coef_
xf = feature_importance.size
feature_importance = feature_importance.reshape(xf,1)

FI_df = pd.DataFrame(feature_importance,columns=['FI'])
FI_df

headers = list(encode_df)
headers

FI_df['Feature'] = headers
Feature_Importance_df = FI_df.iloc[:,[1,0]]
Feature_Importance_df.sort_values(by=['FI'], ascending=False)
#need to save as csv for dashboard