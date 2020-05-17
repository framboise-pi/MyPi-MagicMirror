# MyPiMagicMirror [MPMM]
Magic Mirror in python for Raspberry Pi

[EN]
Magic Mirror is a wonderful idea,
it uses pretty much of CPU/RAM,
so the meaning here is to get a version that could run on a Raspberry Zero;
by using python we should get to the point.

[FR]
Le Magic Mirror est une idée géniale,
mais à la première installation sur un Raspberry Zero,
j'ai été surpris de la charge CPU/RAM pour un simple affichage de page web.
Le but ici est de proposer une version Raspberry en python,
qui sera testée sur Raspberry Zero (développé sur un 3B).

------------------------------------------------

#### HOW TO QUIT MPMM
  - with Escape keyboard button
  
### FILES - all are needed
  - MPMM_config.py -=- main configuration file
  - MPMM_sensehat.py -=- module for sensehat, with some configuration inside
  - MPMM_module_words.py -=- module for random words
  - MyPiMagicMirror.py -=- main file

------------------------------------------------
## WHAT WILL DISPLAY ?
  - On your Sensehat
      - random 
        - LED picture from python file
        - temperature in a message, background color corresponding to a temperature scale (from blue to red)
  - On your Magic Mirror
    - top of the Mirror :
      - clock with date, inspired from Magic Mirror 2
      - from sensehat : temperature and pression
    - center of the Mirror :
      - modules
        - Moon - pictures to show current phase of the moon ( I made pictures I won't release for free, but will modify with free licenses pictures for you on github)
    - footer of the Mirror :
        - Words - random words from a python file to make a sentence. Inspired from Compliments/Magic Mirror 2
-------------------------------------
- This version don't need/use internet connection.
- This version don't use a php/navigator/server, it works with Tkinter
Only python involved
    
  - [update] picture of MPMM working with Sensehat -
-------------------------------------
### Give support ! ( a chocolat viennois break | help me get sensors and Raspberry hardware)
[![paypal](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=E79JA29LBLTAE&source=url)
------------------------------------------------
> I'm currently coding MPMM (May 2020); installation help etc. will be added later on
