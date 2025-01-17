# function
def pattern(pattern, s):
    words = s.split()
    if len(pattern) != len(words):
        return False
    char_to_word = {}
    word_to_char = {}
    for char, word in zip(pattern, words):
# if else statement   
        if char in char_to_word:
            if char_to_word[char] != word:
                return False
        else:
            char_to_word[char] = word
        
        if word in word_to_char:
            if word_to_char[word] != char:
                return False
        else:
            word_to_char[word] = char
    return True
# example
pattern1, s1 = "abba", "flower bee bee flower"
pattern2, s2 = "abba", "flower bee bee plant"
pattern3, s3 = "aaaa", "flower bee bee flower"
pattern4, s4 = "abba", "flower bee plant flower"
#print 
print(pattern(pattern1, s1))  
print(pattern(pattern2, s2))  
print(pattern(pattern3, s3))  
print(pattern(pattern4, s4))  

