#!/usr/bin/python3

"""Kanye Quote Generator | Author: Andrew Taylor

Description:
    A script to interact with an api,
    https://api.kanye.rest and display kanyw west quote as many times as the user wants
"""

import requests
import crayons

kanye_url = 'https://api.kanye.rest' ### Send HTTPS GET to API

print(crayons.yellow("\nThe Gospel According to Kanye West\n"))  # Prints Header


#make call to api to get quote
def getquote():
    resp = requests.get(kanye_url)
    kanye_quote = resp.json()
    quote = kanye_quote["quote"]
    return quote


def main():
    
    while True: #start loop
             
        answer1 = input("\nWould you like to hear a quote from the Gospel of Kanye West? y/n ")   #Ask user if they want a quote
       
        if answer1 == "y":
            print(crayons.red(getquote())) # if y outputs quote in red
            answer2 = input("\nWould you like to hear another? y/n ") #asks user if they want another quote
            
            if answer2 == "y":
                print(crayons.red(getquote())) # if y outputs quote in red
            
            elif answer2 == "n":
                print(crayons.yellow("\nGoodbye! Praise be to Yezus!")) #outputs text in yellow
                break

        elif answer1 == "n":
            print(crayons.yellow("\nGoodbye! Praise be to Yezus!"))
            break #end loop

        else:
            print("\n Please enter y or n ") #prompts user to enter y or n, will loop until one y or n is entered
    
main() #call main function
