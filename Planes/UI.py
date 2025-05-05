import pandas as pd
import matplotlib.pyplot as plt

quit = False
airplane_delays_df = pd.read_csv('Planes/data/full_data_flightdelay.csv')

# Functions
def show_most_delayed_month_mode():
    most_delayed_month_mode = airplane_delays_df['MONTH'].mode()
    print("The most delayed month of the year for airplane delays is " + most_delayed_month_mode.values[0] + ".")

def show_most_delayed_month_value():
    most_delayed_month_value = airplane_delays_df['MONTH'].value_counts()
    most_delayed_month_value.plot(kind='barh', x='Delays', y='Month', color='blue', alpha=0.3, title='Most Delayed Month', fontsize='8')
    plt.show()

def show_most_delayed_dayofweek_mode():
    most_delayed_dayofweek_mode = airplane_delays_df['DAY_OF_WEEK'].mode()
    print("The most delayed day of the week for airplane delays is " + most_delayed_dayofweek_mode.values[0] + ".")

def show_most_delayed_dayofweek_value():
    most_delayed_dayofweek_value = airplane_delays_df['DAY_OF_WEEK'].value_counts()
    most_delayed_dayofweek_value.plot(kind='barh', x='Delays', y='Day of week', color='blue', alpha=0.3, title='Most Delayed Day of the Week', fontsize='8',)
    plt.show()

def show_most_delayed_time_block_mode():
    most_delayed_time_block_mode = airplane_delays_df['DEP_TIME_BLK'].mode()
    print("The most delayed time block for airplane delays is " + most_delayed_time_block_mode.values[0] + ".")

def show_most_delayed_time_block_value():
    most_delayed_time_block_value = airplane_delays_df['DEP_TIME_BLK'].value_counts()
    most_delayed_time_block_value.plot(kind='barh', x='Delays', y='Time Block', color='blue', alpha=0.3, title='Most Delayed Time Block', fontsize='8')
    plt.show()

def show_most_delayed_airline_mode():
    most_delayed_airline_mode = airplane_delays_df['CARRIER_NAME'].mode()
    print("The most delayed airline for airplane delays is " + most_delayed_airline_mode.values[0] + ".")

def show_most_delayed_airline_value():
    most_delayed_airline_value = airplane_delays_df['CARRIER_NAME'].value_counts()
    most_delayed_airline_value.plot(kind='barh', x='Delays', y='Name of Airline', color='blue', alpha=0.3, title='Most Delayed Airlines', fontsize='8')
    plt.show()

def show_most_delayed_airport_mode():
    most_delayed_airport_mode = airplane_delays_df['DEPARTING_AIRPORT'].mode()
    print("The most delayed airport for airplane delays is " + most_delayed_airport_mode.values[0] + ".")

def show_most_delayed_airport_value():
    most_delayed_airport_value = airplane_delays_df['DEPARTING_AIRPORT'].value_counts().head(30)
    most_delayed_airport_value.plot(kind='barh', x='Delays', y='Name of Airport', color='blue', alpha=0.3, title='Most Delayed Airports', fontsize='5')
    plt.show()
    
def show_most_delayed_plane_age():
    most_plane_age = airplane_delays_df['PLANE_AGE'].median()
    print("The most delayed airport for airplane delays is " + str(most_plane_age))

def show_most_delayed_rain():
    most_delayed_PRCP = airplane_delays_df['PRCP'].median()
    print("The average amount of rain in inches for flight delays is " + str(most_delayed_PRCP) + " inches.")
    
def show_most_delayed_rain_mm():
    most_delayed_PRCP_MM = airplane_delays_df['PRCP_MM'].median()
    print("The average amount of rain in mm for flight delays is " + str(most_delayed_PRCP_MM) + "mm.")
    
def show_most_delayed_snow():
    most_delayed_SNOW = airplane_delays_df['SNOW'].median()
    print("The average amount of snow for flight delays is " + str(most_delayed_SNOW) + " inches.")
    
def show_most_delayed_snow_cm():
    most_delayed_SNOW_CM = airplane_delays_df['SNOW_CM'].median()
    print("The average amount of snow for flight delays is " + str(most_delayed_SNOW_CM) + "cm.")
    
def show_most_delayed_max_temp():
    most_delayed_TMAX = airplane_delays_df['TMAX'].median()
    print("The average highest temperature in fahrenheit for flight delays is " + str(most_delayed_TMAX) + "°F.")
    
