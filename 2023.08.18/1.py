def strong_password(password: str) -> bool:
    border_checkpoint = {'big_r': False, 'lower_r': False, 'num_two': 0, 'other_signs': False}
    if len(password) < 8:
        return False
    else:
        for simvol in password:
            if (ord(simvol) >= 65 and ord(simvol) <= 90):
                border_checkpoint['big_r'] = True
                break
        for simvol in password:
            if (ord(simvol) >= 97 and ord(simvol) <= 122):
                border_checkpoint['lower_r'] = True
                break
        if border_checkpoint['big_r'] == True and border_checkpoint['lower_r'] == True:
            for simvol in password:
                if (ord(simvol) >= 48 and ord(simvol) <= 57):
                    border_checkpoint['num_two'] += 1
            if border_checkpoint['num_two'] >= 2:
                for simvol in password:
                    if (ord(simvol) >= 32 and ord(simvol) <= 47) or (ord(simvol) >= 58 and ord(simvol) <= 64) or (ord(simvol) >= 91 and ord(simvol) <= 96) or (ord(simvol) >= 123 and ord(simvol) <= 126):
                        border_checkpoint['other_signs'] = True
                        break
                return border_checkpoint['other_signs']
            else:
                return False
        else:
            return False
            
#C:\Users\Кеша\Desktop\my_life\Б. Прогаммирование\Top-Piton\HomeWork_Python_TOP\HW\2023.08.18>python -i 1.py
#>>> strong_password('aP3:kD_l3')
#True
#>>> strong_password('password')
#False
#>>>