import os
import pandas as pd
import matplotlib.pylab as plt
import scienceplots


plt.style.use(['science', 'no-latex'])

path = os.getcwd()


folder = 'Full_test'

file_fresh1 = 'DO_LOG_14_05_2023__16_35_13.csv'
file_fresh2 = 'DO_LOG_14_05_2023__16_46_02.csv'
file_fresh3 = 'DO_LOG_14_05_2023__17_20_23.csv'
file_salt1 = 'DO_LOG_14_05_2023__17_37_08.csv'
file_salt2 = 'DO_LOG_14_05_2023__17_47_33.csv'
file_salt3 = 'DO_LOG_14_05_2023__17_58_02.csv'

file_salinity_air = 'C_LOG_14_05_2023__18_19_51.csv'
file_salinity_fresh = 'C_LOG_14_05_2023__18_25_32.csv'
file_salinity_salt = 'C_LOG_14_05_2023__18_31_19.csv'

file_DO_air1 = 'DO_LOG_14_05_2023__16_27_56.csv'
file_DO_air2 = 'DO_LOG_14_05_2023__17_31_13.csv'
file_DO_air3 = 'DO_LOG_14_05_2023__18_08_58.csv'

# file_fresh = 'first_air_test.csv'
# file_salt = 'second_air_test.csv'

df_fresh1 = pd.read_csv(path + '/Atlas_calibration/plotter/files/' + folder + '/' + file_fresh1)
df_fresh2 = pd.read_csv(path + '/Atlas_calibration/plotter/files/' + folder + '/' + file_fresh2)
df_fresh3 = pd.read_csv(path + '/Atlas_calibration/plotter/files/' + folder + '/' + file_fresh3)

df_salt1 = pd.read_csv(path + '/Atlas_calibration/plotter/files/' + folder + '/' + file_salt1)
df_salt2 = pd.read_csv(path + '/Atlas_calibration/plotter/files/' + folder + '/' + file_salt2)
df_salt3 = pd.read_csv(path + '/Atlas_calibration/plotter/files/' + folder + '/' + file_salt3)

df_salinity1 = pd.read_csv(path + '/Atlas_calibration/plotter/files/' + folder + '/' + file_salinity_air)
df_salinity2 = pd.read_csv(path + '/Atlas_calibration/plotter/files/' + folder + '/' + file_salinity_fresh)
df_salinity3 = pd.read_csv(path + '/Atlas_calibration/plotter/files/' + folder + '/' + file_salinity_salt)

df_air1 = pd.read_csv(path + '/Atlas_calibration/plotter/files/' + folder + '/' + file_DO_air1)
df_air2 = pd.read_csv(path + '/Atlas_calibration/plotter/files/' + folder + '/' + file_DO_air2)
df_air3 = pd.read_csv(path + '/Atlas_calibration/plotter/files/' + folder + '/' + file_DO_air3)


# df_salt_fixed = df_salt.drop(df_salt.index[:150])
# df_salt_fixed = df_salt_fixed.reset_index(drop=True)

# df_fresh_fixed = df_fresh.drop(df_fresh.index[:150])
# df_fresh_fixed = df_fresh_fixed.reset_index(drop=True)

in_text = (10, 4)

# Figure 1
plt.figure(figsize=in_text)
plt.plot(df_fresh1['reading'], label='Fresh water')
plt.plot(df_salt1['reading'], label='Salt water')
plt.legend(loc='upper right')
plt.tight_layout()
plt.savefig("pictures/3Vpump.png", dpi = 500)

# Figure 2
plt.figure(figsize=in_text)
plt.plot(df_fresh2['reading'], label='Fresh water')
plt.plot(df_salt2['reading'], label='Salt water')
plt.legend(loc='upper right')
plt.savefig("pictures/NOpump.png", dpi = 500)

# Figure 3
plt.figure(figsize=in_text)
plt.plot(df_fresh3['reading'], label='Fresh water')
plt.plot(df_salt3['reading'], label='Salt water')
plt.legend(loc='lower right')
plt.savefig("pictures/1.7Vpump.png", dpi = 500)

# plt.plot(df_salinity2['reading'], label='salinity of fresh water')
# plt.plot(df_salinity3['reading'], label='salinity of salt water')

# Figure 4
fig, axs = plt.subplots(2, figsize=in_text)
# fig.suptitle('Fresh- and salt-water readings')

axs[0].plot(df_fresh1['reading'], label='3V pump')
axs[0].plot(df_fresh2['reading'], label='no pump')
axs[0].plot(df_fresh3['reading'], label='1.7V pump')

axs[1].plot(df_salt1['reading'], label='3V pump')
axs[1].plot(df_salt2['reading'], label='no pump')
axs[1].plot(df_salt3['reading'], label='1.7V pump')

axs[0].legend(loc='lower left')
axs[1].legend(loc='lower left')
fig.savefig('pictures/allpump.png', dpi=500)



# Figure 5
plt.figure(figsize=in_text)
plt.plot(df_air1['reading'], label='Before all tests')
plt.plot(df_air2['reading'], label='After fresh water')
plt.plot(df_air3['reading'], label='After salt water')
plt.legend(loc='lower right')
plt.savefig("pictures/air.png", dpi = 500)

# plt.tight_layout()
# plt.savefig("test.png", dpi = 500)

# plt.show()