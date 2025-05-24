from time import sleep
import random


while True:
    while True:
        print('Вход - в  Регестрация - р')
        vhod=input()
        suget=0
        
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
            
            elif log == 'DoYuraPlay?' and suget == 0:
                print('Вы ещё не продвинулись до этого момента')
                
                
                
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
                
            elif log == 'dumal chto' and suget == 1:
                print('Вы ещё не продвинулись до этого момента')
                
                
                
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
                
            elif log == 'He' and suget == 2:
                print('Вы ещё не продвинулись до этого момента')
                
                   
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
                
            elif log == 'Sozdatel' and suget == 3:
                print('Вы ещё не продвинулись до этого момента')
                
                
            if log == 'Satana' and par == '666':
                print('Добро пожаловать ',log)
                break
            
            elif log != 'Satana' and par == '666':
                print('Неверный логин или пароль')
                sleep(2)
                print('  ')
                print('  ')
            elif log == 'Satana' and par != '666':
                print('Неверный логин или пароль')
                sleep(2)
                print('  ')
                print('  ')
                
            elif log == 'Satana' and suget == 4:
                print('Вы ещё не продвинулись до этого момента')
            
            if log !='He' and log != 'dumal chto' and log != 'DoYuraPlay?' and par != 'Vsevyshniy' and par != 'ON' and par != 'KrutoiChel'  :
                print('Даный акаунт не создан')
                sleep(2)
                print('  ')
                print('  ')
                
        
        elif vhod == 'р' or suget:
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
            if log == 'Satana':
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
        for i in range(20):
            print('  ')
        
    if log == 'dumal chto' and par != 'ON' or par == 'ON' and vhod == 'р':
        for i in range(20):
            print('  ')
            
    if log == 'He' and par != 'Vsevyshniy' or par == 'Vsevyshniy' and vhod == 'р':
        for i in range(20):
            print('  ')
            
    if log == 'Sozdatel' and par != 'Nividin' or par == 'Nividin' and vhod == 'р':
        for i in range(20):
            print('  ')
    
    if log == 'Satana' and par != '666' or par == '666' and vhod == 'р':
        for i in range(20):
            print('  ')
            
    if log == 'DoYuraPlay?' and par == 'KrutoiChel' and suget >= 1:
        print('Подождите загрузка...')
        sleep(3)
        print('Ты правдо dumal chto это сработает?')
        sleep(2)
        print('Password: --- -.')
        suget=2
        sleep(0.5)
        for i in range(20):
            print('  ')
        sleep(3)
        
        
    if log == 'dumal chto' and par == 'ON' and suget >= 2:
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
                suget=3
                sleep(3)
                for i in range(20):
                    print('  ')
                
            elif gram == 'Нет' or gram == 'нет':
                print('-Вот и хорошо...')
                sleep(2)
                print('-Ты задумывался ввести ЕГО iмя? На англиском конешно же')
                suget=3
                sleep(2)
                for i in range(20):
                    print('  ')
        else:
            print('-...')
            sleep(2)
            print('- 11010000 10100010 11010001 10001011 00100000 11010000 10111101 11010000 10110101 11010000 10110011 11010000 10110100 11010000 10110101 00100000 11010000 10111110 11010001 10000010 00100000 11010000 10111101 11010000 10110101 11010000 10110011 11010000 10111110 00100000 11010000 10111101 11010000 10110101 00100000 11010001 10000001 11010000 10111111 11010001 10000000 11010001 10001111 11010001 10000111 11010000 10110101 11010001 10001000 11010001 10001100 11010001 10000001 11010001 10001111')
            suget=3
            sleep(2)
            for i in range(20):
                print('  ')
                    
    if log == 'He' and par == 'Vsevyshniy' and suget >= 3:
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
            suget=4
            sleep(1)
            for i in range(20):
                print('  ')
        else:
            print('=ЗРЯ...')
            suget=4
            sleep(2)
            for i in range(20):
                print('  ')
    
    
    if log == 'Sozdatel' and par == 'Nividin' and suget >= 4:
        rasist=['Враг','Друг','Жизнь','Смерть','Тьма','Разум','Бог','Всевышний','Енот']
        frind='Это близкий человек, но не по крови'
        vrag='Это человек который тебя ненавидит'
        life='Это, то что даётся один раз'
        dead='Это, то что отнимит вещь которая даётся раз'
        dark='То где скрывается всё отвзгляду'
        razum='Это есть у каждого человека'
        god='Это истиный создатель'
        vsevysh='Тот кто выше тебя, но ниже меня'
        enot='Существо похожее на вора '
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
                    suget=5
                    sleep(2)
                    for i in range(20):
                        print('  ')
                        
                        
                else:
                    print('=Ха и лох')
                    suget=5
                    sleep(2)
                    for i in range(20):
                        print('  ')
                        
            elif no == 'Нет' or no == 'нет':
                print('=Хорошо.')
                sleep(2)
                print('=Тогда пока')
                suget=5
                sleep(2)
                for i in range(20):
                    print('  ')
                    
            else:
                print('=Сочту это за нет')
                suget=5
                sleep(2)
                for i in range(20):
                    print('  ')
            
            
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
                    suget=5
                    sleep(2)
                    for i in range(20):
                        print('  ')
                        
                        
                else:
                    print('=Ха ну и лох')
                    suget=5
                    sleep(2)
                    for i in range(20):
                        print('  ')
    
    
    
    if log == 'Satana' and par == '666' and suget >= 5:
        print('Подождите загрузка...')
        sleep(3)
        print('<Приветствую тебя, смертный')
        sleep(2)
        print('<Что привело тебя в мою обитель?')
        sleep(2)
        print('<Неужто ты собираешься...')
        sleep(2)
        print('<...')
        sleep(2)
        print('<Встать на моё место?')
        sleep(2)
        conesh=input('-')
        if conesh == 'Да'or conesh == 'да' or conesh == 'ДА':
            print('<Тогда...')
            sleep(2)
            print('<Забирай наздоровье, оно мне и не нужно')
            sleep(2.5)
            print('<Я серьёзно')
            sleep(2)
            print('<Держи')
            sleep(2)
            print('>Давай, пока')
            sleep(2)
            print('-Как ты это сделал?')
            sleep(2)
            samhz=input('<Неважно как, важно, что теперь это конец')
            sleep(2)
            print('Поздравляю с прохождением проекта')
            sleep(2)
            break
            
        elif conesh == 'Нет'or conesh == 'нет' or conesh == 'НЕТ':
            print('<Тогда зачем?')
            sleep(2)
            print('<Хотя стой я сам угодаю')
            sleep(2)
            print('<Ты просто решил проверить, что будет если ввести этот логин и пароль?')
            sleep(3)
            print('<Что же, тогда ты проиграл')
            sleep(2)
            print('Поздравляю с прохождением проекта')
            sleep(2)
            break
        
        else:
            print('<Понятно...')
            sleep(2)
            print('<Не чего не понел, так что покааа')
            sleep(2)
            print('Поздравляю с прохождением проекта')
            sleep(2)
            break
        
    
    
    
    
    if vhod == 'р' and progres >= 0 and suget >= 0:
        print('Подождите загрузка...')
        progres=progres+1
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
                print('Ваш аккаунт удалён')
                suget=1
                sleep(2)
                for i in range(20):
                        print('  ')
            elif yes == 'Нет' or yes == 'нет':
                print('-Верно. Ведь он, всегда за твоей спиной...')
                sleep(2)
                print('Ваш аккаунт удалён')
                suget=1
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
                    print('Ваш аккаунт удалён')
                    suget=1
                    sleep(2)
                    for i in range(20):
                        print('  ')
                    break
                
                elif reshi == 'ч':
                    print('-Мне? Ничего, но vот ему...')
                    sleep(2)
                    print('Ваш аккаунт удалён')
                    suget=1
                    sleep(2)
                    for i in (0,1,2,3,4,5,6,7,8,9,10,11,12):
                        print('  ')
                    break
                
                else:
                    print('-... Братан, выбери iз двух вариантов')
                    sleep(2)
                    print('  ')
                    print('  ')
        else:
            print('-Понятно')
            sleep(2)
            print('Ваш аккаунт удалён')
            suget=1
            sleep(2)
            for i in range(20):
                print('  ')




print('Пускайте титры')
sleep(2)
print('Сценарист-Юрий Митрошкин')
print('  ')
print('Оператор-Юрец огурец')
print('  ')
print('Режесер-Юрашка Чебурашка')
print('  ')
print('Закадровый голос-Юра')
print('  ')
print('Лётчик космалёта-Юрий Гагарин')
print('  ')
print('Помощник сценариста-ДураПлей')
print('  ')
print('Натуральный актёр-Юрецкий')
print('  ')
print('Идейный вдохновитель-DoYuraPlay?')
print('  ')
sleep(2)
print('ВСЁ. Конец!')