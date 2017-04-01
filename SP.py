##==================================================================================================
##Question 1
##Given a word, return the total number of key presses required to spell the word using the keypad.
##==================================================================================================

###over here, the user will be asked to key in a word, which will be split into a list of alphabet

##name = raw_input("Input:")
##wordlist = list(name)
##print wordlist
##count = 0
##
##for i in wordlist: 
##  
##    if i == 'a' or i == 'd' or i == 'g' or i == 'j' or i == 'm' or i == 'p' or i == 't' or i == 'w':
##        count += 1   #if the alphabet is the 1st alphabet in the keypad, that means only need to press the key once
##        
##    elif i == 'b' or i == 'e' or i == 'h' or i == 'k' or i == 'n' or i == 'q' or i == 'x':
##        count += 2    #if the alphabet is the 2nd alphabet in the keypad
## 
##    elif i == 's' or i == 'z':
##        count += 4    #if the alphabet is the 4th alphabet in the keypad
##
##    else:
##        count += 3    #if the alphabet is the 3rd alphabet in the keypad
##        
##print "Output:" + str(count)  #the output has to be string


   
##==================================================================================================
##Question 2
##Given a word, return the number that the word could represent.
##==================================================================================================


##name = raw_input("Input:")
##wordlist = list(name)
##print wordlist  
##answer = []     #declare an empty string
##
##for i in wordlist:      #add the corresponding number of the alphabet to the string
##    if i == 'a' or i == 'b' or i == 'c':
##        answer.append('2')
##
##    elif i == 'd' or i == 'e' or i == 'f':
##        answer.append('3')
##        
##    elif i == 'g' or i == 'h' or i == 'i' :
##        answer.append('4')
##
##    elif i == 'j' or i == 'k' or i == 'l' :
##        answer.append('5')
##
##    elif i == 'm' or i == 'n' or i == 'o' :
##        answer.append('6')
##
##    elif i == 'p' or i == 'q' or i == 'r' or i == 's' :
##        answer.append('7')
##
##    elif i == 't' or i == 'u' or i == 'v' :
##        answer.append('8')
##
##    else:
##        answer.append('9')
##
##print 'Output:' + ''.join(answer)   # the join() method join the list of number to an empty string with no spacing in between


#====================================================================================================     
##Question 3
##Given a number, return all possible letter combinations that the number could represent.
##==================================================================================================


##number = raw_input("Input:")
##numlist = list(number)
##print numlist
##
##import itertools    #itertools is a function that creates iterators for efficient looping
##
##letters_map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', 
##               '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}
##
##def possible_words(phone_number):
##    letters_to_combine = (letters_map[digit] for digit in phone_number)
##    for letters_group in itertools.product(*letters_to_combine):    #itertools.product() gives a combination of the letters
##        yield ''.join(letters_group)
##
##print 'Output:' + str(list(possible_words(number)))



#==================================================================================================
##Question 4
##Given a number, return all possible word combinations (from Dictionary- pls see attached file) that the number could represent.
##==================================================================================================


number = raw_input("Input:")
numlist = list(number)
#print numlist

datafile = open("WordsRTF.RTF","rt")
contents = datafile.read().splitlines() #to remove all the lines between words
outputlist=[] # declare an empty string as the output
#datafile.close()
#print(contents)

import itertools

letters_map = {'2':'abc', '3':'def', '4':'ghi', '5':'jkl', 
               '6':'mno', '7':'pqrs', '8':'tuv', '9':'wxyz'}

def possible_words(phone_number):
    letters_to_combine = (letters_map[digit] for digit in phone_number)
    for letters_group in itertools.product(*letters_to_combine):
        yield ''.join(letters_group)

# print 'Output:' + str(list(possible_words(number)))


for line in contents:
	for dic in list(possible_words(number)):
		if line.strip("\\") == dic:     # compare each input word with the dictionary
			outputlist.append(line.strip("\\"))

print 'Output:' + str(outputlist)
