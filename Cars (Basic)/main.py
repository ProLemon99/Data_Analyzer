# Modules
import pandas as pd
import matplotlib.pyplot as plt
import sys

# -- Variables --

# Quit
quit = False

# Conversion to AUD rate
conversion_rate = 100000 * 0.018

# -- Dataframe Setup --

# Setting up the original dataframe 
original = pd.read_csv('data/cardata.csv')

# Setting up the new dataframe and its organised version
new = pd.read_csv('data/cardata.csv', on_bad_lines='warn')
new = new.drop(columns=['Owner'], axis=1)
new.head()

# -- Additional Functions --

# Every year's average
def yearavg():
    avgperyear = new.groupby('Year')['Selling_Price'].mean()
    plt.bar(avgperyear.index, avgperyear.values, color='blue')
    plt.title('Average Selling Price per Year')
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('Average Selling Price')
    plt.xticks(avgperyear.index, rotation=45)
    plt.show()

# Average selling price
def avg_new():
    average_new = new['Selling_Price'].mean()
    average_new_aud = conversion_rate * average_new
    print(average_new_aud)
# AVerage currrent price
def avg_new_present():
    average_new_present = new['Present_Price'].mean()
    average_new_present_aud = conversion_rate * average_new_present
    print(average_new_present_aud)

# -- Functions --

# Checking the most and least expensive car in the list
def most_least_expensive():
    most_expensive_sell = new.loc[new['Selling_Price'].idxmax()]
    least_expensive_sell = new.loc[new['Selling_Price'].idxmin()]
    most_expensive_present = new.loc[new['Present_Price'].idxmax()]
    least_expensive_present = new.loc[new['Present_Price'].idxmin()]
    print('Most expensive car for its selling price:')
    print(most_expensive_sell['Car_Name'])
    print('Most expensive car for its present price:')
    print(most_expensive_present['Car_Name'])
    print('Least expensive car for its selling price:')
    print(least_expensive_sell['Car_Name'])
    print('Least expensive car for its present price:')
    print(least_expensive_present['Car_Name'])

# Calculating if there are more automatic or manual cars
def frequent_transmission():
    transmmission_count_print = new['Transmission'].value_counts()
    print("Here are the quantities of manual and automatic cars in the dataset:")
    print(transmmission_count_print)

# Showing the original dataframe
def ShowOriginal():
    print(original)

# Showing the updated dataframe
def ShowNew():
    print(new)

# Showing the kilometres driven by the cars
def sellingpriceevo():
    new.plot(
        kind = 'scatter',
        x = 'Year',
        y = 'Selling_Price',
        color = 'blue',

        alpha = 0.3,
        title = 'Selling prices over the years'
    )
    plt.show()

def presentpriceevo():
    new.plot(
        kind = 'scatter',
        x = 'Year',
        y = 'Present_Price',
        color = 'green',
        alpha = 0.3,
        title = 'Present prices over the years'
    )
    plt.show()

def transmission_presentprice():
    new.plot(
        kind = 'scatter',
        x = 'Transmission',
        y = 'Present_Price',
        color = 'red',
        alpha = 0.3,
        title = 'Relationship between transmission and selling price'
    )
    plt.show()

# The user interface 
def UI():
    try:
        main_options = True
        more_optionz = False
        vis_options = False

        while True: # The variables and IF statements that keep track of which options to show
            if main_options:
                Options()
            elif more_optionz:
                more_options()
            else:
                vis_optionz()
            if main_options: # The main options
                try:
                    option = int(input('Enter your selection: '))
                    if option == 1:
                        ShowOriginal()
                    elif option == 2:
                        ShowNew()
                    elif option == 3:
                        main_options = False
                        more_optionz = True
                    elif option == 4:
                        new.info()
                    elif option == 5:
                        print('Thanks for using this program! Goodbye!')
                        return
                    else:
                        print("Please select a valid choice.")
                except:
                    print("Please enter an option in the appropiate format.")
            elif more_optionz: # The analysis options 
                try:
                    option = int(input('Enter your selection: '))
                    if option == 1:
                        avg_new()
                    elif option ==  2:
                        avg_new_present()
                    elif option == 3:
                        frequent_transmission()
                    elif option == 4:
                        most_least_expensive()
                    elif option == 5:
                        vis_options = True
                        more_optionz = False
                    elif option == 6:
                        main_options = True
                    else:
                        print('Please select a valid choice')
                except:
                        print("Please enter an option in the appropiate format.")
            else: #Visualisation options
                try:
                    option = int(input('Enter your selection: '))
                    if option == 1:
                        sellingpriceevo()
                    elif option ==2:
                        presentpriceevo()
                    elif option == 3:
                        transmission_presentprice()
                    elif option == 4:
                        yearavg()
                    elif option == 5:
                        more_optionz = True
                        vis_options = False
                    else:
                        print('Please select a valid choice')
                except:
                        print("Please enter an option in the appropiate format.")

    except:
        print('Error')
        sys.exit()

# Read README.md
print('\nIf you are unsure about this program in any way, please take a look at the README file attached! Thank you')

# Main Options
def Options():
    print("""To analyse the dataset of Cars, please select one of the options below: 
          
          1 - Show the original dataset
          2 - Show the new and updated dataset
          3 - View more analysis options
          4 - View the general info of the dataset
          5 - Quit
          """)

# More options for analysis
def more_options():
    print("""To analyse additional information on the dataset of Cars, please select one of the options below: 
          
          1 - Show the average selling price (in AUD)
          2 - Show the average present price (in AUD)
          3 - Show whether there are more automatic or manual cars in the dataset
          4 - Show the least and most expensive car in the list
          5 - Visualisation options
          6 - Go back
          """)
    
# Visualisation Options
def vis_optionz():
    print("""To view visualisations on the dataset of Cars, please select one of the options below: 
          
          1 - Visualise the selling price over the years (scatter graph)
          2 - Visualise the present price over the years (scatter graph)
          3 - Visualise the relationship between transmission and present price (scatter graph)
          4 - Visualise the yearly average selling price (bar graph)
          5 - Go back
          """)
    
# Running the UI
UI()