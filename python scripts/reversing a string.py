class wordreverse(string):
    i=len(string)-1
    start=end=0
    result=''
    while i>=0:
        if string[i] =='':
            start=i+1
            while start !=end:
                result +=string[start]
                start+=1
                result += ''
                end=1
    start=0
    while start !=end:
        result+=string[start]
        start +=1
    print(result) 

word=word.wordreverse('i am a geek')