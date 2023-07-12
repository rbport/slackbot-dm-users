import csv

def csvtolist(): #this is the function that pulls emails from csv into a readable format. no extra editing is needed before passing to the next function
    results = []
    with open('emails.csv', newline='') as inputfile:
        for row in csv.reader(inputfile):
            results.append(row[0]) #be very careful that you do have any empty lines in your csv file or you will get an Index out of Range error.
    
    return results
