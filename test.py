def reverse_string(word):
    #reverse a word recursively
    if len(word) == 0:
        return word
    else:
        print(word[0])
        
        return reverse_string(word[1:]) + word[0]
        

print(reverse_string("halloween"))