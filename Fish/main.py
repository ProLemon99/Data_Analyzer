#-----Modules-----#
import pandas as pd
import matplotlib.pyplot as plt
import os
import json
import msvcrt
import sys
from pathlib import Path

#----Global Variables----#
quit = False
fish_data_df = pd.DataFrame()  
top_10_countries = pd.Series()  
USER_DB_FILE = 'Fish/user_credentials.json'

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
def userOptions(current_user):
    while True:
        print(f"""
    Fish Data Analysis (Logged in as: {current_user})

    Please select an option:
    1 - Show the original dataset
    2 - Show the updated Data Frame
    3 - Visualize the Tonnes of Seafood Caught by Country
    4 - Average Harvest
    5 - Top 10 Seafood Harvest
    6 - Isolate Country (total harvest)
    7 - Isolate Country (yearly harvest)
    8 - Account Settings
    9 - Log Out
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
                if account_settings_menu(current_user):
                    return True  # Return to main menu if account was deleted
            elif choice == 9:
                print("\nSuccessfully logged out.")
                return True  # Return to main menu
            else:
                print('Please enter a number between 1 and 9.')
        except ValueError:
            print('Invalid input. Please enter a number.')

#----User Authentication Functions----#
def load_user_db():
    """Load user credentials from JSON file"""
    if not Path(USER_DB_FILE).exists():
        return {}
    try:
        with open(USER_DB_FILE, 'r') as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading user database: {e}")
        return {}

def save_user_db(user_db):
    """Save user credentials to JSON file"""
    try:
        with open(USER_DB_FILE, 'w') as f:
            json.dump(user_db, f, indent=4)
        return True
    except Exception as e:
        print(f"Error saving user database: {e}")
        return False

# Add this new function for password input with asterisks
def get_password_with_asterisks(prompt="Password: "):
    print(prompt, end='', flush=True)
    password = []
    while True:
        ch = msvcrt.getch()
        if ch == b'\r':  # Enter key
            print()
            break
        elif ch == b'\x08':  # Backspace
            if password:
                password.pop()
                sys.stdout.write('\b \b')  # Erase the asterisk
                sys.stdout.flush()
        else:
            password.append(ch.decode('utf-8'))
            sys.stdout.write('*')
            sys.stdout.flush()
    return ''.join(password)

# Then modify the register_user function:
def register_user():
    """Register a new user account"""
    print("\n--- Account Registration ---")
    print("Password requirements:")
    print("- At least 8 characters")
    print("- No spaces")
    user_db = load_user_db()
    
    while True:
        username = input("Choose a username: ").strip()
        if not username:
            print("Username cannot be empty!")
            continue
        if ' ' in username:
            print("Username cannot contain spaces!")
            continue
        if username in user_db:
            print("Username already exists!")
            continue
        break
    
    while True:
        print("\nEnter password (will show * as you type):")
        password = get_password_with_asterisks()
        
        if not password:
            print("Password cannot be empty!")
            continue
        if ' ' in password:
            print("Password cannot contain spaces!")
            continue
        if len(password) < 8:
            print("Password must be at least 8 characters!")
            continue
            
        print("\nConfirm password:")
        password_confirm = get_password_with_asterisks()
        
        if password != password_confirm:
            print("\nPasswords don't match!")
            continue
        break
    
    user_db[username] = password
    if save_user_db(user_db):
        print("\nRegistration successful! You can now login.")
    else:
        print("\nRegistration failed. Please try again.")

def delete_account(username):
    """Delete a user account"""
    user_db = load_user_db()
    if username in user_db:
        confirm = input(f"Are you sure you want to delete {username}'s account? (y/n): ").lower()
        if confirm == 'y':
            del user_db[username]
            if save_user_db(user_db):
                print("Account deleted successfully.")
                return True
    print("Account deletion failed or cancelled.")
    return False

#----Main Menu Functions----#
def account_settings_menu(current_user):
    while True:
        print("\nAccount Settings:")
        print("1. Delete my account")
        print("2. Return to Fish Data Analysis")
        choice = input("Select option: ")
        
        if choice == '1':
            if delete_account(current_user):
                return True  # Return to main menu after deletion
        elif choice == '2':
            return False  # Return to fish data menu
        else:
            print("Invalid choice")

def main_menu():
    """Main program interface"""
    while True:
        print("\n--- Fish Data Analysis ---")
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        choice = input("Select option: ")
        
        if choice == '1':
            current_user = authenticate_user()
            if current_user:
                load_data()  # Only load data after successful login
                userOptions(current_user)  # Enter the options menu
        elif choice == '2':
            register_user()
        elif choice == '3':
            print("Goodbye!")
            sys.exit(0)  # Actually exit the program
        else:
            print("Invalid choice")

# And modify the authenticate_user function:
def authenticate_user():
    """Authenticate existing user"""
    print("\n--- Login ---")
    user_db = load_user_db()
    
    username = input("Username: ").strip()
    print("Password (will show * as you type):")
    password = get_password_with_asterisks()
    
    if username in user_db and user_db[username] == password:
        print(f"\nLogin successful! Welcome {username}!")
        return username
    print("\nInvalid username or password.")
    return None

#----Main program----#
if __name__ == "__main__":
    # Create user DB file if it doesn't exist
    if not Path(USER_DB_FILE).exists():
        save_user_db({})
    
    main_menu()  # Start with the main menu