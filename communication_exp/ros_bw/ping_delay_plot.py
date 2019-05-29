import matplotlib.pyplot as plt
import numpy as np
import statistics as st
#Save all data For final Graph
general_list = []
#Visualize First Node 

file = open('ros_bw_coretalklisten_data.txt','r')
data_list = []
for i in file:
	data_list.append(float(i[0:4]))
general_list.append(data_list[0:180])
plt.subplot(2,2,1)
plt.plot(data_list[0:180])
std_dev = st.stdev(data_list[0:180])
average = st.mean(data_list[0:180])
plt.text(0,3,r'$\mu=%f,\ \sigma=%f$'%(average,std_dev))
plt.title("Senario 1 Node1 :Master Node2 :Talker Node3 :Listener")
plt.xlabel("Time in second")
plt.ylabel("Bandwidth in Mb/S")
file.close()

#Visualize Second Node

file = open('ros_bw_coretalkerlistenlisten_data.txt','r')
data_list = []
for i in file:
	data_list.append(float(i[0:4]))
general_list.append(data_list[0:180])
plt.subplot(2,2,2)
plt.plot(data_list[0:180])
std_dev = st.stdev(data_list[0:180])
average = st.mean(data_list[0:180])
plt.text(0,3,r'$\mu=%f,\ \sigma=%f$'%(average,std_dev))
plt.title("Senario 2 Node1 :Master and talker Node2&3 :Listener")
plt.xlabel("Time in second")
plt.ylabel("Bandwidth in Mb/S")
file.close()

#Visualize Third Node

file = open('ros_bw_blocked_data.txt','r')
data_list = []
for i in file:
	data_list.append(float(i[0:4]))
general_list.append(data_list[0:180])
plt.subplot(2,2,3)
plt.plot(data_list[0:180])
std_dev = st.stdev(data_list[0:180])
average = st.mean(data_list[0:180])
plt.text(0,3,r'$\mu=%f,\ \sigma=%f$'%(average,std_dev))
plt.title("Senario 3 Node1 :Master and talker(Antenna Removed) Node2&3 :Listener")
plt.xlabel('Time in second')
plt.ylabel('Bandwidth in Mb/S')
file.close()

#Visualize Three Node in a comparable way as well as local Ping delay

file = open('ros_bw_control_data.txt','r')
data_list = []
for i in file:
	data_list.append(float(i[0:4]))
general_list.append(data_list[0:180])
plt.subplot(2,2,4)
x=np.linspace(1,180,180)
plt.plot(x,general_list[0][:],'r-',x,general_list[1][:],'b-',x,general_list[2][:],'g-',x,general_list[3][:],'k-')
plt.legend(('senario 1','Senario 2','Senario 3','Control'),loc='upper right')
plt.title("Cross compare between test and control")
plt.xlabel('Time in second')
plt.ylabel('Bandwidth in Mb/S')
file.close()
plt.show()

#Visualize Ping delay of Wire connect and Wireless connect
#file = open('Wireless__control.txt','r')
#data_list = []
#for i in file:
#	data_list.append(float(i[5:]))
#general_list.append(data_list[0:180])
#plt.plot(x,general_list[3][:],'b',x,general_list[4][:],'r')
#std_dev = st.stdev(data_list[0:180])
#average = st.mean(data_list[0:180])
#plt.text(0,2,r'Wired: $\mu=%f,\ \sigma=%f$'%(average,std_dev))
#std_dev = st.stdev(general_list[3][:])
#average = st.mean(general_list[3][:])
#plt.text(0,1.5,r'Wireless: $\mu=%f,\ \sigma=%f$'%(average,std_dev))
#plt.xlabel('Time in second')
#plt.ylabel('Time delay in millisecond')
#plt.title('Delay compare between Wired local host and wireless local host')
#plt.legend(('Wired','Wireless'),loc='upper right')
#plt.show()
#file.close()

