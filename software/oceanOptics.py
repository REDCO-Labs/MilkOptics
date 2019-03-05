import matplotlib.pyplot as plt
import seabreeze.spectrometers as sb
import numpy as np
import time
import os

devices = sb.list_devices()
print(devices)

spec = sb.Spectrometer(devices[0])
spec.integration_time_micros(1500)

waves = spec.wavelengths()[2:]
intens = spec.intensities()[2:]

maxi = 0
mini = 10000

fig, ax = plt.subplots()
graph, = ax.plot(waves, intens)
plt.xlabel("Longueur d'onde [nm]")
plt.ylabel("Intensité")

plt.pause(0.05)

data = []

for i in range(10):
    intens = []
    for j in range(10):
        intens.append(spec.intensities()[2:])

    intens = np.mean(intens, axis=0)
    data.append(intens)

    graph.set_ydata(intens)
    if min(intens) < mini:
        mini = min(intens)
    if max(intens) > maxi:
        maxi = max(intens)

    plt.ylim(mini, maxi)
    plt.pause(0.01)

data = np.mean(data, axis=0)

waves = waves[np.newaxis].T
data = data[np.newaxis].T

arr = np.hstack((waves, data))
print(arr.shape)

filename = "data"
num = 0
while os.path.exists("{}{}.txt".format(filename, num)):
    num += 1
np.savetxt("{}{}.txt".format(filename, num), arr, newline="\n")
