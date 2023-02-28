import PySimpleGUI as sg

headings = ['Detaļas izmēri', 'Darbība', ['Ēvelēšana', 'Garināšana', 'Zāģēšana'], 'Daudzums', 'Koeficients', 'Gala summa']

class Logs:

    layout = [
        [sg.Text("Ievadi izmērus:"), sg.I(key = '-GARUMS-'), sg.I(key = '-PLATUMS-')],
        [sg.T('Ievadīts: ')], [sg.T(key='-OUT_GAR-'), sg.T(key='-OUT_PLAT-')],
        [sg.B('Ievadīt'),sg.Exit()]
    ]

    window = sg.Window("gmgm", layout)   


    while True:
        event, values = window.read()
        # print(event, values)  # izdrukā bibliotēkas vērtības
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Ievadīt':
            window['-OUT_GAR-'].update(values['-GARUMS-'])
            window['-OUT_PLAT-'].update(values['-PLATUMS-'])

    window.close()