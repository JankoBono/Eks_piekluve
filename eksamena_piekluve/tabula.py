import PySimpleGUI as sg
import datu_inters

import operator

def dabu_datus():
    darba_dati = datu_inters.parbaude()
    return darba_dati

def sort_table(table, col_clicked):
    table = sorted(table, key=operator.itemgetter(col_clicked))
    return table

def create():
    darbu_masivs = dabu_datus()
    headings = ['Darba id', 'Summa', 'Darbs', 'Daudzums']

    darba_datu_layout = [
        [sg.Table(values=darbu_masivs, headings=headings, max_col_width=35,
                    auto_size_columns=True,
                    display_row_numbers=True,
                    justification='right',
                    num_rows=10,
                    enable_events=True,
                    enable_click_events=True, 
                    key='-TABULA-',
                    row_height=35,
                    tooltip='darbu tabula'
                 )
        ]
    ]

    tabula = sg.Window("darba datu logs", 
    darba_datu_layout, modal=True)

    while True:
        event, values = tabula.read()
        if event == "Exit" or event == sg.WIN_CLOSED:
            break
        if event[2][0] == -1 and event[2][1] != -1:
            col_num_clicked = event[2][1]
            new_table = sort_table(darbu_masivs, col_num_clicked)
            tabula['-TABULA-'].update(new_table)
        
        
    tabula.close()