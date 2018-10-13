#Для хранения списка контактов используется динамический список, поиск осуществляется перебором его элементов и проверкой на вхождение строки в этот элемент 
#вывод условий
print ('Записная книжка')
print ('Add name - добавить контакт')
print ('Find name - поиск контакта')
print ('exit - выход')

#создание списка контактов
contactList = []
command = input() # ввод первой команды

while (command != "exit"): # цикл для постоянного ввода, закончится по команде "exit"

    commandArgs = command.split(' ') # разделяем команду на список двух аргументов ['команда', 'имя']

    #если команда "add", то добавляем в список контактов contactList новый элемент со значением имя контакта
    if (commandArgs[0] == "Add") or (commandArgs[0] == "add"):
        contactList.append(commandArgs[1])
        print ('Добавлен контакт ', commandArgs[1])
        print (contactList)

    #если же команда "find", то перебираем все элементы списка контактов и находим тот, который начинается с введенного имени
    elif (commandArgs[0] == "Find") or (commandArgs[0] == "find"):
        count = 0 #счетчик контактов, обнуляется каждый раз когда вызывается команда поиска
        for index, item in enumerate(contactList):
            if contactList[index].startswith(commandArgs[1]):
                count = count + 1 #если строка из списка контактов начинается со строки, введенной как имя контакта, то прибавляем 1 к количеству искомых контактов
        print(count) #вывод количества вхождений

    command = input() #ввод очередной команды после выполнения