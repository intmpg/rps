import time

#Для хранения списка контактов используется словарь, ключ которого - первая буква имени, а значение - список имен
#вывод условий
print ('Записная книжка')
print ('Add name - добавить контакт')
print ('Find name - поиск контакта')
print ('exit - выход')

#создание словаря контактов
contactDict = dict()
command = input() # ввод первой команды

while (command != "exit"): # цикл для постоянного ввода, закончится по команде "exit"

    commandArgs = command.split(' ') # разделяем команду на список двух аргументов ['команда', 'имя']

    #если команда "add", то либо добавляем новый ключ в словарь и список с контактом к нему, либо добавляем уже к существующему списку новый контакт если он начинается на ту же букву
    if (commandArgs[0] == "Add") or (commandArgs[0] == "add"):
        contactNameChars = ''
        i = 0
        for index in commandArgs[1]:
            contactNameChars = contactNameChars + commandArgs[1][i]
            i+= 1
            if contactNameChars not in contactDict:
                contactDict[contactNameChars] = 1
            else:
                contactDict[contactNameChars]+= 1

        print ('Добавлен контакт ', commandArgs[1])

    #если же команда "find", то перебираем все элементы списка контактов и находим тот, который начинается с введенного имени
    elif (commandArgs[0] == "Find") or (commandArgs[0] == "find"):
        
        start_time = time.clock()
        print(contactDict.get(commandArgs[1]))
        print(time.clock() - start_time, "seconds")

    command = input() #ввод очередной команды после выполнения