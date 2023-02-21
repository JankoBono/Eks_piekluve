import PySimpleGUI as sg

headings = ['Detaļas izmēri', 'Darbība', 'Daudzums', 'Koeficients', 'Gala summa']

layout = [[sg.text("Ievadi darbību:"), sg.Input(key='-DARBIBA-', size=(20, 1))]]