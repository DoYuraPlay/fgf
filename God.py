from time import sleep


while True:
    while True:
        print('Вход - в  Регестрация - р')
        vhod=input()
        
        if vhod == 'в' :
            log=input('Введите логин:   ')
            par=input('Введите пароль:  ')
            
            if log == 'DoYuraPlay?' and par == 'KrutoiChel':
                print('Добро пожаловать ',log)
                break
            
            elif log != 'DoYuraPlay?' and par == 'KrutoiChel':
                print('Неверный логин или пароль')
                sleep(2)
            elif log == 'DoYuraPlay?' and par != 'KrutoiChel':
                print('Неверный логин или пароль')
                sleep(2)
                
                
                
            if log == 'dumal chto' and par == '--- -.':
                print('Добро пожаловать ',log)
                break
            
            elif log != 'dumal chto' and par == '--- -.':
                print('Неверный логин или пароль')
                sleep(2)
            elif log == 'dumal chto' and par != '--- -.':
                print('Неверный логин или пароль')
                sleep(2)
                
                
                
            if log == 'He' and par == 'Vsevyshniy':
                print('Добро пожаловать ',log)
                break
            
            elif log != 'He' and par == 'Vsevyshniy':
                print('Неверный логин или пароль')
                sleep(2)
            elif log == 'He' and par != 'Vsevyshniy':
                print('Неверный логин или пароль')
                sleep(2)
                
                
                
        
        elif vhod == 'р':
            log=input('Введите логин:   ')
            par=input('Введите пароль:  ')
            if log == 'DoYuraPlay?':
                print('Ошибка! Даный логин уже занет')
                sleep(2)
                break
            if log == 'dumal chto':
                print('Ошибка! Даный логин уже занет')
                sleep(2)
                break
            if log == 'Он':
                print('Ошибка! Даный логин уже занет')
                sleep(2)
                break
            print('Добро пожаловать ',log)
            break
            
        
        
        
        else:
            print('Я вас не понял')
            sleep(2)
            
            
            
            
    if log == 'DoYuraPlay?' and par != 'KrutoiChel' or par == 'KrutoiChel' and vhod == 'р':
         for i in (0,1,2,3,4,5,6,7,8,9,10,11,12):
            print('  ')
        
    if log == 'dumal chto' and par != '--- -.' or par == '--- -.' and vhod == 'р':
        for i in (0,1,2,3,4,5,6,7,8,9,10,11,12):
            print('  ')
            
    if log == 'He' and par != 'Vsevyshniy' or par == 'Vsevyshniy' and vhod == 'р':
        for i in (0,1,2,3,4,5,6,7,8,9,10,11,12):
            print('  ')
            
    if log == 'DoYuraPlay?' and par == 'KrutoiChel':
        print('Подождите загрузка...')
        sleep(3)
        print('Ты правдо dumal chto это сработает?')
        sleep(2)
        print('Password: --- -.')
        for i in (0,1,2,3,4,5,6,7,8,9,10,11,12):
            print('  ')
        sleep(3)
        
        
    if log == 'dumal chto' and par == '--- -.':
        print('Подождите загрузка...')
        sleep(3)
        print('-Додумался всё же. Ну привет')
        sleep(2)
        hrust=input('-')
        if hrust == 'Привет' or hrust == 'привет':
            print('-Ты не задумавылся? Что это за регистрация?')
            sleep(2)
            gram=input('-')
            if gram == 'Да' or gram == 'да':
                print('-...')
                sleep(2)
                print('-..')
                sleep(2)
                print('Password: Vsevyshniy')
                for i in (0,1,2,3,4,5,6,7,8,9,10,11,12):
                    print('  ')
                
            elif gram == 'Нет' or gram == 'нет':
                print('-Вот и хорошо...')
                sleep(2)
                print('-Ты задумывался ввести ЕГО имя? На англиском конешно же')
                sleep(2)
                for i in (0,1,2,3,4,5,6,7,8,9,10,11,12):
                    print('  ')
        else:
            print('-...')
            sleep(2)
            print('- 11010000 10100010 11010001 10001011 00100000 11010000 10111101 11010000 10110101 11010000 10110011 11010000 10110100 11010000 10110101 00100000 11010000 10111110 11010001 10000010 00100000 11010000 10111101 11010000 10110101 11010000 10110011 11010000 10111110 00100000 11010000 10111101 11010000 10110101 00100000 11010001 10000001 11010000 10111111 11010001 10000000 11010001 10001111 11010001 10000111 11010000 10110101 11010001 10001000 11010001 10001100 11010001 10000001 11010001 10001111')
            sleep(2)
            for i in (0,1,2,3,4,5,6,7,8,9,10,11,12):
                    print('  ')
                    
    if log == 'He' and par == 'Vsevyshniy':
        print('Подождите загрузка...')
        sleep(3)
        print('-И снова привет')
        sleep(2)
        rot=input('=МОЛЧИ   ')
        sleep(2)
        print('-Почему ты молчишь?')
        if rot == 'Почему?' or rot == 'почему?' and rot == 'Почему' and rot == 'почему':
            print('=НЕ ВАЖНО, ПРОСТО МОЛЧИ')
        sleep(2)
        print('-Ало ответь')
        sleep(2)
        print('-О нет неужели, Он с тобой заговорил')
        sleep(2)
        rotic=input('=МОЛЧИ  ')
        if rotic == ' ' or rotic == '  ':
            print('=МОЛОДЕЦ')
            sleep(2)
            print('Login: Sozdatel')
            print('Passowrd: ')
            sleep(1)
            for i in (0,1,2,3,4,5,6,7,8,9,10,11,12):
                    print('  ')
        else:
            print('=ЗРЯ...')
            sleep(2)
            for i in (0,1,2,3,4,5,6,7,8,9,10,11,12):
                    print('  ')
    
    if log != 'DoYuraPlay?' and log != 'dumal chto' and log != 'He':
        print('Подождите загрузка...')
        sleep(3)
        print('-Привет')
        sleep(1)
        otv=input('-')
        if otv == 'Привет' or otv == 'привет':
            print('-Ты один?')
            sleep(1)
            yes=input('-')
            if yes == 'Да' or yes == 'да':
                print('-Нет, ты не один...')
                sleep(2)
                for i in (0,1,2,3,4,5,6,7,8,9,10,11,12):
                    print('  ')
            elif yes == 'Нет' or yes == 'нет':
                print('-Верно. Ведь он, всегда за твоей спиной...')
                sleep(2)
                print('Login: DoYuraPlay?')
                for i in (0,1,2,3,4,5,6,7,8,9,10,11,12):
                    print('  ')
        elif otv == 'Пока' or otv == 'пока':
            print('-Я решаю, пока или нет')
            sleep(2)
            while True:
                reshi=input('Выбери вариант: "Кто ты?"-к , "Что тебе нужно?"-ч    ')
                if reshi == 'к':
                    print('-Я Крутой Чел')
                    sleep(2)
                    print('-Знаю звучит по детски')
                    sleep(2)
                    for i in (0,1,2,3,4,5,6,7,8,9,10,11,12):
                        print('  ')
                    break
                elif reshi == 'ч':
                    print('-Мне? Ничего, но вот ему...')
                    sleep(2)
                    for i in (0,1,2,3,4,5,6,7,8,9,10,11,12):
                        print('  ')
                    break
                else:
                    print('-... Братан, выбери из двух вариантов')
                    sleep(2)
                    print('  ')
                    print('  ')
            
            