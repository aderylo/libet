import os
import pandas as pd
import matplotlib.pyplot as plt

data_directory = "data"

for filename in os.listdir(data_directory):
    if "press" in filename:
        df = pd.read_csv(f"data/{filename}", delimiter=";")
        df = df[["dotDelay", "pressOnset", "ansTime"]]
        df["timeDelta"] = df["ansTime"] - df["pressOnset"]

        descriptive_stats = df.describe()
        descriptive_stats.to_csv(f"stats/{filename}")

        plt.figure(figsize=(10, 6))
        df[["timeDelta"]].boxplot()
        plt.title(
            "Wykres pudelkowy czasu pomiedzy uswiadomieniem intencji a nacisnieciem"
        )
        plt.ylabel("Sekundy")
        plt.xticks(rotation=45)

        plt.savefig(f"plots/{filename}.png")
