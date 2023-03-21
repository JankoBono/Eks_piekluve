# importē bibliotēkas un failus
import PySimpleGUI as sg
import datu_inters, paroles_logs, tabula
import sqlite3

conn = sqlite3.connect('data.db')
cur = conn.cursor()

# izveiodo tabulas datubāzē, ja tādas jau neeksistē
cur.execute("""CREATE TABLE IF NOT EXISTS dati(
            darba_id INTEGER PRIMARY KEY,
            summa float,
            drops text,
            daudzums integer
            )""")
cur.execute("""CREATE TABLE IF NOT EXISTS darba_koef(
            id INTEGER PRIMARY KEY,
            saraksta_id INTEGER,
            drops text,
            koef_darbam float,
            FOREIGN KEY (saraksta_id) REFERENCES users(darba_id)
            )""")

# izkārtojums logam
layout = [
    [sg.Text("Ievadi darba nr:"), sg.I(key = '-ID-',enable_events=True,size=(5, 1)),sg.Text("Ievadi savākto summu:"), sg.I(key = '-SUMMA-',enable_events=True,size=(5, 1))], 
    [sg.Text("Izvēlies darbību:"),sg.OptionMenu(values = ['Ēvelēšana', 'Garināšana', 'Zāģēšana'],default_value = 'Ēvelēšana', key = "-DROPS-"),sg.Text("Ievadi daudzumu:"),sg.I(key = '-DAUDZUMS-', size = (5,1))],
    [sg.B('Ievadīt'),sg.B('Tabula'),sg.Exit()],
    [sg.T('Ieraksti darba nr, kuru vēlies dzēst'),sg.I(key = '-DZEST_ID-',enable_events=True,size=(5, 1)),sg.B('Int ID dzēst')],
    [sg.Text("ID:"),sg.I(key = '-MAINIT_ID-',enable_events=True,size=(5, 1)),sg.Text("Jaunā summa:"),sg.I(key = '-UZ_KO-',enable_events=True,size=(5, 1)),sg.B('Int ID maiņai')]
]

window = sg.Window("Gabaldarbinieku algas kopotājs", layout)   

vajag_autorizeties=0

# cikls loga nepārtrauktas darbības nodrošināšanai
while True:

    # pārbauda autorizāciju
    if vajag_autorizeties ==0:
        paroles_logs.protect()
        vajag_autorizeties=1
    event, values = window.read()
    
    # iziet no programmas
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    # ievada datus un pārbauda pareizos datu tipus ievades logiem
    if event == 'Ievadīt':
        if values['-DAUDZUMS-'] == "" or values['-ID-'] == "" or values['-SUMMA-'] == "":
            sg.popup("ievadā ir tukšs lauks")
        if values['-ID-'].isdigit() == False or values['-DAUDZUMS-'].isdigit() == False:
            sg.popup("ievads nav aizpildīts pareizi!")
        else:
            datu_inters.ievieto_darbu(values['-ID-'],values['-SUMMA-'],values['-DROPS-'],values['-DAUDZUMS-'])
            sg.popup("darbs ievietots!")
    
    # nodrošina summas pareizo datus ievades tipu
    if event == '-SUMMA-' and values['-SUMMA-']:
        in_as_float = float(values['-SUMMA-'])

    if event == '-UZ_KO-' and values['-UZ_KO-']:
                in_as_float = float(values['-UZ_KO-'])

    # izveido tabulu
    if event == 'Tabula':
        tabula.create()

    # izdzēš datus pēc darba ID
    if event == 'Int ID dzēst':
        if values['-DZEST_ID-'] == "":
            sg.popup("ievadā ir tukšs lauks")

        else:
            dzest_id=values['-DZEST_ID-']
            datu_inters.izdzest_darbu(dzest_id)

    # maina summu konkurētam darba ID
    if event == 'Int ID maiņai':
        if values['-MAINIT_ID-'] == "" or values['-UZ_KO-']=="":
            sg.popup("ievadā ir tukšs lauks")
        else:
            mainit_id=values['-MAINIT_ID-']
            uz_ko=values['-UZ_KO-']
            datu_inters.izmaina_summu(mainit_id,uz_ko)
            
# aizver logu un beidz datubāzes procesus
conn.commit()
conn.close()
window.close()