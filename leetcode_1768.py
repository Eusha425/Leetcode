# 1768. Merge Strings Alternately

def mergeAlternately(word1: str, word2: str) -> str:
    newWord = ''
    for i in range(len(word1 + word2)):

        if i < len(word1):
            newWord = newWord + word1[i:i+1]
        if i < len(word2):
            newWord = newWord + word2[i:i+1]
    return newWord
