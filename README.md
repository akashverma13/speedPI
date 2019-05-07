# What is SpeedPI? 
![logo](https://user-images.githubusercontent.com/44171411/57285640-eed67600-70b3-11e9-8020-a83d2e0a7554.png)
**SpeedPI is a tool that lets you test your internet connection with jush a push of a button.**
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
### Insert circuit image here
----

### Componenti gruppo


- **Akash Verma** *(Program developer)*	  -- https://github.com/itisverma
- **Nicola Prevedello** *(Presentation developer)*
- **Ye Conghzu** *(Circuit developer)*
- **Manolache Pavel** *(UML developer)*
- **Ismail Rachid** *(Something)*
     
----
                
### FlowChart

![flowchart](https://user-images.githubusercontent.com/44171411/57286116-e92d6000-70b4-11e9-9940-9a943dcd2b35.png)

### Sequence Diagram
insert here
### UML Diagrams
insert here
```


