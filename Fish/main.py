#-----Modules-----#
import pandas as pd
import matplotlib.pyplot as plt
import os

#----Global Variables----#
quit = False
fish_data_df = pd.DataFrame()  
top_10_countries = pd.Series()  

# Define credentials
USERNAME = 'Kelvin'
PASSWORD = 'Skibidi'

#----Setup dataframe----#
def load_data():
    global original_df, fish_data_df, top_10_countries
    
    try:
        # Use relative path with os.path.join for cross-platform compatibility
        file_path = os.path.join('Fish', 'data', 'Fish_data.csv')
        
        # Verify file exists before trying to read
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Data file not found at: {file_path}")
        
        # Read the data
        original_df = pd.read_csv(file_path)
        fish_data_df = pd.read_csv(
            file_path,
            header=None,
            names=['Entity', 'Code', 'Year', 'Fish and seafood']
        )
        
        # Clean the data
        fish_data_df = clean_data(fish_data_df)
        
        # Calculate top 10 seafood harvest countries
        country_totals = fish_data_df.groupby('Entity')['Fish and seafood'].sum()
        top_countries = country_totals.sort_values(ascending=False)
        top_10_countries = top_countries.head(10)
        
        # Save processed data
        save_processed_data()
        
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        exit(1)

def save_processed_data():
    """Save the processed data to a new CSV file"""
    try:
        # Create directory if it doesn't exist
        os.makedirs(os.path.join('Fish', 'data'), exist_ok=True)
        
        # Save the file
        output_path = os.path.join('Fish', 'data', 'new_fish_data.csv')
        fish_data_df.to_csv(output_path, index=False)
    except Exception as e:
        print(f"Error saving processed data: {str(e)}")

def clean_data(df):
    """Clean and prepare the data"""
    try:
        # Convert 'Fish and seafood' and 'Year' to numeric
        df['Fish and seafood'] = pd.to_numeric(df['Fish and seafood'], errors='coerce').fillna(0)
        df['Year'] = pd.to_numeric(df['Year'], errors='coerce').fillna(0)
        
        # Drop duplicate rows
        df.drop_duplicates(inplace=True)
        return df
    except Exception as e:
        print(f"Error cleaning data: {str(e)}")
        return df

#----Data Analysis Functions----#
def showOriginalData():
    print(original_df)

def avg_harvest():
    fish_data_df['Fish and seafood'] = pd.to_numeric(fish_data_df['Fish and seafood'], errors='coerce')
    average_harvest = fish_data_df['Fish and seafood'].mean()
    print(f"The average seafood harvest is {average_harvest:,.2f} tonnes")

def showUpdatedData():
    df = fish_data_df.copy()
    df = clean_data(df)
    print(df)
    print("\nMissing Values:")
    print(df.isnull().sum())

def showCharts():
    fish_data_df.plot(
        kind='scatter',
        x='Entity',
        y='Fish and seafood',
        color='blue',
        alpha=0.5,
        title='Tonnes of Seafood Caught by Country'
    )
    plt.tight_layout()  # Prevent label cutoff
    plt.show()

def isolate_country_data(df, country_name):
    """Isolate and analyze data for a specific country"""
    try:
        country_data = df[df['Entity'] == country_name]
        if country_data.empty:
            print(f"No data found for country: {country_name}")
            return 0, pd.DataFrame()
        
        total_harvest = country_data['Fish and seafood'].sum()
        yearly_data = country_data.groupby('Year')['Fish and seafood'].sum().reset_index()
        return total_harvest, yearly_data
    except Exception as e:
        print(f"Error processing country data: {str(e)}")
        return 0, pd.DataFrame()

#----User Interface Functions----#
def userOptions():
    global quit

    print("""
    Fish Data Analysis

    Please select an option:
    1 - Show the original dataset
    2 - Show the updated Data Frame
    3 - Visualize the Tonnes of Seafood Caught by Country
    4 - Average Harvest
    5 - Top 10 Seafood Harvest
    6 - Isolate Country (total harvest)
    7 - Isolate Country (yearly harvest)
    8 - Quit Program
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
            avg_harvest()
        elif choice == 5:
            print("\nTop 10 Seafood Harvest Countries:")
            print(top_10_countries)
        elif choice == 6:
            country_name = input('Enter the name of the country: ')
            total_harvest, _ = isolate_country_data(fish_data_df, country_name)
            print(f"Total Seafood Harvest for {country_name}: {total_harvest:,.2f} tonnes")
        elif choice == 7:
            country_name = input('Enter the name of the country: ')
            _, yearly_data = isolate_country_data(fish_data_df, country_name)
            if not yearly_data.empty:
                print(f"\nYearly Seafood Harvest Data for {country_name}:")
                print(yearly_data)
        elif choice == 8:
            print("Aight cya")
            quit = True
        else:
            print('Please enter a number between 1 and 8.')

    except ValueError:
        print('Invalid input. Please enter a number.')

def authenticate_user():
    """Authenticate user based on username and password."""
    print("Please login:")
    username = input("Username: ")
    password = input("Password: ")

    if username == USERNAME and password == PASSWORD:
        print("Login successful!")
        return True
    else:
        print("Invalid username or password.")
        return False

#----Main program----#
if __name__ == "__main__":
    if authenticate_user():
        load_data()  # Load and clean data before starting the main loop
        while not quit:
            userOptions()
    else:
        print("Access denied. Exiting program.")