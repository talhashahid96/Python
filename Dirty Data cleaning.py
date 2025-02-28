import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

pd.set_option("display.max_rows", 10000)
pd.set_option("display.max_columns", 100)
pd.set_option("display.width", 1000)
df = pd.read_csv("dirty_cafe_sales.csv")

df = df.dropna(subset=["Quantity", "Price Per Unit"])
#print(df.isna().sum())
df = df.loc[df["Quantity"] != "ERROR"]  # Remove String ERROR in rows
df = df.query("Quantity!='UNKNOWN'")  # Method 2 to remove certain values
error_count = df.loc[df["Price Per Unit"] == "ERROR"]  # Checking errors in price per unit
unknown_count = df.loc[df["Price Per Unit"] == "UNKNOWN"]  # Same
# print(error_count["Price Per Unit"].value_counts())
# print(unknown_count["Price Per Unit"].value_counts())
df = df.loc[df["Price Per Unit"] != "ERROR"]
df = df.loc[df["Price Per Unit"] != "UNKNOWN"]
df = df.reset_index()
df.index += 1
df = df.astype({"Quantity": "int32", "Price Per Unit": "float"})
#print(df.dtypes)
df = df.drop(columns="Total Spent", inplace=False)
df["Total Spent"] = df["Quantity"] * df["Price Per Unit"]
col_to_move = df.pop("Total Spent")  # Moving columns
df.insert(5, "Total Spent", col_to_move)


def word_to_split(word_name):
    to_split = word_name.split("_")
    return pd.Series([to_split[0], to_split[1]])


df[["Transaction", "ID"]] = df["Transaction ID"].apply(word_to_split)
df = df.drop(columns="Transaction ID", inplace=False)
transaction_move = df.pop("Transaction")
df.insert(1, "Transaction", transaction_move)
id_move = df.pop("ID")
df.insert(2, "TRX ID", id_move)
df["TRX ID"] = df["TRX ID"].astype(int)
#print(df.dtypes)
# print(df.head(100))
corre_matrix = df.corr(numeric_only=True)
#print(corre_matrix)


def heat_map():
    plt.figure()
    sns.heatmap(data=corre_matrix, annot=True)
    plt.title("Variables Correlation")
    plt.show()


#heat_map()