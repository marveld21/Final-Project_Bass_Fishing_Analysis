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
fish_df = df.drop(['Angler_Name','Species','Weight','Recorded_Time','Tournament_Day','Weight_Group','Recorded_Time_24','Recorded_Time_hour'],axis=1)
# attempt model using Bait to predict Weight Group
fish_df.columns

#simplify bait column ----binning
bait_count = fish_df.Bait.value_counts()
bait_count

bait_count.plot.density()

replace_bait = list(bait_count[bait_count<10].index)

# Replace in dataframe
for app in replace_bait:
    fish_df.Bait = fish_df.Bait.replace(app,"Other")
    
# Check to make sure binning was successful
fish_df.Bait.value_counts()

#simplify Cover column ----binning
fish_df.nunique()

cover_count = fish_df.Cover.value_counts()
cover_count

cover_count.plot.density()

replace_cover = list(cover_count[cover_count<7].index)

# Replace in dataframe
for app in replace_cover:
    fish_df.Cover = fish_df.Cover.replace(app,"Other")
    
# Check to make sure binning was successful
fish_df.Cover.value_counts()


fish_df.nunique()

#encode categorical variables
# Generate our categorical variable lists
fish_cat = fish_df.dtypes[fish_df.dtypes == "object"].index.tolist()
fish_cat

# Create a OneHotEncoder instance
enc = OneHotEncoder(sparse=False)

# Fit and transform the OneHotEncoder using the categorical variable list
encode_df = pd.DataFrame(enc.fit_transform(fish_df[fish_cat]))

# Add the encoded variable names to the dataframe
encode_df.columns = enc.get_feature_names(fish_cat)
encode_df


# Merge one-hot encoded features and drop the originals
fish_df= fish_df.merge(encode_df,left_index=True,right_index=True)
fish_df = fish_df.drop(columns = fish_cat)
fish_df['Weight-lbs']


#all of the data is catagorical

# Split our preprocessed data into our features and target arrays
y = fish_df['Weight-lbs']
X = fish_df.drop(columns="Weight-lbs")

# Split the preprocessed data into a training and testing dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)


# Create a StandardScaler instances
scaler = StandardScaler()

# Fit the StandardScaler
X_scaler = scaler.fit(X_train)

# Scale the data
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)


#### logistical regression



























# #keras deep learning
# #Define the model - deep neural net, i.e., the number of input features and hidden nodes for each layer.

# number_input_features = len(X_train_scaled[0])


# nn = tf.keras.models.Sequential()

# # First hidden layer
# nn.add(tf.keras.layers.Dense(units=100, activation="relu", input_dim = number_input_features))

# # Second hidden layer
# nn.add(tf.keras.layers.Dense(units=60, activation="relu"))

# # third hidden layer
# nn.add(tf.keras.layers.Dense(units=30, activation="relu"))

# # Output layer
# nn.add(tf.keras.layers.Dense(units=1, activation="relu"))

# # Check the structure of the model
# nn.summary()


# # Compile the model
# nn.compile(loss="binary_crossentropy", optimizer="adam", metrics=["accuracy"])


# # Train the model
# fit_model = nn.fit(X_train_scaled, y_train, epochs=100)


# # Evaluate the model using the test data
# model_loss, model_accuracy = nn.evaluate(X_test_scaled,y_test,verbose=2)
# print(f"Loss: {model_loss}, Accuracy: {model_accuracy}")




# #randomforest
# # Create a random forest classifier.
# rf_model = RandomForestClassifier(n_estimators=128, random_state=78)

# # Fitting the model
# rf_model = rf_model.fit(X_train_scaled, y_train)

# # Evaluate the model
# y_pred = rf_model.predict(X_test_scaled)
# print(f" Random forest predictive accuracy: {accuracy_score(y_test,y_pred):.3f}")