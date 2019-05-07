###What is SpeedPI?
**SpeedPI is a tool that lets you test your internet connection with jush a push of a button.**

# README.md

##add logo.png here

![](https://img.shields.io/github/stars/pandao/editor.md.svg) ![](https://img.shields.io/github/forks/pandao/editor.md.svg) ![](https://img.shields.io/github/tag/pandao/editor.md.svg) ![](https://img.shields.io/github/release/pandao/editor.md.svg) ![](https://img.shields.io/github/issues/pandao/editor.md.svg) ![](https://img.shields.io/bower/v/editor.md.svg)


----



###Instructions

####What to install, before testing your internet connection.

`$ pip install RPi.GPIO`


`$ pip install RPLCD`

`$ pip install speedtest-cli`

####Main function (On boot up)

**This** is the **main** function that is run when the **PI** **boots** **up**.

    def onButton(channel):
   		if channel == 16:	##In this case the channel is 16
        		os.system("/home/root/myscripts/speedtest.py")
###Circuit
###Insert circuit image here
----

###Componenti gruppo


- **Akash Verma** *(Program developer)*	  -- https://github.com/itisverma
- **Nicola Prevedello** *(Presentation developer)*
- **Ye Conghzu** *(Circuit developer)*
- **Manolache Pavel** *(UML developer)*
- **Ismail Rachid** *(Something)*
     
----
                
###FlowChart

```flow
st=>start: Boot up Raspberry PI
op0=>operation: "main.py" starts
op=>operation: "main.py" is waiting for input
cond=>condition: Is the buttun pressed - Yes or No?
e=>end: Begin test & Print on display

st->op0->op->cond
cond(yes)->e
cond(no)->op
```

###Sequence Diagram
insert here
###UML Diagrams
insert here
```

###End
