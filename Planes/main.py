import pandas as pd
import matplotlib.pyplot as plt

# Read the .csv file
airplane_delays_df = pd.read_csv('Planes/data/full_data_flightdelay.csv', on_bad_lines='warn')

airplane_delays_df = airplane_delays_df.drop(columns=['DISTANCE_GROUP',
                                                      'SEGMENT_NUMBER',
                                                      'CONCURRENT_FLIGHTS',
                                                      'NUMBER_OF_SEATS',
                                                      'AIRPORT_FLIGHTS_MONTH',
                                                      'AIRLINE_FLIGHTS_MONTH',
                                                      'AIRLINE_AIRPORT_FLIGHTS_MONTH',
                                                      'AVG_MONTHLY_PASS_AIRPORT',
                                                      'AVG_MONTHLY_PASS_AIRLINE',
                                                      'FLT_ATTENDANTS_PER_PASS',
                                                      'GROUND_SERV_PER_PASS',
                                                      'LATITUDE',
                                                      'LONGITUDE',
                                                      'PREVIOUS_AIRPORT',
                                                      'SNWD'])

# Add new columns based off other ones
airplane_delays_df["PRCP_MM"] = airplane_delays_df["PRCP"] * 25.4
airplane_delays_df["SNOW_CM"] = airplane_delays_df["PRCP"] * 2.54
airplane_delays_df["TMAX_CELSIUS"] = (airplane_delays_df["TMAX"] - 32) * 5/9

# Only show the flight delays
airplane_delays_df = airplane_delays_df[airplane_delays_df['DEP_DEL15'] == 1]

#Change the 'MONTH' category to string and change the values
airplane_delays_df['MONTH'] = airplane_delays_df['MONTH'].astype(str)
airplane_delays_df = airplane_delays_df.replace(to_replace="1", value="January")
airplane_delays_df = airplane_delays_df.replace(to_replace="2", value="February")
airplane_delays_df = airplane_delays_df.replace(to_replace="3", value="March")
airplane_delays_df = airplane_delays_df.replace(to_replace="4", value="April")
airplane_delays_df = airplane_delays_df.replace(to_replace="5", value="May")
airplane_delays_df = airplane_delays_df.replace(to_replace="6", value="June")
airplane_delays_df = airplane_delays_df.replace(to_replace="7", value="July")
airplane_delays_df = airplane_delays_df.replace(to_replace="8", value="August")
airplane_delays_df = airplane_delays_df.replace(to_replace="9", value="September")
airplane_delays_df = airplane_delays_df.replace(to_replace="10", value="October")
airplane_delays_df = airplane_delays_df.replace(to_replace="11", value="November")
airplane_delays_df = airplane_delays_df.replace(to_replace="12", value="December")

# Change the 'DAY_OF_WEEK' category to string and change the values
airplane_delays_df["DAY_OF_WEEK"] = airplane_delays_df["DAY_OF_WEEK"].astype(str)
airplane_delays_df = airplane_delays_df.replace(to_replace="1", value="Monday")
airplane_delays_df = airplane_delays_df.replace(to_replace="2", value="Tuesday")
airplane_delays_df = airplane_delays_df.replace(to_replace="3", value="Wednesday")
airplane_delays_df = airplane_delays_df.replace(to_replace="4", value="Thursday")
airplane_delays_df = airplane_delays_df.replace(to_replace="5", value="Friday")
airplane_delays_df = airplane_delays_df.replace(to_replace="6", value="Saturday")
airplane_delays_df = airplane_delays_df.replace(to_replace="7", value="Sunday")


# Print it out
print(airplane_delays_df)

# Make the cleaned dataframe into a .csv file
airplane_delays_df.to_csv('airplane_delays.csv', index=False)
