def DistanceCounter(sentence, word1, word2):
    word1Pos = []
    word2Pos = []
    words = sentence.split(' ')

    for index, item in enumerate(words):
        if (words[index] == word1):
            word1Pos.append(index)
        if (words[index] == word2):
            word2Pos.append(index)

    if len(words) == 2:
        print('min distance: 0')
        print('max distance: 0')

    elif len(words) == 1:
        print('The sentence consists of one word')
    
    elif not word1Pos or not word2Pos:
        print('The sentence does not contain both words')
            
    elif min(word1Pos) < min(word2Pos):
        print('Min distance: ', (min(word2Pos) - min(word1Pos) - 1))
        print('Max distance: ', (max(word2Pos) - max(word1Pos) - 1))

    elif min(word1Pos) > min(word2Pos):
        print('Min distance: ', (min(word1Pos) - min(word2Pos) - 1))
        print('Max distance: ',  (max(word1Pos) - max(word2Pos) - 1))
    

sentence = input()
word1 = input()
word2 = input()

DistanceCounter(sentence, word1, word2)





       





