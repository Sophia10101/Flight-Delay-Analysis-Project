# Flight-Delay-Analysis-Project
Flying can be stressful, especially when unexpected delays disrupt travel plans. To better anticipate these disruptions this project analyzes over 24,000+ flight records from the U.S Department of Transportation. Built with python, pandas, sickit-learn, matplotlib, seaborn, and a streamlit UI for predictions. The features used for this model are the following:
1. carrier_name (airline name)
2. airport (A three character alpha-numeric code issued by the U.S. Department of Transportation  which is the official designation of the airport.)
3. Month
4. carrier_ct (Carrier Count for airline cause of delay)
5. arr_del15 (Arrival Delay Indicator, 15 Minutes or More Arrival delay equals the difference of the actual arrival time minus the scheduled arrival time. A flight is considered on-time when it arrives less than 15 minutes after its published arrival time.)
6. arr_flights (arrival flights)
7. year


Model Performance:
R²:  0.991406052852239
MSE: 1.0345017057649566
MAE: 0.33374704221440005
