import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk

# Load the data
df = pd.read_csv('Cars (Advanced)/data/Average_Model.csv')

# Calculate the average price for each make, take the columns from the original csv file (Reused from previous Documentation)
avg_price_by_make = df.groupby(['Make'])['Price'].mean().reset_index()
avg_price_by_make.columns = ['Make', 'Average_Price']

# Round to 2 decimal places (Reused)
avg_price_by_make['Average_Price'] = avg_price_by_make['Average_Price'].round(2)

# Calculate the price for each model, take the columns from the original csv file (Reused from previous documentation)
avg_price_by_model = df.groupby(['Model'])['Price'].mean().reset_index()
avg_price_by_model.columns = ['Model', 'Price']

# Round to 2 decimal places (Reused)
avg_price_by_model['Price'] = avg_price_by_model['Price'].round(2)

# Create the main window (Reused)
root = tk.Tk()
root.title("Average Prices GUI")
root.geometry("900x600")
root.config(bg="skyblue")

# Create a notebook widget
carsnotebook = ttk.Notebook(root)
carsnotebook.pack(fill='both', expand=True)

# Create frames for each tab
makeframe = ttk.Frame(carsnotebook)
modelframe = ttk.Frame(carsnotebook)
dataframe = ttk.Frame(carsnotebook)
helpframe = ttk.Frame(carsnotebook)

# Add frames to notebook
carsnotebook.add(makeframe, text='Make Prices')
carsnotebook.add(modelframe, text='Model Prices')
carsnotebook.add(dataframe, text='DataFrame')
carsnotebook.add(helpframe, text = 'Help')

# Inserting Pandas Dataframe into the GUI: First Convert to String, create a text widget and insert it into the widget. 
def data_make():
    df_string = df.to_string()
    text_widget = tk.Text(dataframe)
    text_widget.insert(tk.END, df_string)
    text_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Function to create the bar plot for Make (Reused from previous Documentation)
def plot_make():
# Create a figure and axes object to plot
    fig, ax = plt.subplots()
    avg_price_by_make.plot(
        kind='bar',
        x='Make',
        y='Average_Price',
        color='blue',
        alpha=0.3,
        ax=ax,
        title="Comparison of Average Make Prices"
    )
# Allows for placing the matplotlib into a frame, which is then drawn and packed into the frame properly.
    canvas = FigureCanvasTkAgg(fig, master=makeframe)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Function to create the bar plot for Model
def plot_model():
# Create a figure and axes object to plot
    fig, ax = plt.subplots()
    avg_price_by_model.plot(
        kind='bar',
        x='Model',
        y='Price',
        color='blue',
        alpha=0.3,
        ax=ax,
        title="Comparison of Average Model Prices"
    )
# Allows for placing the matplotlib into a frame, which is then drawn and packed into the frame properly.
    canvas = FigureCanvasTkAgg(fig, master=modelframe)
    canvas.draw()
    canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)

# Create buttons/text to reveal the plots and the dataframe and help text (Calling the function for revealing the graphs and the dataframe and help text)
Plot1_Make = tk.Button(makeframe, text="Plot Make Prices", command=plot_make)
Plot1_Make.pack(pady=10)

Plot2_Model = tk.Button(modelframe, text="Plot Model Prices", command=plot_model)
Plot2_Model.pack(pady=10)

DataFrame_Model = tk.Button(dataframe, text="Show DataFrame", command=data_make)
DataFrame_Model.pack(pady=10)

Help_Text = tk.Label(helpframe, text="For context, the first frame contains the average brand pricing, second frame average model pricing of each brand, and the third frame contains all the information in the original dataframe.")
Help_Text.place(x=50, y=50)

# Finally reveal the GUI
root.mainloop()