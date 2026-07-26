import pandas as pd

from ml_dell.plotting import savefig



def main():
    f = pd.read_csv("./data/fruit_data_with_colors.txt", sep="\t")
    f_name_freq = f['fruit_name'].value_counts()
    f_name_freq.plot(kind='bar')
    savefig("assets/v1/fruit_name_freq.png", dpi=300)


if __name__ == "__main__":
    main()
