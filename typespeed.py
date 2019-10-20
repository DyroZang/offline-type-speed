import sys
import matplotlib.pyplot as plt
import time
from random import randint

#Variables
prompt = ""
wordslist = []
wpm = timed = 0
response = ""


def createPrompt(le, wordsl):
    ret = ""
    for i in range(le):
        ret += wordsl[randint(0,len(wordsl)-1)].lower() + " "
    return ret.strip()

def test():
    global wordslist, response, prompt, timed, wpm
    #Create the prompt and show it to the user
    prompt = createPrompt(10, wordslist)
    print("\n",prompt,"\n", sep ="")

    #Have the user type in the prompt
    print("Type the above prompt in...")

    #Countdown to typing
    for i in range(3,0,-1):
        print(str(i) + "."*3)
        time.sleep(1)

    #Check how long it took to type and store that amount of time in the time variable
    print("Start!")
    timed = time.time()
    response = input()
    timed = round(time.time() - timed, 2)

    #Calculate WPM
    #print("Time:",timed)
    #print("Characters:",len(response))
    wpm = int((len(response)/5)/(timed/60))
    main()

def wpmavg():
    #Read from a file of past WPM and add that to a table of values
    wpmfile = open("wpmhistory.txt", "r")
    #Turn the file speeds into a list
    wpms = [int(i) for i in wpmfile.read().split()]
    #Print out the average wpm
    print("\n\nYour average typing speed is",sum(wpms)/len(wpms),"Words Per Minute!")
    wpmfile.close()

def wpmadd(num):
    #Adds given wpm to the text file of words per minute
    infile = open("wpmhistory.txt","a")
    print(str(num) + " ", file=infile)
    infile.close()

def wpmgraph():
    file = open("wpmhistory.txt", "r")
    speeds = [int(i) for i in file.read().split()]
    ys = [i for i in range(len(speeds))]
    fig, graph = plt.subplots()
    graph.plot(ys,speeds)
    plt.show()
    file.close()

def main():
    global wordslist, response, prompt, timed, wpm
    #Opening from a file of 10,000 words and putting all the words into a list
    words = open("words.txt", "r")
    wordslist = words.read()
    wordslist = wordslist.split()

    #Check if they wrote the prompt and print out wpm with a cute statement
    if prompt == "":
        print()
    elif(response == prompt):
        print("Great job, you typed at", wpm,"Words Per Minute!")
        wpmadd(wpm)
    elif response == "avg":
        print()
    elif response == "graph":
        print()
    else:
        print("You made a typing error, however you typed at",wpm,"Words Per Minute!")

    response = input("Would you like to race?\n\t'Y' for yes\n\t'N' for no\n\t'AVG' for your wpm avg\n\t'GRAPH' for graph of WPM history\n\t")
    if(response.lower().strip() == "y"):
        #restarts the program
        test()
    elif(response.lower().strip() == "avg"):
        #Displays their wpm average
        wpmavg()
        main()
    elif(response.lower().strip() == "graph"):
        wpmgraph()
        main()
    else:
        sys.exit()

main()
