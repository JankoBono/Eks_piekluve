import PySimpleGUI as sg
import datu_inters, paroles_logs, tabula
import sqlite3

conn = sqlite3.connect('data.db')
cur = conn.cursor()

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

layout = [
    [sg.Text("Ievadi darba nr:"), sg.I(key = '-ID-',enable_events=True,size=(5, 1)),sg.Text("Ievadi savākto summu:"), sg.I(key = '-SUMMA-',enable_events=True,size=(5, 1))], 
    [sg.Text("Izvēlies darbību:"),sg.OptionMenu(values = ['Ēvelēšana', 'Garināšana', 'Zāģēšana'],default_value = 'Ēvelēšana', key = "-DROPS-"),sg.Text("Ievadi daudzumu:"),sg.I(key = '-DAUDZUMS-', size = (5,1))],
    [sg.B('Ievadīt'),sg.B('Tabula'),sg.Exit()],
    [sg.T('Ieraksti darba nr, kuru vēlies dzēst'),sg.I(key = '-DZEST_ID-',enable_events=True,size=(5, 1)),sg.B('Int ID dzēst')],
    [sg.Text("ID:"),sg.I(key = '-MAINIT_ID-',enable_events=True,size=(5, 1)),sg.Text("Jaunā summa:"),sg.I(key = '-UZ_KO-',enable_events=True,size=(5, 1)),sg.B('Int ID maiņai')]
]

window = sg.Window("Gabaldarbinieku algas kopotājs", layout)   

vajag_autorizeties=0

while True:
    if vajag_autorizeties ==0:
        paroles_logs.protect()
        vajag_autorizeties=1
    event, values = window.read()
    
    if event == sg.WIN_CLOSED or event == 'Exit':
        break

    if event == 'Ievadīt':
        if values['-DAUDZUMS-'] == "" or values['-ID-'] == "" or values['-SUMMA-'] == "":
            sg.popup("ievadā ir tukšs lauks")
        if values['-ID-'].isdigit() == False or values['-DAUDZUMS-'].isdigit() == False:
            sg.popup("ievads nav aizpildīts pareizi!")
        else:
            datu_inters.ievieto_darbu(values['-ID-'],values['-SUMMA-'],values['-DROPS-'],values['-DAUDZUMS-'])
            sg.popup("darbs ievietots!")
        
    if event == '-SUMMA-' and values['-SUMMA-']:
        in_as_float = float(values['-SUMMA-'])

    if event == 'Tabula':
        tabula.create()

    if event == 'Int ID dzēst':
        if values['-DZEST_ID-'] == "":
            sg.popup("ievadā ir tukšs lauks")

        else:
            dzest_id=values['-DZEST_ID-']
            datu_inters.izdzest_darbu(dzest_id)

    if event == '-UZ_KO-' and values['-UZ_KO-']:
            in_as_float = float(values['-UZ_KO-'])

    if event == 'Int ID maiņai':
        if values['-MAINIT_ID-'] == "" or values['-UZ_KO-']=="":
            sg.popup("ievadā ir tukšs lauks")
        else:
            mainit_id=values['-MAINIT_ID-']
            uz_ko=values['-UZ_KO-']
            datu_inters.izmaina_summu(mainit_id,uz_ko)
    
conn.commit()
conn.close()
window.close()
