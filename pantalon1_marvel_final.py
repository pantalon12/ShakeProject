import csv
import re
file='marvel-wikia-data.csv'
#Imports necessary packages and defines the file to be used in this program

def sort(file):
#Splits each characters info into arrays and returns said arrays to be used in search

    index = []
    names = []
    url = []
    public = []
    gbn = []
    eyes = []
    hair = []
    gender = []
    gsm = []
    live = []
    appearance = []
    date = []
    year = []
    #creating empty arrays

    with open(file) as marveldata:
        marvelread = csv.reader(marveldata)
        #opens csv file
        for row in marvelread:
            index.append(row[0])
            names.append(row[1])
            url.append(row[2])
            public.append(row[3])
            gbn.append(row[4])
            eyes.append(row[5])
            hair.append(row[6])
            gender.append(row[7])
            gsm.append(row[8])
            live.append(row[9])
            appearance.append(row[10])
            date.append(row[11])
            year.append(row[12])
            #iterates through rows of csv file and fills arrays with info for each hero
    nhero=len(index)
    return index, names, url, public, gbn, eyes, hair, gender, gsm, live, appearance, date, year, nhero

class search:
    #search functions
    def yearsearch(yearinput,nhero):
        #search through file by year of first appearance
        yearinput=str(yearinput)
        yearmatches = []
        #creates an empty array that will be used to store all characters which debuted in that year
        for i in range(0, nhero):
            if year[i] == yearinput:
                yearmatches.append(i)
                #fills array with matches
        return yearmatches

    def namesearch(nameinput,nhero):
        namematches = []
        #creates an empty array that will be used to store all characters which have a matching name
        for j in range(0, nhero):
            if re.search(nameinput.lower(),names[j].lower()):
                namematches.append(j)
                #fills array with matches
        return namematches

class user:
    def name():
        #This function will allow the user to search by name, and will then list all matching characters and allow them to select a character to get more info
        nameinput = input("Name:")
        namematches = search.namesearch(nameinput,nhero)
        print("Matching Characters:")
        for k in range(0,len(namematches)):
            print(k, names[namematches[k]])
            #lists all matching characters with an indexing number
        charselect = input("Enter the number next to the character you'd like to learn more about:")
        charselect = int(charselect)
        print("Index Number: ", index[namematches[charselect]])
        print("Name/Planet: ", names[namematches[charselect]])
        print("URL: ", url[namematches[charselect]])
        print("Public/Private: ", public[namematches[charselect]])
        print("Good/Bad/Neutral: ", gbn[namematches[charselect]])
        print("Eye Color: ", eyes[namematches[charselect]])
        print("Hair Color: ", hair[namematches[charselect]])
        print("Gender: ", gender[namematches[charselect]])
        print("GSM: ", gsm[namematches[charselect]])
        print("Alive/Dead: ", live[namematches[charselect]])
        print("Appearance: ", appearance[namematches[charselect]])
        print("Date of First Appearance: ", date[namematches[charselect]])
        print("Year of First Appearance: ", year[namematches[charselect]])
    def year():
        #This function will allow the user to search by year, and will then list all matching characters and allow them to select a character to get more info
        yearinput=input("Year:")
        yearmatches=search.yearsearch(yearinput,nhero)
        print("Matching Characters:")
        for k in range(0,len(yearmatches)):
            print(k, names[yearmatches[k]])
            #lists all matching characters with an indexing number
        charselect = input("Enter the number next to the character you'd like to learn more about:")
        charselect = int(charselect)
        print("Index Number: ", index[yearmatches[charselect]])
        print("Name/Planet: ", names[yearmatches[charselect]])
        print("URL: ", url[yearmatches[charselect]])
        print("Public/Private: ", public[yearmatches[charselect]])
        print("Good/Bad/Neutral: ", gbn[yearmatches[charselect]])
        print("Eye Color: ", eyes[yearmatches[charselect]])
        print("Hair Color: ", hair[yearmatches[charselect]])
        print("Gender: ", gender[yearmatches[charselect]])
        print("GSM (if available): ", gsm[yearmatches[charselect]])
        print("Alive/Dead: ", live[yearmatches[charselect]])
        print("Appearance: ", appearance[yearmatches[charselect]])
        print("Date of First Appearance: ", date[yearmatches[charselect]])
        print("Year of First Appearance: ", year[yearmatches[charselect]])

index, names, url, public, gbn, eyes, hair, gender, gsm, live, appearance, date, year, nhero = sort(file)
#Splits csv file into arrays

q=1
while q==1:
    #will keep program running until user enters 3
    type = input("Enter 1 to search by name, enter 2 to search by year of first appearance, or enter 3 to end the program:")
    type = int(type)

    if type == 1:
        user.name()
    if type == 2:
        user.year()
    if type == 3:
        q=2
