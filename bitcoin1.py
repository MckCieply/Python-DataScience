import numpy as np
import matplotlib.pyplot as plt
data = np.loadtxt("Data/BTC-USD.csv")
yearly = data[0:365]
mean = round(np.mean(yearly),2)
median = round(np.median(yearly),2)
minimum = round(np.min(yearly),2)
maximum = round(np.max(yearly),2)
deviation = round(np.std(yearly),2)
q1 = round(np.median(yearly[:len(yearly)//2]),2)
q3 = round(np.median(yearly[len(yearly)//2:]),2)
iqr = round(q3 - q1,2)
print(f"""Arithmetic mean: {mean},
Median: {median},
Minimum: {minimum},
Maximum: {maximum},
Standard Deviation: {deviation},
Interquartile Range: {iqr}""")

plt.plot(yearly, color="red", linestyle="dotted")
plt.title("BTC to USD")
plt.show()
