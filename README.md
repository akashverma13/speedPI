# What is SpeedPI? 

**SpeedPI is a tool that lets you test your internet connection with jush a push of a button.**
![](https://user-images.githubusercontent.com/44171411/57285640-eed67600-70b3-11e9-8020-a83d2e0a7554.png)
# README.md

![](https://img.shields.io/github/stars/pandao/editor.md.svg) ![](https://img.shields.io/github/forks/pandao/editor.md.svg) ![](https://img.shields.io/github/tag/pandao/editor.md.svg) ![](https://img.shields.io/github/release/pandao/editor.md.svg) ![](https://img.shields.io/github/issues/pandao/editor.md.svg) ![](https://img.shields.io/bower/v/editor.md.svg)


----



### Instructions

#### What to install, before testing your internet connection.

`$ pip install RPi.GPIO`


`$ pip install RPLCD`

`$ pip install speedtest-cli`

#### Main function (On boot up)

**This** is the **main** function that is run when the **PI** **boots** **up**.

    def onButton(channel):
   		if channel == 16:	##In this case the channel is 16
        		os.system("/home/root/myscripts/speedtest.py")
### Circuit

![Circuit](https://user-images.githubusercontent.com/44171411/57286331-50e3ab00-70b5-11e9-8209-ffb893d57890.jpg)


----

### Componenti gruppo


- **Akash Verma** *([Program Developer](https://github.com/itisverma/speedPI/tree/master/code)*	  -- https://github.com/itisverma
- **Nicola Prevedello** *([Presentation developer](https://prezi.com/wdbphm_2kc77/?utm_campaign=share&utm_medium=copy&rc=ex0share)*
- **Ye Conghzu** *([Circuit developer](https://user-images.githubusercontent.com/44171411/57286331-50e3ab00-70b5-11e9-8209-ffb893d57890.jpg)))*
- **Manolache Pavel** *([UML developer](https://github.com/itisverma/speedPI/tree/master/umlDiagrams)*
- **Ismail Rachid** *([UML developer](https://github.com/itisverma/speedPI/tree/master/umlDiagrams)*
     
----
                
### FlowChart

![flowchart](https://user-images.githubusercontent.com/44171411/57286116-e92d6000-70b4-11e9-9940-9a943dcd2b35.png)

### UML CLASS
insert here
### UML User case
insert here
```


