def DistanceCounter(words, word1, word2):
    word1First = -1
    word2First = -1
    word1Last = -1
    word2Last = -1
    maxDist = -1
    minDist = 65000

    for i in range(len(words)):
        if words[i] == word1:
            if word1First == -1:
                word1First = i
                word1Last = i
            else:
                word1Last = i

        if words[i] == word2:
            if word2First == -1:
                word2First = i
                word2Last = i
            else:
                word2Last = i

        if (word1Last > -1) and (word2Last > -1) and minDist > abs((word1Last - word2Last)):
            minDist = abs(word1Last - word2Last)

    if (word1First > -1) and (word2First > -1):
        maxDist = abs(word1First - word2Last)
        if maxDist < abs(word2First - word1Last):
            maxDist = abs(word2First - word1Last)
            
    return [maxDist - 1, minDist - 1]


#ввод данных
sentence = input()
word1 = input()
word2 = input()
words = sentence.split(' ') #создание списка из слов входного предложения

#выполнение функции
result = DistanceCounter(words, word1, word2)

print('max distance: ', result[0], 'min distance: ', result[1])