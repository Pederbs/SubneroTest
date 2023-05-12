import os
import pandas as pd
import matplotlib.pylab as plt
import scienceplots


plt.style.use(['science', 'no-latex'])

path = os.getcwd()
file_fresh = 'DO_test_fresh_water.csv'
file_salt = 'DO_test_salt_water.csv'

df_fresh = pd.read_csv(path + '/Atlas_calibration/plotter/files/' + file_fresh)
df_salt = pd.read_csv(path + '/Atlas_calibration/plotter/files/' + file_salt)


df_salt_fixed = df_salt.drop(df_salt.index[:190])
df_salt_fixed = df_salt_fixed.reset_index(drop=True)

fig, ax = plt.subplots()
ax.plot(df_fresh, label='Fresh water')
ax.plot(df_salt_fixed, label='Salt water')

ax.legend(loc='upper right')

# df_all['fresh'] = df_fresh
# df_all['salt'] = df_salt
# df_all.plot()

plt.show()