import sys, time
from random import randint


#Variables
prompt = ""
wordslist = []
wpm = timed = 0
response = ""

def main():
    global wordslist, wpm, timed, response, prompt
    

    #Opening from a file of 10,000 words and putting all the words into a list
    words = open("words.txt", "r")
    wordslist = words.read()
    wordslist = wordslist.split()
    
    #Run the program
    test()

def createPrompt(le, wordsl):
    ret = ""
    for i in range(le):
        ret += wordsl[randint(0,len(wordsl)-1)].lower() + " "
    return ret.strip()

def test():
    global wordslist, response, prompt, timed, wpm
    #Create the prompt and show it to the user
    prompt = createPrompt(20, wordslist)
    print("\n",prompt,"\n", sep ="")


    #Have the user type in the prompt 
    print("Type the above prompt in...")

    #Countdown to typing
    for i in range(3,0,-1):
        print(str(i) + "."*3)
        time.sleep(1)

    #Check how long it took to type and store that amount of time in the time variable
    timed = time.time()
    response = input()
    timed = round(time.time() - timed, 2)

    #Calculate WPM
    #print("Time:",timed)
    #print("Characters:",len(response))
    wpm = int((len(response)/5)/(timed/60))
    restart()
    

def restart():
    global wordslist, response, prompt, timed, wpm
    #Check if they wrote the prompt and print out wpm with a cute statement
    if(response == prompt):
        print("Great job, you typed at", wpm,"Words Per Minute!")
    else:
        print("You made a typing error, however you typed at",wpm,"Words Per Minute!")

    response = input("Would you like to go again? (y/n)")
    if(response == "y"):
        #TODO: Make the whole program run again
        test()
    else:
        sys.exit()

main()