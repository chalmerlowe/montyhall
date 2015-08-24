# Title: 
# Filename: .py
# Usage: 
# Description:
# Author: Nevan Lowe
# Version: 1.1
# Python Revision: 3.*
# IPython Revision: n/a
# TO DO:
# 
#---------------------------------------------------------

import random
from datetime import datetime
startTime = datetime.now()

#  creates counters to track wins and losses.
wincount = 0
losecount = 0

cycles = int(input('How many tests do you want to run? '))

for x in range(cycles):
    #  sets the game to play one hundred million times
    contents = [1, 0, 0]
    #  sets the doors and their contents. 1 = car, 0 = donkey
    random.shuffle(contents)
    #  places the car inside a random door
    pick = random.randint(0, 2)
    #  you pick a random door
    contents.insert(3, contents.pop(pick))
    pick = 1
    #  moves your door to the end (this is to help make 'revealing' an incorrect door easier). This is done by removing the door you picked and inserting it at the end

    if contents[2] == 0:
    #  checks if there is a donkey behind your door
        contents.remove(0)
    #  if there is, 'reveal' the only other door with a donkey. This is done by checking for the first door with a donkey behind it and deleting it
    else:
        contents.pop(0)
    #  if there isn't, 'reveal' one of the donkeys. This is done by deleting the first item in the list. Because your pick is the car and it's been moved to the end of
    #  the list, the first item in the list is guaranteed to be a donkey
    pick -= 1
    #  this is effectively switching
    
    if contents[pick] == 1:
    #  this is where the car is revealed
        wincount += 1
    #  if it is under your door, I add 1 to the win counter
    else:
        losecount += 1
    #  if the car is not under your door, I add 1 to the loss counter
    
summary = 'Over the past {} games, switching won you a car {} times, while if you stuck with your original choice you would have won {} times, & switching caused you to win {}% of the time.'    

percentage = wincount/(cycles/100)

print(cycles, wincount, losecount)
#cycles, wincount, losecount = [str(x) for x in (cycles, wincount, losecount)]
print(cycles, wincount, losecount)



    
print('Over the past '+str(cycles)+' games, switching won you a car '+str(wincount)+' times, while if you stuck with your original choice you would have won '+str(losecount)+' times, & switching caused you to win '+str(wincount/(cycles/100))+'% of the time.')
    #  this is the end results of a 100 million Monty Hall Problems
print(datetime.now() - startTime)
    #  says how long the program took to run. This is done by comparing the time the program started to the current time
    
    
    
    
    
    
    
    
    
    
    
    



# import random
# from datetime import datetime
# 
# 
# # set a start time to evaluate the efficiency of the script
# startTime = datetime.now()
# 
# # set counters to monitor the number of cycles and wins/losses
# 
# wincount = 0
# losecount = 0
# wincount2 = 0
# losecount2 = 0
# 
# for x in range(100):
#     # sets the doors and their contents. 1 = car, 0 = donkey
#     doors = [1, 2, 3]
#     contents = [1, 0, 0]
#     
#     # places the car inside a random door
#     random.shuffle(contents)
#     
#     # you pick a random door
#     pick = random.randint(0, 2)
# 
#     # moves your door to the end (this is to help make 'revealing' an
#     # incorrect door easier). This is done by removing the door you picked and
#     # inserting it at the end    
#     doors.insert(3, doors.pop(pick))
#     contents.insert(3, contents.pop(pick))
#     pick = 1
# 
# 
#     # checks if there is a donkey behind your door 
#     if contents[2] == 0:
#         # if there is, 'reveal' the only other door with a donkey. This is done
#         # by checking for the first door with a donkey behind it and deleting it
# 
#         doors.pop(contents.index(0))
#         contents.remove(0)
#     else:
#         # if there isn't, 'reveal' one of the donkeys. This is done by deleting
#         # the first item in the list. Because your pick is the car and it's been
#         # moved to the end of the list, the first item in the list is guaranteed
#         # to be a donkey
#         doors.pop(0)
#         contents.pop(0)
#     # this is effectively switching
# 
#     pick -= 1
#     if contents[pick] == 1:
#     # this is where the car is revealed
#         wincount += 1
#         wincount2 += 1
#     # if it is under your door, I add 1 to both wincounters
#     else:
#         losecount += 1
#         losecount2 += 1
#     # if the car is not under your door, I add 1 to both loss counters
#     if wincount2 + losecount2 == 3000000:
#         print('Over the past 3 million games, switching won you a car '+str(wincount2)+' times, while you won an ostrich '+str(losecount2)+' times, & switching caused you to win '+str(wincount2/30000)+'% of the time.')
#         wincount2 = 0
#         losecount2 = 0
#     # this segment is just showing the results of 3 million games, rather than
#     # waiting for the entire game to end. This is done by adding both of the 
#     # second counters
#     # together and checking if the sum = 3000000. Then both of the second
#     # counters are reset.
# 
# print('Over the past 100 million games, switching won you a car '+str(wincount)+' times, while you won an ostrich '+str(losecount)+' times, & switching caused you to win '+str(wincount/1000000)+'% of the time.')
# # this is the end results of a 100 million Monty Hall Problems
# 
# print(datetime.now() - startTime)
# # says how long the program took to run. This is done by comparing the time the
# # program started to the current time
#     
