import serial 
import numpy as np
import matplotlib.pyplot as plt



plt.close('all')                                               #clear all the previous plots if present


raw = serial.Serial('com6', baudrate = 115200, timeout = 10)   #selects the com port and baudrate
adc_values = []
dac_values = []
i = 0
x = np.linspace(1, 1000, 1000)                                 #generating the values for x-axis to plot


#--------------------Serial_read_begins------------------------#
while i<1000:

	data = raw.readline(1000).decode('utf-8').rstrip('\n')
	
	split_data = data.split(',')								#values is separated from its original form(1,2) to 1 2
	adc_values = np.append(adc_values, split_data[0])			#appending first value to a defined variable adc_values
	dac_values = np.append(dac_values, split_data[1])			#appending second value to a defined variable dac_values

	i=i+1


#---------------------saving the serial splitted data to text file one by one----------------------------#
with open('adc_values.txt', 'wb') as f:
    np.savetxt(f, np.column_stack(adc_values), fmt='%s\r\n')

f.close()

with open('dac_values.txt', 'wb') as f:
    np.savetxt(f, np.column_stack(dac_values), fmt='%s\r\n')

f.close()


#---------------------importing the text files for plot--------------------------------------------------#
filename1 = "adc_values.txt"

filename2 = "dac_values.txt"


plt.close('all')

data1 = np.loadtxt(filename1, dtype = int, skiprows = 0,  max_rows = 1000)
data2 = np.loadtxt(filename2, dtype = int,skiprows = 0,  max_rows = 1000)

fig, ax = plt.subplots(figsize=(24,24))


plt.plot(x, data1, 'r', marker = 'd', markersize = 2, label = 'ADC_values')
plt.plot(x,data2, marker = 'o', markersize = 2, label = 'DAC_values')


plt.xlabel("Index")
plt.ylabel("ADC_COUNTS")
plt.legend(loc='best')
plt.show()

	