
from matplotlib import pyplot as plt
import pandas as pd
import os

my_data = pd.read_csv(f"results/v1/{os.getenv[RUN_NAME}.csv")
my_data["time"] = pd.to_datetime(my_data["time"])

figure, axis = plt.subplots(2, 4)

axis[0, 0].plot(my_data[time], my_data["network speed test ping (s)"])
axis[0, 0].set_title("Network Speed Test Ping")
axis[0, 0].set_xlabel("Time")
axis[0, 0].set_ylabel("Seconds")

axis[0, 1].plot(my_data[time], my_data["jitter (s)"])
axis[0, 1].set_title("Jitter")
axis[0, 1].set_xlabel("Time")
axis[0, 1].set_ylabel("Seconds")

axis[0, 2].plot(my_data[time], my_data["upload (bit/s)"])
axis[0, 2].set_title("Upload")
axis[0, 2].set_xlabel("Time")
axis[0, 2].set_ylabel("MBit/s")

axis[0, 3].plot(my_data[time], my_data["download (bit/s)"])
axis[0, 3].set_title("Download")
axis[0, 3].set_xlabel("Time")
axis[0, 3].set_ylabel("MBit/s")

axis[1, 0].plot(my_data[time], my_data["charmhub resource download mean (s)"])
axis[1, 0].set_title("Charmhub Resource Download Mean")
axis[1, 0].set_xlabel("Time")
axis[1, 0].set_ylabel("Seconds")

axis[1, 1].plot(my_data[time], my_data["min (s)"])
axis[1, 1].set_title("Min")
axis[1, 1].set_xlabel("Time")
axis[1, 1].set_ylabel("Seconds")

axis[1, 2].plot(my_data[time], my_data["max (s)"])
axis[1, 2].set_title("Max")
axis[1, 2].set_xlabel("Time")
axis[1, 2].set_ylabel("Seconds")

figure.set_figwidth(1.5 * 16)
figure.set_figheight(1.5 * 9)
plt.savefig(f"results/v1/{os.getenv[RUN_NAME}.png")

