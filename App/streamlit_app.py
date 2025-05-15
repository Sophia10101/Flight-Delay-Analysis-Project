import streamlit as st
import joblib 
import pandas as pd

# dataset
df = pd.read_csv("/Users/sophiashull/Desktop/DS personal projects/Flight-Delay-Analysis-Project/Data/processed/cleaned_delay_data_1yr.csv")
# model
model = joblib.load("/Users/sophiashull/Desktop/DS personal projects/Flight-Delay-Analysis-Project/Data/processed/flight_delays_model")
model_columns = joblib.load("/Users/sophiashull/Desktop/DS personal projects/Flight-Delay-Analysis-Project/Data/processed/model_columns.pkl")



st.title("US Airlines Flight Delay Probability Predictor")
airline= st.selectbox("Please select your airline", (sorted(df["carrier_name"].unique())))
airport=st.selectbox("Please select the departing airport", (sorted(df["airport"].unique())))
month_map = {
    "January": 1,
    "February": 2,
    "March": 3,
    "April": 4,
    "May": 5,
    "June": 6,
    "July": 7,
    "August": 8,
    "September": 9,
    "October": 10,
    "November": 11,
    "December": 12
}
month=st.selectbox("Please select the month of departure", (list(month_map.keys())))
month = month_map[month]
year=st.selectbox("Please select the year", (sorted(df["year"].unique())))

specific_df= df[
  (df["carrier_name"]==airline)&
  (df["airport"]==airport)&
  (df["month"]==month)
]
if st.button("Predict Delay Probability"):
    if specific_df.empty:
        st.error("No matching data found for this airline, airport, and month combination. Please try different values.")
    else:
      specific_df["yr_diff"]=(specific_df["year"]-year).abs()

      specific_df=specific_df.copy()
      best_row = specific_df.loc[specific_df["yr_diff"].idxmin()]
      carrier_ct_val = best_row["carrier_ct"]
      arr_del15_val = best_row["arr_del15"]
      arr_flights_val=best_row["arr_flights"]

      data = {"carrier_name": [airline],
              "airport":[airport],
              "month":[month],
              'year':[year],
              "carrier_ct":[carrier_ct_val],
              "arr_del15":[arr_del15_val],
              "arr_flights":[arr_flights_val]
      }
      user_df=pd.DataFrame(data)
      user_data_encoded = pd.get_dummies(user_df)
      user_data_encoded = user_data_encoded.reindex(columns=model_columns, fill_value=0)
      prediction = model.predict(user_data_encoded)[0]

      probability = prediction
      st.write(f"This flight has an approximate delay probability of {probability:.1f}%")
      if probability < 20:
          st.write("Low risk")
      elif probability < 40:
          st.write("Medium risk")
      else:
          st.write("High risk")



