import pandas as pd

def main():
    frutas = pd.read_csv("./data/fruit_data_with_colors.txt", sep="\t")
    d = frutas.describe()
    print(d)


if __name__ == "__main__":
    main()
