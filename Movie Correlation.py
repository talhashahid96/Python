import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
pd.set_option("display.max_rows", 10000)
pd.set_option("display.max_columns", 100)
pd.set_option("display.width", 10000)
data = pd.read_csv("movies.csv")
#print(data.head())

# Check for NULL Values

#print(data.isnull().any())

# Find the NULL Percentages

null_percentages = (data.isnull().sum() / len(data) * 100).round(2)
#print(null_percentages)

# Check Data Types

#print(data.dtypes)

# Drop Null Values

data = data.dropna()

# Change data type

data = data.astype({"budget":"int64","gross":"int64"})

# Sort by Budget

sorted_budget = data.sort_values(by='budget',ascending=False)
#print(sorted_budget.head())

# Scatter plot to check correlation b/w budget and gross
def scatter_plot():
    plt.scatter(x=sorted_budget['budget'],y=sorted_budget['gross'])
    plt.title("Budget and Gross Earnings")
    plt.xlabel("Budget")
    plt.ylabel("Gross")

    # Regplot (Line intersection)

    sns.regplot(data= sorted_budget,x="budget",y="gross",scatter_kws={"color":"blue"},line_kws={"color":"red"})
    plt.show()

#scatter_plot()
# Find correlation of budget with all numeric columns

correlation_matrix_numericonly = data.corr(numeric_only=True)
#print(correlation_matrix)
# Heatmap of correlation matrix

def heat_map_no():
    sns.heatmap(correlation_matrix_numericonly,annot=True)
    plt.title("Correlation between variables")
    plt.xlabel("Movie functions")
    plt.ylabel("Movie functions")
    plt.show()
#heat_map_no()

# Numerization. converting objects to numeric codes (cat codes)
print(data.head())
df_numerized = data
for col_name in df_numerized:
    if (df_numerized[col_name].dtype == 'object'):
        df_numerized[col_name] = df_numerized[col_name].astype("category")
        df_numerized[col_name] = df_numerized[col_name].cat.codes
print(df_numerized.head())

correlation_matrix = df_numerized.corr()
def heatmap():
    sns.heatmap(correlation_matrix,annot=True)
    plt.title("Correlation between variables")
    plt.xlabel("Movie features")
    plt.ylabel("Movie features")
    plt.show()
#heatmap()

corr_pair_sorted = correlation_matrix.unstack().sort_values()
high_corr = corr_pair_sorted[(corr_pair_sorted) > 0.5]
print("High Correlation between the following\n",high_corr)
