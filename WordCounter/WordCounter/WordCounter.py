def DistanceCounter(sentence, word1, word2):
    word1Pos = [] #список для позиций первого слова
    word2Pos = [] #список для позиций второго слова
    words = sentence.split(' ') #создание списка из слов входного предложения

    #заполнение списков с позициями первого и второго слова
    for index, item in enumerate(words):
        if (words[index] == word1):
            word1Pos.append(index)
        if (words[index] == word2):
            word2Pos.append(index)

    #вычисление и вывод минимального и максимального расстояния
    minDist = 65000

    for i, item in enumerate(word2Pos):
        for j, item in enumerate(word1Pos):
            if (word2Pos[i] > word1Pos[j]) and ((word2Pos[i] - word1Pos[j]) < minDist):
                minDist = word2Pos[i] - word1Pos[j]
            elif (word2Pos[i] < word1Pos[j]) and ((word1Pos[j] - word2Pos[i]) < minDist):
                minDist = word1Pos[j] - word2Pos[i]

    if len(words) == 2: #в случае если предложение состоит из двух слов
        print('min distance: 0')
        print('max distance: 0')

    elif len(words) == 1: #в случае если предложение - это одно слово выходит ошибка
        print('The sentence consists of one word')
    
    elif not word1Pos or not word2Pos: #если какого-то из двух слов в предложении нет
        print('The sentence does not contain both words')

    #расстояние между словами - разность между номерами их позиций        
    elif min(word1Pos) < min(word2Pos): # в случае если первым встречается первое слово
        maxDist = min(word1Pos) + max(word2Pos)
        print("Min distance: ", minDist - 1)
        print("Max distance: ", maxDist - 1)

    elif min(word1Pos) > min(word2Pos): # в случае если первым встречается второе слово
        maxDist = min(word2Pos) +  max(word1Pos)
        print("Min distance: ", minDist - 1)
        print("Max distance: ", maxDist - 1)
        
#ввод данных
sentence = input()
word1 = input()
word2 = input()

#выполнение функции
DistanceCounter(sentence, word1, word2)