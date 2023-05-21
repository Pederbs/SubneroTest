import os
import pandas as pd
import matplotlib.pylab as plt
import scienceplots


plt.style.use(['science', 'no-latex'])

path = os.getcwd()
file_fresh = 'fresh_water_test.csv'
file_salt = 'salt_water_test.csv'

# file_fresh = 'first_air_test.csv'
# file_salt = 'second_air_test.csv'

df_fresh = pd.read_csv(path + '/Atlas_calibration/plotter/files/14mai/' + file_fresh)
df_salt = pd.read_csv(path + '/Atlas_calibration/plotter/files/14mai/' + file_salt)


df_salt_fixed = df_salt.drop(df_salt.index[:150])
df_salt_fixed = df_salt_fixed.reset_index(drop=True)

df_fresh_fixed = df_fresh.drop(df_fresh.index[:150])
df_fresh_fixed = df_fresh_fixed.reset_index(drop=True)

fig, ax = plt.subplots()
# ax.plot(df_fresh_fixed['reading'], label='Fresh water')
# ax.plot(df_salt_fixed['reading'], label='Salt water')

ax.plot(df_fresh['reading'], label='Fresh water')
ax.plot(df_salt['reading'], label='Salt water')

ax.legend(loc='upper right')

# df_all['fresh'] = df_fresh
# df_all['salt'] = df_salt
# df_all.plot()
# plt.tight_layout()
# plt.savefig("pictures/test.png", dpi = 500)

plt.show()