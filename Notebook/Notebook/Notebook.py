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

        if commandArgs[1][0] not in contactDict:
            contactDict[commandArgs[1][0]] = commandArgs[1].split(' ')
        else:
            contactDict[commandArgs[1][0]].append(commandArgs[1])

        print ('Добавлен контакт ', commandArgs[1])
        print (contactDict)

    #если же команда "find", то перебираем все элементы списка контактов и находим тот, который начинается с введенного имени
    elif (commandArgs[0] == "Find") or (commandArgs[0] == "find"):
        contactList = contactDict.get(commandArgs[1][0]) # получаем список контактов по ключу (первой букве)
        count = 0 #счетчик контактов, обнуляется каждый раз когда вызывается команда поиска
        for index, item in enumerate(contactList):
            if contactList[index].startswith(commandArgs[1]):
                count = count + 1 #если строка из списка контактов начинается со строки, введенной как имя контакта, то прибавляем 1 к количеству искомых контактов
        print(count) #вывод количества вхождений

    command = input() #ввод очередной команды после выполнения