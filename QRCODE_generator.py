import PySimpleGUI as sg
import qrcode 
layout = [
    [sg.Text('Enter the text or URL to convert to QR code:')],
    [sg.Input(key='data')],
    [sg.Button('GENERATE'),sg.Button('EXIT')],
    [sg.Image(key='output')]

]
window = sg.Window('QRCODE GENERATOR',layout)

while True:
    event,values = window.read()
    if event == sg.WIN_CLOSED or event == 'EXIT':
       break
    elif event == 'GENERATE':
        qc = qrcode.make(values['data'])
        qc.save('qr_code.png')
        window['output'].update('qr_code.png')
window.close()

