def repeater (w):
    def howmuch(n):
        return w * n
    return howmuch
 

 # cant get eassier than this. User is asked to enter a word, next is asked to enter a number
 # Program returns the word repeated X times 




def run():
    enterword : str = input ("Word : ")
    result = repeater(enterword)
    times : int = int(input ("times: "))
    print(result(times))





if __name__=="__main__":
    run()