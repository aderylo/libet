import pandas as pd
import matplotlib.pyplot as plt

file_path = "data/subject_1_M-press1.csv"

# Read the data into a DataFrame
df = pd.read_csv(file_path, delimiter=';')

# Select only the columns 'dotDelay', 'pressOnset', and 'ansTime'
df = df[['dotDelay', 'pressOnset', 'ansTime']]
df["timeDelta"] = df['ansTime'] - df['pressOnset']

# Calculate descriptive statistics
descriptive_stats = df.describe()

# Display descriptive statistics
print("Descriptive Statistics:")
print(descriptive_stats)


# Create a box plot for the selected columns
plt.figure(figsize=(10, 6))
df[["timeDelta"]].boxplot()
plt.title("Wykres pudelkowy czasu pomiedzy uswiadomieniem intencji a nacisnieciem ")
plt.ylabel("Sekundy")
plt.xticks(rotation=45)
plt.show()
