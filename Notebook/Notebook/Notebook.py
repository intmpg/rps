print ('Записная книжка')
print ('Add name - добавить контакт')
print ('Find name - поиск контакта')
print ('exit - выход')

contactList = []
command = input()

while (command != "exit"):

    commandArgs = command.split(' ')

    if (commandArgs[0] == "Add") or (commandArgs[0] == "add"):
        contactList.append(commandArgs[1])
        print ('Добавлен контакт ', commandArgs[1])
        print (contactList)

    elif (commandArgs[0] == "Find") or (commandArgs[0] == "find"):
        count = 0
        for index, item in enumerate(contactList):
            if contactList[index].startswith(commandArgs[1]):
                count = count + 1
        print(count)

    command = input()