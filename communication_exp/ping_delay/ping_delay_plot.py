import matplotlib.pyplot as plt
import numpy as np
import statistics as st
#Save all data For final Graph
general_list = []
#Visualize First Node 

file = open('ping_data1.txt','r')
data_list = []
for i in file:
	data_list.append(float(i[5:]))
general_list.append(data_list[0:180])
plt.subplot(2,2,1)
plt.plot(data_list[0:180])
std_dev = st.stdev(data_list[0:180])
average = st.mean(data_list[0:180])
plt.text(0,300,r'$\mu=%f,\ \sigma=%f$'%(average,std_dev))
plt.title("Delay from Node 1 Distance From Signal Source 1m No block")
plt.xlabel("Time in second")
plt.ylabel("Time delay in millisecond")
file.close()

#Visualize Second Node

file = open('ping_data2.txt','r')
data_list = []
for i in file:
	data_list.append(float(i[5:]))
general_list.append(data_list[0:180])
plt.subplot(2,2,2)
plt.plot(data_list[0:180])
std_dev = st.stdev(data_list[0:180])
average = st.mean(data_list[0:180])
plt.text(0,220,r'$\mu=%f,\ \sigma=%f$'%(average,std_dev))
plt.title("Delay from Node 2 Distance From Signal Source 3m No block")
plt.xlabel("Time in second")
plt.ylabel("Time delay in millisecond")
file.close()

#Visualize Third Node

file = open('ping_data3.txt','r')
data_list = []
for i in file:
	data_list.append(float(i[5:]))
general_list.append(data_list[0:180])
plt.subplot(2,2,3)
plt.plot(data_list[0:180])
std_dev = st.stdev(data_list[0:180])
average = st.mean(data_list[0:180])
plt.text(0,250,r'$\mu=%f,\ \sigma=%f$'%(average,std_dev))
plt.title("Delay from Node 3 Distance From Signal Source 5m No Block")
plt.xlabel('Time in second')
plt.ylabel('Time delay in millisecond')
file.close()

#Visualize Three Node in a comparable way as well as local Ping delay

file = open('Control_data.txt','r')
data_list = []
for i in file:
	data_list.append(float(i[5:]))
general_list.append(data_list[0:180])
plt.subplot(2,2,4)
x=np.linspace(1,180,180)
plt.plot(x,general_list[0][:],'r-',x,general_list[1][:],'b-',x,general_list[2][:],'g-',x,general_list[3][:],'k-')
plt.legend(('Node1','Node2','Node3','Control'),loc='upper right')
plt.title("Cross compare between test and control")
plt.xlabel('Time in second')
plt.ylabel('Time delay in millisecond')
file.close()
plt.show()

#Visualize Ping delay of Wire connect and Wireless connect
file = open('Wireless__control.txt','r')
data_list = []
for i in file:
	data_list.append(float(i[5:]))
general_list.append(data_list[0:180])
plt.plot(x,general_list[3][:],'b',x,general_list[4][:],'r')
std_dev = st.stdev(data_list[0:180])
average = st.mean(data_list[0:180])
plt.text(0,2,r'Wired: $\mu=%f,\ \sigma=%f$'%(average,std_dev))
std_dev = st.stdev(general_list[3][:])
average = st.mean(general_list[3][:])
plt.text(0,1.5,r'Wireless: $\mu=%f,\ \sigma=%f$'%(average,std_dev))
plt.xlabel('Time in second')
plt.ylabel('Time delay in millisecond')
plt.title('Delay compare between Wired local host and wireless local host')
plt.legend(('Wired','Wireless'),loc='upper right')
plt.show()
file.close()

