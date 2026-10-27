# 1.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("src/hw1_data_analysis/bicycle_data.csv")

# 2. Date should be datetime. The bike counts should be numbers.
df["Date"] = pd.to_datetime(df["Date"])

# 3.
df["Total"] = (
    df["Fremont Bridge Sidewalks, south of N 34th St Cyclist West Sidewalk"]
    + df["Fremont Bridge Sidewalks, south of N 34th St Cyclist East Sidewalk"]
)
df["Hour"] = df["Date"].dt.hour
df["Year"] = df["Date"].dt.year

# 4.
df_2016 = df[df["Year"] == 2016]

# 5. There is 1 time point with missing data.
df_2016 = df_2016.dropna(subset=["Total"])

# 6.
counts_by_hour = df_2016.groupby("Hour")["Total"].mean()
counts_by_hour.plot()
plt.title("Average Bicycle Counts by Hour")
plt.xlabel("Hour of Day")
plt.ylabel("Average Bicycle Count")
plt.savefig("counts_by_hour.png")

# 7. The busiest hour is 17:00.
busiest_hour = counts_by_hour.idxmax()