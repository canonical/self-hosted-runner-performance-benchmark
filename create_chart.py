
from matplotlib import pyplot as plt
import pandas as pd
import os

run_name = os.getenv("RUN_NAME")

my_data = pd.read_csv(f"results/v1/{run_name}.csv")
my_data["time"] = pd.to_datetime(my_data["time"])

plt.subplot(2, 4, 1)
plt.plot(my_data["time"], my_data["network speed test ping (s)"])
plt.title("Network Speed Test Ping")
plt.xlabel("Time")
plt.ylabel("Seconds")

plt.subplot(2, 4, 2)
plt.plot(my_data["time"], my_data["jitter (s)"])
plt.title("Jitter")
plt.xlabel("Time")
plt.ylabel("Seconds")

plt.subplot(2, 4, 3)
plt.plot(my_data["time"], my_data["upload (bit/s)"])
plt.title("Upload")
plt.xlabel("Time")
plt.ylabel("MBit/s")

plt.subplot(2, 4, 4)
plt.plot(my_data["time"], my_data["download (bit/s)"])
plt.title("Download")
plt.xlabel("Time")
plt.ylabel("MBit/s")

plt.subplot(2, 1, 2)
plt.plot(my_data["time"], my_data["max (s)"], label = "max")
plt.plot(my_data["time"], my_data["charmhub resource download mean (s)"], label = "mean")
plt.plot(my_data["time"], my_data["min (s)"], label = "min")
plt.legend()
plt.title("Charmhub Resource Download")
plt.xlabel("Time")
plt.ylabel("Seconds")

fig = plt.gcf()
fig.set_figwidth(1.5 * 16)
fig.set_figheight(1.5 * 9)
plt.savefig(f"results/v1/{run_name}.png")

