import os
import pandas as pd
import matplotlib.pylab as plt
import scienceplots
'''
This file plots the .csv file of a test taken with two teacups 
filled with water with different temperatures
T_low = approx 20 C
T_high = approx 45 C

sample time = 0.6

reading 0 - 100 = cold water
reading 101 - 200 = warm water
reading 201 - 300 = cold water

'''

plt.style.use(['science', 'no-latex'])

path = os.getcwd()


file= '/home/peder/GitHub/Tools/Atlas_calibration/plotter/files/DO_cold_warm_cold.csv'


df = pd.read_csv(file)


cutoff = [0, 7, 102, 197, 302]

air_df = df.loc[cutoff[0]:cutoff[1]]
cold1_df = df.loc[cutoff[1]:cutoff[2]]
warm_df = df.loc[cutoff[2]:cutoff[3]]
cold2_df = df.loc[cutoff[3]:cutoff[4]]


in_text = (10, 4)

# Figure 1
plt.figure(figsize=in_text)
# plt.plot(df['reading'], label='test')
plt.plot(air_df['reading'], label='Air')
plt.plot(cold1_df['reading'], label='20°C water')
plt.plot(warm_df['reading'], label='45°C water')
plt.plot(cold2_df['reading'], label='20°C water')

plt.legend(loc='upper right')
# plt.tight_layout()
plt.grid()
plt.xlabel('Samples')
plt.ylabel('Salinity [mg/l]')
plt.savefig("Temp_test.png", dpi = 500)
plt.show()

