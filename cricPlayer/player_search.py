outputFileName = open("player_data.txt", 'r')

file = open("player_data.txt", "r")
data = file.read()
file_data = data
file_data = file_data.lower()

file_data = file_data.splitlines()

search_for = input("Players Name: ")
search_for = search_for.lower()

for i in range(len(file_data)):
    x = file_data[i].split("|")
    if (x[0].find(search_for))!=-1:
        print(x[1])
        exit(0)