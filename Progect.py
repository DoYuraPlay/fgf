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
            
            elif log == 'DoYuraPlay?' and par != 'KrutoiChel':
                print('Неверный логин или пароль')
                sleep(2)
                
        
        elif vhod == 'р':
            log=input('Введите логин:   ')
            par=input('Введите пароль:  ')
            print('Добро пожаловать ',log)
            break
            
        
        
        
        else:
            print('Я вас не понял')
            
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
    
    
     if log == 'DoYuraPlay?':
        print('Подождите загрузка...')
        sleep(3)
        print('Ты правдо dumal chto это сработает?')
        sleep(2)
        for i in (0,1,2,3,4,5,6,7,8,9,10,11,12):
            print('  ')
        sleep(3)