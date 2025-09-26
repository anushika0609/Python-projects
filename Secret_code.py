
word = input("Enter the word or code : ")
code = int(input("Enter whether to code or decode (0 or 1) : "))

# Coding
if(code == 0):
    if(len(word) > 3):
        word+=word[0]
        index = 0
        word = word[:index] + word[index+1:]
        final = "hjk"+word+"iou"
        print(f"Codeword is : {final}")
    else:
        word = word[::-1]
        print(f"Codeword is : {word}")
        
# Decoding
if(code == 1):
    if(len(word)<3):
        word = word[::-1]
        print(f"Decoded word is : {word}")
    else:
        index = 0
        word = word[:index] + word[index+3:]
        index2 = len(word)-3
        word = word[:index2] + word[index2+3:]
        word = word[len(word)-1]+word
        index = len(word) - 1
        word = word[:index] + word[index+1:]
        print(word)
