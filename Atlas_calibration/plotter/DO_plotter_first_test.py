import os
import pandas as pd
import matplotlib.pylab as plt
import scienceplots
'''
This file plots the .csv file of a test taken with two bowls 
filled with water with different salinity levels
S_low = 0 grams salt
S_high = 178 grams salt

sample time = 0.65

with pump

'''

plt.style.use(['science', 'no-latex'])

path = os.getcwd()


file_fresh= '/home/peder/GitHub/Tools/Atlas_calibration/plotter/files/rpi/DO_fresh_test_1305.csv'
file_salt= '/home/peder/GitHub/Tools/Atlas_calibration/plotter/files/rpi/DO_salt_test_1305.csv'


df_fresh = pd.read_csv(file_fresh)
df_salt = pd.read_csv(file_salt)

cutoff = 130

df_salt_fixed = df_salt.drop(df_salt.index[:cutoff])
df_salt_fixed = df_salt_fixed.reset_index(drop=True)
df_salt_fixed = df_salt_fixed.loc[0:700]

df_fresh_fixed = df_fresh.drop(df_fresh.index[:cutoff])
df_fresh_fixed = df_fresh_fixed.reset_index(drop=True)
df_fresh_fixed = df_fresh_fixed.loc[0:700]


in_text = (10, 4)

# Figure 1
plt.figure(figsize=in_text)
plt.plot(df_fresh_fixed['reading'], label='0 grams salt')
plt.plot(df_salt_fixed['reading'], label='178 grams salt')

plt.legend(loc='center right')
# plt.tight_layout()
plt.grid()
plt.xlabel('Samples')
plt.ylabel('Salinity [mg/l]')

plt.savefig("pictures/Super_salt_test.png", dpi = 500)
plt.show()

