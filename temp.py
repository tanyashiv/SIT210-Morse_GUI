# Import necessary modules
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel,QLineEdit, QPushButton
import sys

import RPi.GPIO as GPIO  #Import the RPi.GPIO library for controlling Raspberry Pi GPIO pins
import time  #Import time module for handling time-related functions

GPIO.setmode(GPIO.BOARD)  #Set the GPIO mode to use the physical pin numbering

GPIO.setup(19, GPIO.OUT)  #Configure GPIO pin 19 as output pin

#Function to emit a short Morse code signal (dot)
def dot():
  GPIO.output(19,GPIO.HIGH)  #Turn on LED
  time.sleep(300)  #Keep LED on for 300ms
  GPIO.output(19,GPIO.LOW)  #Turn off LED
  time.sleep(900)  #Delay after LED is off for 900ms

  
#Function to emit a long Morse code signal (dash)
def dash():
  GPIO.output(19, GPIO.HIGH)  #Turn on LED
  time.sleep(900)  #Keep LED on for 900ms
  GPIO.output(19,GPIO.LOW)  #Turn off LED
  time.sleep(900)  #Delay after LED is off for 900ms

#Function to convert a character to its Morse code representation
def create_morse(alpha):
    if(alpha=='a' or alpha=='A'):
        dot()
        dash()
          
    elif(alpha=='b' or alpha=='B'):
        dash()
        dot()
        dot()
        dot()
      
    elif(alpha=='c' or alpha=='C'):
      dash()
      dot()
      dash()
      dot()
    elif(alpha=='d' or alpha=='D'):
  
      dash()
      dot()
      dot()
    elif(alpha=='e' or alpha=='E'):
      dot()
    elif(alpha=='f' or alpha=='F'):
      dot()
      dot()
      dash()
      dot()
    elif(alpha=='g' or alpha=='G'):
      dash()
      dash()
      dot()
    elif(alpha=='h' or alpha=='H'):
      dot()
      dot()
      dot()
      dot()
    elif(alpha=='i' or alpha=='I'):
      dot()
      dot()
    elif(alpha=='j' or alpha=='J'):
      dot()
      dash()
      dash()
      dash()
    elif(alpha=='k' or alpha=='K'):
      dash()
      dot()
      dash()
    elif(alpha=='l' or alpha=='L'):
      dot()
      dash()
      dot()
      dot()
    elif(alpha=='m' or alpha=='M'):
      dash()
      dash()
    elif(alpha=='n' or alpha=='N'):
      dash()
      dot()
    elif(alpha=='o' or alpha=='O'):
      dash()
      dash()
      dash()
    elif(alpha=='p' or alpha=='P'):
      dot()
      dash()
      dash()
      dot()
    elif(alpha=='q' or alpha=='Q'):
      dash()
      dash()
      dot()
      dash()
    elif(alpha=='r' or alpha=='R'):
      dot()
      dash()
      dot()
    elif(alpha=='s' or alpha=='S'):
      dot()
      dot()
      dot()
    elif(alpha=='t' or alpha=='T'):
     dash()
    elif(alpha=='u' or alpha=='u'):
      dot()
      dot()
      dash()
    elif(alpha=='v' or alpha=='V'):
      dot()
      dot()
      dot()
      dash()
    elif(alpha=='w' or alpha=='W'):
      dot()
      dash()
      dash()
    elif(alpha=='x' or alpha=='X'):
      dash()
      dot()
      dot()
      dash()
    elif(alpha=='y' or alpha=='Y'):
      dash()
      dot()
      dash()
      dash()
    elif(alpha=='z' or alpha=='Z'):
      dash()
      dash()
      dot()
      dot()

#Function to handle the "Upload" button click event
def handle_upload():
  name=win.textbox.text()  #Get the value of name from the text box


#Limit the input to a maximum of 12 characters
  if len(name) > 12:
      name = name[:12]  
#Convert each character of the name to Morse code
  for char in name:
      create_morse(char) 
  win.textbox.clear()   #Clear the text input field

app = QApplication([])  # Create the PyQt application
win = QMainWindow()  # Create the main window
#Set the title, position and size of the main window
win.setWindowTitle("Blink Morse Code")  
win.resize(500,200)
win.move(400,200)

#Create a label to instruct the user to enter their name
label1=QLabel(win)
label1.setText("Enter Your Name")

# Create a text input field and adjust its position and size
win.textbox = QLineEdit(win)
win.textbox.move(40, 40)
win.textbox.resize(250,50)

# Create an "Upload" button and connect it to the handle_upload function
buttonUpload = QPushButton("Upload", win)
buttonUpload.move(80,100)
buttonUpload.clicked.connect(handle_upload)

win.show()  #Show the main window

sys.exit(app.exec_())
