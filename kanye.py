#!/usr/bin/python3

import requests
import crayons

kanye_url = 'https://api.kanye.rest'

print(crayons.yellow("\nThe Gospel According to Kanye West\n"))

def getquote():
    resp = requests.get(kanye_url)
    kanye_quote = resp.json()
    quote = kanye_quote["quote"]
    return quote


def main():
    
    while True:    
             
        answer1 = input("Would you like to hear a quote from the Gospel of Kanye West? y/n ")
        if answer1 == "y":
            
            print(crayons.red(getquote()))
            answer2 = input("\n Would you like to hear another? y/n ")
            if answer2 == "y":
                print(crayons.red(getquote()))
            elif answer2 == "n":
                print("\nGoodbye")
                break
        elif answer1 == "n":
            print("\nGoodbye!")
            break
        else:
            print("\n Please enter y or n ")
    
main()