def show_most_delayed_max_temp_celsius():
    most_delayed_TMAX_CELSIUS = airplane_delays_df['TMAX_CELSIUS'].median()
    print("The average highest temperature in celsius for flight delays is " + str(round(most_delayed_TMAX_CELSIUS, 2)) + "°C.")
 
def useroptions():
    global quit
    
    print("""Welcome to the home of flight delays. 
          
    Please select one of these options:
    1. View the whole dataset with delays
    2. See the most delayed month
    3. See the most delayed day of the week
    4. See the most delayed time block
    5. See the most delayed airplane company
    6. See the most delayed airport
    7. See the average plane age for flight delays
    8. See the weather for flight delays
    9. Quit program
    """)
    
    try:
        choice = int(input('Enter Selection: '))
        if choice == 1:
            print(airplane_delays_df)
        
        elif choice == 2:
            print("""Which of the following would you like to see?
                  
                  1. The most delayed month of the year
                  2. A chart with all the months of the year
                  3. Go back
                  """)
            
            try:
                choice = int(input('Enter Selection: '))
                if choice == 1:
                    show_most_delayed_month_mode()
                elif choice == 2:
                    show_most_delayed_month_value()
                elif choice == 3:
                    useroptions()
                else:
                    print("Enter a number between 1 and 3 please.")
            except:
                print("Are you okay or can you not choose a number?")
        elif choice == 3:
            print("""Which of the following would you like to see?
                  
                  1. The most delayed day of the week
                  2. A chart with all the days of the week
                  3. Go back
                  """)
            
            try:
                choice = int(input('Enter Selection: '))
                if choice == 1:
                    show_most_delayed_dayofweek_mode()
                elif choice == 2:
                    show_most_delayed_dayofweek_value()
                elif choice == 3:
                    useroptions()
                else:
                    print("Enter a number between 1 and 3 please.")
            except:
                print("Are you okay or can you not choose a number?")
        elif choice == 4:
            print("""Which of the following would you like to see?
                  
                  1. The most delayed time block
                  2. A chart with all the time blocks
                  3. Go back
                  """)
            
            try:
                choice = int(input('Enter Selection: '))
                if choice == 1:
                    show_most_delayed_time_block_mode()
                elif choice == 2:
                    show_most_delayed_time_block_value()
                elif choice == 3:
                    useroptions()
                else:
                    print("Enter a number between 1 and 3 please.")
            except:
                print("Are you okay or can you not choose a number?")
        elif choice == 5:
            print("""Which of the following would you like to see?
                  
                  1. The most delayed airline
                  2. A chart with all the airlines
                  3. Go back
                  """)
            
            try:
                choice = int(input('Enter Selection: '))
                if choice == 1:
                    show_most_delayed_airline_mode()
                elif choice == 2:
                    show_most_delayed_airline_value()
                elif choice == 3:
                    useroptions()
                else:
                    print("Enter a number between 1 and 3 please.")
            except:
                print("Are you okay or can you not choose a number?")
        elif choice == 6:
            print("""Which of the following would you like to see?
                  
                  1. The most delayed airport
                  2. A chart with 30 of the most delayed airports
                  3. Go back
                  """)
            
            try:
                choice = int(input('Enter Selection: '))
                if choice == 1:
                    show_most_delayed_airport_mode()
                elif choice == 2:
                    show_most_delayed_airport_value()
                elif choice == 3:
                    useroptions()
                else:
                    print("Enter a number between 1 and 3 please.")
            except:
                print("Are you okay or can you not choose a number?")
        elif choice == 7:
            show_most_delayed_plane_age()
        elif choice == 8:
            print("""Which of the following would you like to see?
                  
                  1. The inches of rain
                  2. The mm of rain
                  3. The inches of snow
                  4. The cm of snow
                  5. The maximum temperature in fahrenheit
                  6. The maximum temperature in celsius
                  7. Go back
                  """)
            
            try:
                choice = int(input('Enter Selection: '))
                if choice == 1:
                    show_most_delayed_rain()
                elif choice == 2:
                    show_most_delayed_rain_mm()
                elif choice == 3:
                    show_most_delayed_snow()
                elif choice == 4:
                    show_most_delayed_snow_cm()
                elif choice == 5:
                    show_most_delayed_max_temp()
                elif choice == 6:
                    show_most_delayed_max_temp_celsius()
                elif choice == 7:
                    useroptions()
                else:
                    print("Enter a number between 1 and 7 please.")
            except:
                print("Are you okay or can you not choose a number?")
        elif choice == 9:
            quit = True
        else:
            print("Enter a number between 1 and 8 please")
    except:
        print("Are you okay or can you not choose a number?")

while not quit:
    useroptions()