def find_pattern(word,pattern):
    pattern_exists=False
    for i in range(0,len(word)):
        for j in range(0,len(pattern)):
            if(i+j>len(word)-1):
                break
            if(word[i+j]!=pattern[j]):
                break
            if(j==len(pattern)-1):
                pattern_exists=True
                print("The location where the word/pattern \'"+pattern+"\' exists in \'"+word+"\' is")
                print((i+1),i+1+len(pattern))
    if(pattern_exists==False):
        print("\'"+pattern+"\' doesn't exist in \'"+word+"\'")


pattern="s"
word="Sun rises in the East."
find_pattern(word,pattern)
