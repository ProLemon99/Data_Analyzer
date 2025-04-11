import pandas as pd
import matplotlib.pyplot as plt
import tkinter as tk

# ----------------------------------------------------- Optional Modules --------------------------------------------------------
import time
import random

# ----------------------------------------------------- Global Variables --------------------------------------------------------
run = True
auth_time = random.randint(0,1111)
original_df = pd.read_csv('Video Games/data/games-features.csv')

updated_df = original_df.loc[:,['index', 'QueryID', 'ResponseID', 'QueryName', 'ResponseName', 'ReleaseDate', 'ControllerSupport', 'PlatformWindows', 'PlatformLinux', 'PlatformMac', ]]
updated_df.to_csv('data/games-simple.csv')

Platform = ['PlatformMac', 'PlatformWindows', 'PlatformLinux', 'ControllerSupport']
No_Games = [4562,13355,3057,3658]
# --------------------------------------------------- Defining Functions --------------------------------------------------------

def showOG():
    print(original_df)

def showUpdated():
    print(updated_df)

def macGames():
    mac_updated_df = updated_df.loc[:, ['index', 'QueryName', 'ReleaseDate', 'PlatformMac']]
    mac_df = mac_updated_df[mac_updated_df['PlatformMac']==True]
    print(mac_df)

def windowsGames():
    win_updated_df = updated_df.loc[:, ['index', 'QueryName', 'ReleaseDate', 'PlatformWindows']]
    win_df = win_updated_df[win_updated_df['PlatformWindows']==True]
    print(win_df)

def linuxGames():
    linux_updated_df = updated_df.loc[:, ['index', 'QueryName', 'ReleaseDate', 'PlatformLinux']]
    linux_df = linux_updated_df[linux_updated_df['PlatformLinux']==True]
    print(linux_df)

def controllerGames():
    controller_games_support_df = updated_df.loc[:, ['index', 'ResponseName', 'ReleaseDate', 'ControllerSupport', 'PlatformWindows', 'PlatformLinux', 'PlatformMac']]
    controller_games_df = controller_games_support_df[controller_games_support_df['ControllerSupport']==True]
    print(controller_games_df)

def userAuthentication():
    print(f"Welcome User.\nThis is the most popular video games on different platforms. Below are the options of what you can do. Please note that these are only Steam Games and are may not include some newer titles.")

def platformComparison():
    Platform = ['PlatformMac', 'PlatformWindows', 'PlatformLinux', 'ControllerSupport']
    No_Games = [4562,13355,3057,3658]

    plt.bar(Platform, No_Games)
    plt.suptitle('Platform Comparison')
    plt.show()

def options():
    print("""[1] -> View the original dataframe
[2] -> View the dataframe with only the necessary information
[3] -> View the most popular macOS games
[4] -> View the most popular Windows games
[5] -> View the most popular Linux games
[6] -> View the games with controller support
[7] -> Compare the platform's number of games along with the number of games that support controller
[8] -> Exit the program""")
    print(" ")


def mainloop():
    try:
        userAuthentication()
        options()
        selection = int(input("PLEASE SELECT AN OPTION: "))

        if selection == 1:
            showOG()
        elif selection == 2:
            showUpdated()
        elif selection == 3:
            macGames()
        elif selection == 4:
            windowsGames()
        elif selection == 5:
            linuxGames()
        elif selection == 6:
            controllerGames()
        elif selection == 7:
            platformComparison()
        elif selection == 8:
            print("Goodbye, user! I will miss you! xo")
            quit()
        else:
            print("IT CAN'T BE THAT DIFFICULT TO ENTER A NUMBER BETWEEN 1 AND 6")

    except ValueError:
        print("IT'S OKAY, JUST ENTER A NUMBER")

# =============================================== Define the Main Program ==================================================

while run:
    mainloop()