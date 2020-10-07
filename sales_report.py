"""Generate sales report showing total melons each salesperson sold."""


salespeople = []
melons_sold = []
#initializing empty lists to store the salespeople and melons sold 

f = open('sales-report.txt')
#opens the file (creates an access point to the file)
for line in f:
    #iterating over each line in the file 
    line = line.rstrip()
    #stripping off the trailing whitespace of the string 
    entries = line.split('|')
    #splitting the file into a list of strings on the delimiter |

    salesperson = entries[0]
    #using the index to pull out the salesperson's name 
    melons = int(entries[2])
    #using the index to pull out the number of melons as an integer

    if salesperson in salespeople:
        position = salespeople.index(salesperson)
        #if the salesperson is in the salespeople list, the position is the index 
        #of salesperson

        melons_sold[position] += melons
        #melons at the same index (as the index of the salesperson in the salesperson list)
        #are incremented 
 
    else:
        salespeople.append(salesperson)
        melons_sold.append(melons)
        #if the salesperson isn't in the list yet, add the salesperson to the end of the
        #list and add the initial amount of the melons


for i in range(len(salespeople)):
    print(f'{salespeople[i]} sold {melons_sold[i]} melons')
    #indexing through salespeople using the range 0 1 2 3 ... to print the salesperson
    #at index i in salespeople and the melons at index i in melons_sold
