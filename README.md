# Report Of Ros Communication Experiment
## Introduction:
  Communication Between different Robot (*Node*) is essential in multirobots system. In simulated condition each robots can communicate with other robots easily without worrying **Time Delay** and **Lost Bags** due to bad communiction condition i.e.: Weak Signal or Signal interference. In real condition while the signal quality cannot be on hundred percent guaranteed, **Time delay** and **lost bags** might lead to catastrophic consequnce i.e.: Robot collision or ineffective movement due to out of day position information. This Report illustrate ros commuication result in physical world as well as derived reasoning and suggestions to properly implement ros communication in a multi-robots system.
## Experiment Enviorment:
  This communication experiment was conducted with three Nvidia TX1 AI development boards connected to 5G wifi through a wifi router. Experiment surrounding was HKU Dreamlab where there was no strong interference from other wifi or communication devices that shares 5G channel. Three borad are placed at different location inside the lab and have slightly different distance between itself and router(Under Normal condition. Signal Quality can be considered as sufficiently good). As it might illustrated below the to exam the signal quality's impact on communication, we create poor signal quality by remove the Wi-Fi antenna of the machine running **master** node, the signal strength with antenna is 866 mb/s and without antenna is 175 mb/s.
## Condition Statement and Experiment Result:
### 1.Time Delay Between Different Node:
#### Variable One: Distance Between Wi-Fi Router:
####                        Result Diagram 1.1
![**Result Diagram 1.1**](/communication_exp/ping_delay/result.png)
####                        Result Diagram 1.2
![**Result Diagram 1.2**](/communication_exp/ping_delay/wireless_vs_wired.png)
#### Illustration: 
   * The test data is gathered from Desktop PC running Linux 16.04 connected to the Local Area Network through wire. The time delay      * when ping itself is ignorable and can refer to Wired Control group shows in Diagram 1.2.
    1. As it is shown in diagram 1.1 the distance factor plays a trivial role in affecting ping delay of different node.
    1. However, the delay varies significantly between approximately 30ms to approximately 280ms, the variation is periodic:
      1. **Reason analysis**: By comparing ping devices running different operating system (Linux: Android(Huawei P20 Pro); Linux:    Raspbian(Raspberry pi 3b+); Window 10 (Huawei Matebook d); IOS 12 (ipad);Ubuntu 16.04 on Jetson Tx 1 and Huawei Matebook d and raspberry pi), as well as comparing divices with different Wi-Fi embedded module: (Ubuntu 16.04 using Intel Dual band Wi-Fi ac 8265; Ubuntu 16.04 using Cypress CYW43455; Ubuntu 16.04 using Cypress CYW4354); The difference in Wi-Fi module proves to be most influential on ping delay and delay pattern. While module using Intel Dual band Wi-Fi ac 8265 and Cypress CYW4354 has ping delay averagely 5ms.
      1. **Improvement** :If the real time requirement is important in a multi-robot system. The factor of transmitting chip and hardware generated delay need to be considered.
### 2.Communication Band Width Under ~~Three~~ different senarios:
#### Variable Two: Communication Architecture and Signal Strength:
####                       Result Diagram 2.1
![Result Diagram 2.1](/communication_exp/ros_bw/result.png)
#### Illustration:
  * The test data is gathered from device running master node the talker and listener code are obtained from ros official tutorial and modified to maximize the data transmit quantity (A string with size of 1,600,000 character) for stress test Code Link: **To be Uploaded** , as it mentioned above and shown in diagram 2.1 the "Blocked means the TX 1's wifi antenna is removed and the signal quality decreased from 866mb/s to 175mb/s" which simulate real senario where some robot nodes are under signal inteference or distrubuted in further distance.
    1. As its is shown in senario 2, The master Node play the same role as talker while the rest two node are listener can obtain best communication band width. Since the communication is one way without a intermedia. As shown in diagram 2.2.
    ![Diagram2.2](/communication_exp/io_diagram/Diagram2.2)
    #### Architecture Diagram 2.2
    1. As its is shown in senario 1 and senario 3. The maximum transmitting rate stay roughly 1.5 - 1.7 mb/s where senario 1 has slightly better performance. The diagram 2.3 shows the architecture of senario 1.
    #### Architecture Diagram 2.3
    ![Diagram2.3](/communication_exp/io_diagram/Diagram2.3)
    1. In the controlled group
  
  
