# What is SpeedPI? 

**SpeedPI is a tool that lets you test your internet connection with jush a push of a button.**
![](https://user-images.githubusercontent.com/44171411/57285640-eed67600-70b3-11e9-8020-a83d2e0a7554.png)
# README.md

----



### Instructions

#### What to install before testing your internet connection.

`$ pip install RPi.GPIO`


`$ pip install RPLCD`

`$ pip install speedtest-cli`

#### Main function (On boot up)

**This** is the **main** function that runs when the **PI** **boots** **up**.

    def onButton(channel):
   		if channel == 16:	##In this case the channel is 16
        		os.system("/home/root/myscripts/speedtest.py")
### Circuit

![Circuit](https://user-images.githubusercontent.com/44171411/57286331-50e3ab00-70b5-11e9-8209-ffb893d57890.jpg)


----

### Group


- **Akash Verma** *([Program Developer](https://github.com/itisverma/speedPI/tree/master/code))*	  -- https://github.com/itisverma
- **Nicola Prevedello** *([Presentation developer](https://prezi.com/wdbphm_2kc77/?utm_campaign=share&utm_medium=copy&rc=ex0share))*    --  https://github.com/PRVNick
- **Ye Congzhou** *([Circuit developer](https://user-images.githubusercontent.com/44171411/57286331-50e3ab00-70b5-11e9-8209-ffb893d57890.jpg))*  -- https://github.com/congzhouye
- **Manolache Pavel** *([UML developer](https://github.com/itisverma/speedPI/tree/master/umlDiagrams))* -- https://github.com/PavelManolache
- **Ismail Rachid** *([UML developer](https://github.com/itisverma/speedPI/tree/master/umlDiagrams))*
     
----
                
### FlowChart

![flowchart](https://user-images.githubusercontent.com/44171411/57286116-e92d6000-70b4-11e9-9940-9a943dcd2b35.png)

### UML Sequence Diagram
![Sequence](https://user-images.githubusercontent.com/44171411/57600113-2b451e80-7559-11e9-9d09-33273f5a5a09.jpg)
### UML User case Diagram
![User case](https://user-images.githubusercontent.com/44171411/57600149-47e15680-7559-11e9-9f84-5ffa81c3824e.jpg)

```


