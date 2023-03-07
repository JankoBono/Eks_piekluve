import PySimpleGUI as sg
import datu_inters
import tabula

class Logs:

    layout = [
        [sg.Text("Ievadi darba nr:"), sg.I(key = '-ID-',enable_events=True,size=(5, 1)),sg.Text("Ievadi savāto summu:"), sg.I(key = '-SUMMA-',enable_events=True,size=(5, 1))], 
        [sg.Text("Izvēlies darbību:"),sg.OptionMenu(values = ['Ēvelēšana', 'Garināšana', 'Zāģēšana'],default_value = 'Ēvelēšana', key = "-DROPS-"),sg.Text("Ievadi daudzumu:"),sg.I(key = '-DAUDZUMS-', size = (5,1))],
        [sg.T('Ievadīts: ')], [sg.T(key='-OUT_GAR-'), sg.T(key='-OUT_PLAT-'),sg.T(key='-OUT_DROPS-'),sg.T(key='-OUT_DAUDZ-')],
        [sg.B('Ievadīt'),sg.B('Tabula'),sg.Exit()]
    ]

    window = sg.Window("gmgm", layout)   


    while True:
        event, values = window.read()
        # print(event, values)  # izdrukā bibliotēkas vērtības
        
        if event == sg.WIN_CLOSED or event == 'Exit':
            break
        if event == 'Ievadīt':
            window['-OUT_GAR-'].update(values['-ID-'])
            window['-OUT_PLAT-'].update(values['-SUMMA-'])
            window['-OUT_DROPS-'].update(values['-DROPS-'])
            window['-OUT_DAUDZ-'].update(values['-DAUDZUMS-'])
            datu_inters.ievieto_darbu(values['-ID-'],values['-SUMMA-'],values['-DROPS-'],values['-DAUDZUMS-'])
            sg.popup("darbs ievietots!")
        # if event == '-GARUMS-' and values['-GARUMS-']:
        #     in_as_float = float(values['-GARUMS-'])
        #     if float(values['-GARUMS-']) == 0:
        #         window['-GARUMS-'].update('1')
        # if event == '-PLATUMS-' and values['-PLATUMS-']:
        #     in_as_float = float(values['-PLATUMS-'])
        #     if float(values['-PLATUMS-']) == 0:
        #         window['-PLATUMS-'].update('1')
        if event == 'Tabula':
            tabula.create()

    window.close()