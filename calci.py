import PySimpleGUI as sg

#Layout                                                     
layout = [[sg.Txt(''  * 10)],                      
          [sg.Text('', size=(15, 1), font=('Chesterish', 16), text_color='black', key='input')],
          [sg.Txt(''  * 10)],
          [sg.ReadFormButton('('), sg.ReadFormButton(')'), sg.ReadFormButton('AC'), sg.ReadFormButton('DEL')],
          [sg.ReadFormButton('7'), sg.ReadFormButton('8'), sg.ReadFormButton('9'), sg.ReadFormButton('÷')],
          [sg.ReadFormButton('4'), sg.ReadFormButton('5'), sg.ReadFormButton('6'), sg.ReadFormButton('x')],
          [sg.ReadFormButton('1'), sg.ReadFormButton('2'), sg.ReadFormButton('3'), sg.ReadFormButton('-')],
          [sg.ReadFormButton('.'), sg.ReadFormButton('0'), sg.ReadFormButton('='), sg.ReadFormButton('+')],
          [sg.ReadFormButton('MOD')],
          ]

# Set PySimpleGUI
form = sg.FlexForm('DJSCE_CALCI', default_button_element_size=(5, 2), auto_size_buttons=False, grab_anywhere=False)
form.Layout(layout)

# Set Operations
Equal = ''
List_Op_Error =  ['+','-','*','/','(']

# Loop
while True:
    button, value = form.Read()                            # call GUI
    
    # Press Button
    if button is 'AC':
        Equal = ''
        form.FindElement('input').Update(Equal)
    elif button is 'DEL':
        Equal = Equal[:-1]
        form.FindElement('input').Update(Equal)
    elif len(Equal) == 16 :
        pass
    elif str(button) in '1234567890+-().':
        Equal += str(button)
        form.FindElement('input').Update(Equal) 
    elif button is 'x':
        Equal += '*'
        form.FindElement('input').Update(Equal)
    elif button is '÷':
        Equal += '/'
        form.FindElement('input').Update(Equal)
    elif button is 'MOD':
        Equal += '%'
        form.FindElement('input').Update(Equal)
       
   # Process Conditional
    elif button is '=':
        # Error Case
        for i in List_Op_Error :  
            if '*' is Equal[0] or '/' is Equal[0] or ')' is Equal[0]  or i is Equal[-1]:   # Check Error Case
                Answer = "Error Operation" 
                break
            elif '/0' in Equal or '*/' in Equal or '/*' in Equal :
                Answer = "Error Operation" 
                break
            elif '(' in Equal :
                if ')' not in Equal :
                    Answer = "Error Operation" 
                    break   
            elif '(' not in Equal:
                if ')' in Equal:
                    Answer = "Error Operation" 
                    Break

    # Calculate Case    
        else :
            Answer = str("%0.7f" %(eval(Equal)))                         # eval(Equal)  
            if '.0' in Answer:
                Answer = str(int(float(Answer)))                         # convert float to int
        form.FindElement('input').Update(Answer)                         
        Equal = Answer

    elif button is 'Quit'  or button is None:                            # QUIT Program
        break
