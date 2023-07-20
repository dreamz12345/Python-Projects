import pandas

data = pandas.read_csv(
    "25 - Pandas/2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"
)

fur_colors = data["Primary Fur Color"].value_counts()

squirrels_df = pandas.DataFrame(
    {
        "Color": fur_colors.index,
        "Count": fur_colors.values,
    }
)

pandas.DataFrame.to_csv(squirrels_df, "25 - Pandas/squirrel_data.csv")
