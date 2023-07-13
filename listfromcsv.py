import csv

def csvtolist(): #this is the function that pulls emails from csv into a readable format. no extra editing is needed before passing to the next function
    results = []
    with open('emails.csv', newline='') as inputfile:
        for row in csv.reader(inputfile):
            if len(row) > 0:  # Check if the row has at least one element. eliminates empty line index error
                results.append(row[0]) 
    #print(results)
    return results

