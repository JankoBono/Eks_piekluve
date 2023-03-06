import PySimpleGUI as sg

class Logs:

    layout = [
        [sg.Text("Ievadi izmērus:"), sg.I(key = '-GARUMS-',enable_events=True,size=(5, 1)), sg.I(key = '-PLATUMS-',enable_events=True,size=(5, 1))], 
        [sg.Text("Izvēlies darbību:"),sg.OptionMenu(values = ['Ēvelēšana', 'Garināšana', 'Zāģēšana'],default_value = 'Ēvelēšana', key = "-DROPS-"),sg.Text("Ievadi daudzumu:"),sg.I(key = '-DAUDZUMS-', size = (5,1))],
        [sg.T('Ievadīts: ')], [sg.T(key='-OUT_GAR-'), sg.T(key='-OUT_PLAT-'),sg.T(key='-OUT_DROPS-'),sg.T(key='-OUT_DAUDZ-')],
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
            window['-OUT_DROPS-'].update(values['-DROPS-'])
            window['-OUT_DAUDZ-'].update(values['-DAUDZUMS-'])
        if event == '-GARUMS-' and values['-GARUMS-']:
            in_as_float = float(values['-GARUMS-'])
            if float(values['-GARUMS-']) == 0:
                window['-GARUMS-'].update('1')
        if event == '-PLATUMS-' and values['-PLATUMS-']:
            in_as_float = float(values['-PLATUMS-'])
            if float(values['-PLATUMS-']) == 0:
                window['-PLATUMS-'].update('1')

    window.close()
