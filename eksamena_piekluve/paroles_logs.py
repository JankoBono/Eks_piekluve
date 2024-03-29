# importē bibliotēkas
import PySimpleGUI as sg
import hashlib

def protect():

        # izkārtojums logam
        layout = [
                [sg.Text("Ievadi lietotājvārdu:"), sg.Input(key='-EMAIL-', do_not_clear=True, size=(30, 1))],
                [sg.Text('Ievadi paroli:', size=(15, 1)), sg.InputText('', key='-PASSWORD-', password_char='*', size=(15, 1))],
                [sg.Button("Iesniegt"),sg.Button("Iziet")]
                ]

        password_window = sg.Window('Gabaldarbinieku algas kopotājs', layout, modal=True)

        # pārbauda paroli
        def verify_password(password):
                hash = '8b15670ea8fb9647e783263380bbbadf0cfa543a11dd7140fecf34cc4b710266'
                password_utf = password.encode('utf-8')
                password_hash = hashlib.sha256(password_utf).hexdigest()
                if hash == password_hash:
                        return True
                return False

        # pārbauda e-pasta adresi
        def verify_email_address(email_address):
                user_email_addresses = ['janis', 'kokle', 'kubiks']
                if email_address in user_email_addresses:
                        return True
                return False

        # cikls loga nepārtrauktas darbības nodrošināšanai
        while True:
                event, values = password_window.read()

                # beidz programmas darbību
                if event == "Iziet" or event == sg.WIN_CLOSED:
                        exit()

                # pārbauda iesniegtos autorizācijas datus
                if event == 'Iesniegt':
                        email_input_value = values['-EMAIL-']
                        password_input_value = values['-PASSWORD-']
                        if verify_password(password_input_value) and verify_email_address(email_input_value):
                                break
                        else:
                                sg.popup("nav ievadīta pareiza parole vai lietotājvārds")
                                continue

        # aizver autorizācijas logu
        password_window.close()
