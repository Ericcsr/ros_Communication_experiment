# Report Of Ros Communication Experiment
## Introduction:
  Communication Between different Robot (*Node*) is essential in multirobots system. In simulated condition each robots can communicate with other robots easily without worrying **Time Delay** and **Lost Bags** due to bad communiction condition i.e.: Weak Signal or Signal interference. In real condition while the signal quality cannot be on hundred percent guaranteed, **Time delay** and **lost bags** might lead to catastrophic consequnce i.e.: Robot collision or ineffective movement due to out of day position information. This Report illustrate ros commuication result in physical world as well as derived reasoning and suggestions to properly implement ros communication in a multi-robots system.
## Experiment Enviorment:
  This communication experiment was conducted with three Nvidia TX1 AI development boards connected to 5G wifi through a wifi router. Experiment surrounding was HKU Dreamlab where there was no strong interference from other wifi or communication devices that shares 5G channel. Three borad are placed at different location inside the lab and have slightly different distance between itself and router(Under Normal condition. Signal Quality can be considered as sufficiently good). As it might illustrated below the to exam the signal quality's impact on communication, we create poor signal quality by remove the Wi-Fi antenna of the machine running **master** node, the signal strength with antenna is 866 mb/s and without antenna is 175 mb/s.
## Condition Statement and Experiment Result:
  ### Time Delay Between Different Node:
  #### Variable One: Distance Between Wi-Fi Router:
  ![**Result Diagram**](/communication_exp/ping_delay/result.png)
  Format: ![Alt Text](url)
  
  
