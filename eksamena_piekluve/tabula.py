# importē bibliotēkas un failus
import PySimpleGUI as sg
import datu_inters
import operator

# iegūst datus no datubāzes
def dabu_datus():
    darba_dati = datu_inters.parbaude()
    return darba_dati

# sakārto tabulas datus pēc noteiktas kolonas
def sort_table(table, col_clicked):
    table = sorted(table, key=operator.itemgetter(col_clicked))
    return table

# izveido tabulas logu
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

    # cikls loga nepārtrauktas darbības nodrošināšanai
    while True:
        event, values = tabula.read()

        # beidz programmas darbību
        if event == "Exit" or event == sg.WIN_CLOSED:
            break

        # nolasa kura kolona ir noklikšķināta, lai varētu sakārtot datus
        if event[2][0] == -1 and event[2][1] != -1:
            col_num_clicked = event[2][1]
            new_table = sort_table(darbu_masivs, col_num_clicked)
            tabula['-TABULA-'].update(new_table)
        
    # aiver tabulas logu
    tabula.close()