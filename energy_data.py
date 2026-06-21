import pandas as pd

df = pd.read_csv("energy_data.csv")

days = 30

df["Monthly_kWh"] = (
    df["Power_Watts"] *
    df["Hours_Per_Day"] *
    days
)/1000

print(df)

print("\nTotal Energy Consumption:")
print(df["Monthly_kWh"].sum(),"kWh")


rate = 8

total_units = df["Monthly_kWh"].sum()

bill = total_units * rate

print("Monthly Bill =", bill)
import matplotlib.pyplot as plt

plt.bar(
    df["Device"],
    df["Monthly_kWh"]
)

plt.xticks(rotation=45)

plt.ylabel("kWh")

plt.title("Monthly Energy Consumption")

plt.show()

highest = df.loc[
    df["Monthly_kWh"].idxmax()
]

print(
f"Highest consuming device: {highest['Device']}"
)

if highest["Device"]=="AC":
    print(
    "Reduce AC usage by 1 hour/day to save energy."
    )
import streamlit as st
import pandas as pd

df = pd.read_csv("energy_data.csv")

days = st.slider(
    "Number of Days",
    1,
    31,
    30
)

df["Monthly_kWh"] = (
df["Power_Watts"] *
df["Hours_Per_Day"] *
days
)/1000

st.title(
"Smart Energy Consumption Tracker"
)

st.dataframe(df)

st.bar_chart(
df.set_index("Device")
["Monthly_kWh"]
)

st.metric(
"Total Consumption",
round(df["Monthly_kWh"].sum(),2)
)
