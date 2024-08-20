import pandas as pd
import matplotlib.pyplot as plt

# -- Variables --
quit = False

#---- Dataframe Setup ----#
original = pd.read_csv('Datasets/data/highest_hollywood_grossing_movies.csv')

hollywood_movies = pd.read_csv('Datasets/data/highest_hollywood_grossing_movies.csv',
                            header=None,
                            names=['Title', 'Year', 'Distributors', 'Budget', 'Worldwide Sales', 'Genres', 'Running Time'])

# Data Cleaning
hollywood_movies

print(hollywood_movies)

# Calculations
hollywood_movies.mean

#---- Function Definitions ----#
def showOriginalData():
    print(original)

def showUpdatedData():
    print(hollywood_movies)

# Visualizing the data with Matplotlib

def showCharts():
    hollywood_movies.plot(
                    kind='scatter',
                    x='Title',
                    y='Worldwide Sales',
                    color='blue',
                    alpha=0.3,
                    title='Worldwide Sales of Movies in USD')
    plt.show()

# Data Analysis

average_sales = hollywood_movies['Worldwide Sales'].mean()
print(average_sales)

# The User Interface

def UI():
    global quit

    print("""Welcome to the Dataset Visualization!
          
    Please select an option:
    1 - Show the original dataset
    2 - Show the updated Data Frame
    3 - Visualise the worldwide sales of movies in USD
    4 - Quit Program
        """)
    
    try:
        choice = int(input('Enter Selection: '))

        if choice == 1:
            showOriginalData()
        elif choice == 2:
            showUpdatedData()
        elif choice == 3:
            showCharts()
        elif choice == 4:
            quit = True
        else:
            print('Not a valid number')

    except:
        print('Type a number')

#----Main program----#
while not quit:
    UI()