#guess number gui by Enzo_a_person 
import PySimpleGUI as sg
import random 

#setting up variables
menu_def = [['File', ['start', 'about', 'Exit', 'options'  ]] ]

number = ['1','2','3','4','5','6','7','8','9','10']

title_screen = [[sg.Menu(menu_def, )], [sg.Text('welcome to guess the number go to the file menu to start a game')] ]

game_play = [[sg.Text('try to guess my number its in between 1 or 10')], [sg.InputText()], [sg.Submit(),]]

window = sg.Window('guess the number', title_screen)

#summon windows
event, values = window.read()    

#main game loop
if event == 'about':      
    sg.popup('About this program', 'Version 1.0', 'Created by Enzo_a_person')
if event == 'Exit':
    exit()
if event == 'options':
    sg.popup('this has not been added yet')
if event == 'start':
    window.close()
    n = random.choice(number) #creates a number between 0 or 10
    window = sg.Window('pick a number', game_play)
    print (n)  #cheet code
    event, values = window.read()
    window.close()
    if values[0] == n:  #you win
        print ("you win")
        sg.popup('you have won')
    if values[0] != n: # you lose
        print ("you lose")
        sg.popup('you have lost')

    