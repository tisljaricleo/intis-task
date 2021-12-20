import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_theme()


def main():

    # Path to dataset.
    data_path = r"./data/podaci.csv"

    # Load data into Pandas dataframe.
    data = pd.read_csv(data_path, sep=",", names=["x1", "x2", "x3", "x4", "u"])

    # provjeriti dtypes
    # je li treba flaot 32 ili normalizirati

    sns.pairplot(data=data, hue=["x1", "x2", "x3", "x4", "u"])
    plt.show()

    print()


if __name__ == "__main__":
    main()
