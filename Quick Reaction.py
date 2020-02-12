from gpiozero import LED,Button
from time import sleep
from random import uniform
from sys import exit
import time 




scoreOne = 0
scoreTwo = 0

def pressed(button):
    
    global scoreOne 
    global scoreTwo
    
    if button.pin.number == 14:
        
        print(left_name + ' won the game ' + ' reaction time was ' + str(time.clock()-now))
        scoreOne +=1
        
    elif button.pin.number == 15:
        
        print(right_name + ' won the game ' + ' reaction time was '+ str(time.clock() - now))
        scoreTwo +=1
        
   
    

led = LED(4)


    
left_name  = input(' left player name is ')
right_name = input(' right player name is ')
rounds = int(input(' The number of round(s) '))

right_button = Button(15)
left_button  = Button(14)

right_button.when_pressed = pressed
left_button.when_pressed  = pressed

for i in range(0,rounds):      
    print("Round", i,"get ready","\n")
    
    led.on()
    sleep(uniform(5,10))
    
    led.off()
    
    
    now = time.clock()

    right_button.when_released = led.on
    left_button.when_released = led.on

    sleep(uniform(5,10))
    led.off()

    
led.off()
print("FINAL SCORE",left_name  + ' ' + str(scoreOne) + ' - ' + right_name + ' ' + str(scoreTwo))
    

   
    


    
   
  
   
