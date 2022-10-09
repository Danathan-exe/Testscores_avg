x, y, z, a, b = input("Enter Five Test Scores: ").split() #allows user input for 5 on one line
list = [int(x), int(y), int(z), int(a), int(b)] #creates list
#creates variables such as the average and sorts them.
avg = sum(list)/len(list)
list.sort()
length = len(list)
#prints the test scores from highest to lowest then prints the average.
print("Test Score #1:", list[length-1])
print("Test Score #2:", list[length-2])
print("Test Score #3: ", list[2])
print("Test Score #4: ", list[1])
print("Test Score #5: ", list[0])

print("The Average Test Score was " + str(avg))