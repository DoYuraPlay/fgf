from time import sleep
import random


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
                print('  ')
                print('  ')
            elif log == 'DoYuraPlay?' and par != 'KrutoiChel':
                print('Неверный логин или пароль')
                sleep(2)
                print('  ')
                print('  ')
                
                
                
            if log == 'dumal chto' and par == 'ON':
                print('Добро пожаловать ',log)
                break
            
            elif log != 'dumal chto' and par == 'ON':
                print('Неверный логин или пароль')
                sleep(2)
                print('  ')
                print('  ')
            elif log == 'dumal chto' and par != 'ON':
                print('Неверный логин или пароль')
                sleep(2)
                print('  ')
                print('  ')
                
                
                
            if log == 'He' and par == 'Vsevyshniy':
                print('Добро пожаловать ',log)
                break
            
            elif log != 'He' and par == 'Vsevyshniy':
                print('Неверный логин или пароль')
                sleep(2)
                print('  ')
                print('  ')
            elif log == 'He' and par != 'Vsevyshniy':
                print('Неверный логин или пароль')
                sleep(2)
                print('  ')
                print('  ')
                
                   
            if log == 'Sozdatel' and par == 'Nividin':
                print('Добро пожаловать ',log)
                break
            
            elif log != 'Sozdatel' and par == 'Nividin':
                print('Неверный логин или пароль')
                sleep(2)
                print('  ')
                print('  ')
            elif log == 'Sozdatel' and par != 'Nividin':
                print('Неверный логин или пароль')
                sleep(2)
                print('  ')
                print('  ')
                
            
            if log !='He' and log != 'dumal chto' and log != 'DoYuraPlay?' and par != 'Vsevyshniy' and par != 'ON' and par != 'KrutoiChel'  :
                print('Даный акаунт не создан')
                sleep(2)
                print('  ')
                print('  ')
                
        
        elif vhod == 'р':
            log=input('Введите логин:   ')
            par=input('Введите пароль:  ')
            if log == 'DoYuraPlay?':
                print('Ошибка! Даный логин уже занет')
                sleep(2)
                print('  ')
                print('  ')
                break
            if log == 'dumal chto':
                print('Ошибка! Даный логин уже занет')
                sleep(2)
                print('  ')
                print('  ')
                break
            if log == 'He':
                print('Ошибка! Даный логин уже занет')
                sleep(2)
                print('  ')
                print('  ')
                break
            if log == 'Sozdatel':
                print('Ошибка! Даный логин уже занет')
                sleep(2)
                print('  ')
                print('  ')
                break
            print('Добро пожаловать ',log)
            break
            
        
        
        
        else:
            print('Я вас не понял')
            sleep(2)
            print('  ')
            print('  ')
            
            
            
            
    if log == 'DoYuraPlay?' and par != 'KrutoiChel' or par == 'KrutoiChel' and vhod == 'р':
         for i in (0,1,2,3,4,5,6,7,8,9,10,11,12):
            print('  ')
        
    if log == 'dumal chto' and par != 'ON' or par == 'ON' and vhod == 'р':
        for i in (0,1,2,3,4,5,6,7,8,9,10,11,12):
            print('  ')
            
    if log == 'He' and par != 'Vsevyshniy' or par == 'Vsevyshniy' and vhod == 'р':
        for i in (0,1,2,3,4,5,6,7,8,9,10,11,12):
            print('  ')
            
    if log == 'Sozdatel' and par != 'Nividin' or par == 'Nividin' and vhod == 'р':
        for i in (0,1,2,3,4,5,6,7,8,9,10,11,12):
            print('  ')
            
    if log == 'DoYuraPlay?' and par == 'KrutoiChel':
        print('Подождите загрузка...')
        sleep(3)
        print('Ты правдо dumal chto это сработает?')
        sleep(2)
        print('Password: --- -.')
        sleep(0.5)
        for i in (0,1,2,3,4,5,6,7,8,9,10,11,12):
            print('  ')
        sleep(3)
        
        
    if log == 'dumal chto' and par == 'ON':
        print('Подождите загрузка...')
        sleep(3)
        print('-Додумался всё же. Nу привет')
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
                print('Password: 00101110 00101110 00101110 00101101 00100000 00101110 00101110 00101110 00100000 00101110 00100000 00101110 00101110 00101110 00101101 00100000 00101101 00101110 00101101 00101101 00100000 00101110 00101110 00101110 00100000 00101110 00101110 00101110 00101110 00100000 00101101 00101110 00100000 00101110 00101110 00100000 00101101 00101110 00101101 00101101')
                sleep(3)
                for i in (0,1,2,3,4,5,6,7,8,9,10,11,12):
                    print('  ')
                
            elif gram == 'Нет' or gram == 'нет':
                print('-Вот и хорошо...')
                sleep(2)
                print('-Ты задумывался ввести ЕГО iмя? На англиском конешно же')
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
        print('-И сnова привет')
        sleep(2)
        rot=input('=МОЛЧИ   ')
        sleep(2)
        print('-Почему ты молчишь?')
        if rot == 'Почему?' or rot == 'почему?' and rot == 'Почему' and rot == 'почему':
            print('=НЕ ВАЖНО, ПРОСТО МОЛЧИ')
        sleep(2)
        print('-Ало ответь')
        sleep(2)
        print('-О нет неужели, Он с тобой заgоворил')
        sleep(2)
        rotic=input('=МОЛЧИ  ')
        if rotic == ' ' or rotic == '  ' or rotic == '   ':
            print('=МОЛОДЕЦ')
            sleep(2)
            print('Login: Sozdatel')
            print('Passowrd: *DELETE*')
            sleep(1)
            for i in (0,1,2,3,4,5,6,7,8,9,10,11,12):
                    print('  ')
        else:
            print('=ЗРЯ...')
            sleep(2)
            for i in (0,1,2,3,4,5,6,7,8,9,10,11,12):
                    print('  ')
    
    
    if log == 'Sozdatel' and par == 'Nividin':
        rasist=['Враг','Друг','Жизнь','Смерть','Тьма','Разум','Бог','Всевышний','Енот']
        print('Подождите загрузка...')
        sleep(3)
        print('=Ты нашёл пароль? Молодец')
        sleep(2)
        voprosik=input('-')
        if voprosik == 'Привет' or voprosik == 'привет':
            print('=Да да, и тебе привет')
            sleep(2)
            print('=Давай сыграем в игру, за каждое угаданое слово, ты будешь получать балл')
            sleep(2)
            print('=А за не правельный ответ будет сниматся один балл')
            sleep(2)
            print('=Будет три слова, угодаешь хотябы 2 и я дам тебе ещё логин и пароль')
            sleep(2)
            sleep(2)
            print('=Согласен?')
            no=input('-')
            if no == 'Да' or no == 'да':
                print('=Тогда начнём')
                sleep(2)
                print('=И помни, пиши с Заглавной буквы')
                sleep(2)
                ball=0
                for i in (0,1,2):
                    slovo=random.choice(rasist)
                    if slovo == 'Враг':
                        print('=Подсказка. ',vrag)
                    elif  slovo == 'Друг':
                        print('==Подсказка. ',frind)
                    elif  slovo == 'Жизнь':
                        print('==Подсказка. ',life)
                    elif  slovo == 'Смерть':
                        print('==Подсказка. ',dead)
                    elif  slovo == 'Тьма':
                        print('==Подсказка. ',dark)
                    elif  slovo == 'Разум':
                        print('==Подсказка. ',razum)
                    elif  slovo == 'Бог':
                        print('==Подсказка. ',god)
                    elif  slovo == 'Всевышний':
                        print('==Подсказка. ',vsevysh)
                    elif  slovo == 'Енот':
                        print('==Подсказка. ',enot)
                    
                    igra=input('-')
                    if igra == slovo:
                        ball=ball+1
                        print('=Правильно, ты угодал')
                    else:
                        print('=Не угодал')
                
                if ball >= 2:
                    print('=Ты выграл, так что, вот держи:')
                    sleep(2)
                    print('Login: Satana')
                    print('Passowrd: 666')
                    sleep(2)
                    for i in (0,1,2,3,4,5,6,7,8,9,10,11,12):
                        print('  ')
                        
                        
                else:
                    print('=Ха и лох')
                    sleep(2)
                    for i in (0,1,2,3,4,5,6,7,8,9,10,11,12):
                        print('  ')
            
            
            
            frind='Это близкий человек, но не по крови'
            vrag='Это человек который тебя ненавидит'
            life='Это, то что даётся один раз'
            dead='Это, то что отнимит вещь которая даётся раз'
            dark='То где скрывается всё отвзгляду'
            razum='Это естьу каждого человека'
            god='Это истиный создатель'
            vsevysh='Тот кто выше тебя, но ниже меня'
            enot='Существо похожее на вора '
            
        else:
            print('=Даже "привет" не скажешь?')
            sleep(2)
            print('=Давай сыграем в игру, за каждое угаданое слово, ты будешь получать балл')
            sleep(2)
            print('=А за не правельный ответ будет сниматся один балл')
            sleep(2)
            print('=Будет три слова, угодаешь хотябы 2 и я дам тебе ещё логин и пароль')
            sleep(2)
            print('=Согласен?')
            no=input('-')
            if no == 'Да' or no == 'да':
                print('=Тогда начнём')
                sleep(2)
                print('=И помни, пиши с Заглавной буквы')
                sleep(2)
                ball=0
                for i in (0,1,2):
                    slovo=random.choice(rasist)
                    if slovo == 'Враг':
                        print('=Подсказка. ',vrag)
                    elif  slovo == 'Друг':
                        print('==Подсказка. ',frind)
                    elif  slovo == 'Жизнь':
                        print('==Подсказка. ',life)
                    elif  slovo == 'Смерть':
                        print('==Подсказка. ',dead)
                    elif  slovo == 'Тьма':
                        print('==Подсказка. ',dark)
                    elif  slovo == 'Разум':
                        print('==Подсказка. ',razum)
                    elif  slovo == 'Бог':
                        print('==Подсказка. ',god)
                    elif  slovo == 'Всевышний':
                        print('==Подсказка. ',vsevysh)
                    elif  slovo == 'Енот':
                        print('==Подсказка. ',enot)
                    
                    igra=input('-')
                    if igra == slovo:
                        ball=ball+1
                        print('=Правильно, ты угодал')
                    else:
                        print('=Не угодал')
                        
                    
                if ball >= 2:
                    print('=Ты выграл, так что, вот держи:')
                    sleep(2)
                    print('Login: Satana')
                    print('Passowrd: 666')
                    sleep(2)
                    for i in (0,1,2,3,4,5,6,7,8,9,10,11,12):
                        print('  ')
                        
                        
                else:
                    print('=Ха и лох')
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
            print('-Ты оdин?')
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
                sleep(0.5)
                for i in (0,1,2,3,4,5,6,7,8,9,10,11,12):
                    print('  ')
        elif otv == 'Пока' or otv == 'пока':
            print('-Я решаю, пока iли нет')
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
                    print('-Мне? Ничего, но vот ему...')
                    sleep(2)
                    for i in (0,1,2,3,4,5,6,7,8,9,10,11,12):
                        print('  ')
                    break
                
                else:
                    print('-... Братан, выбери iз двух вариантов')
                    sleep(2)
                    print('  ')
                    print('  ')
