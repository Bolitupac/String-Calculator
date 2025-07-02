#this program is used to calculate with text
import math
from functools import reduce
import operator


#prompt the user  to type in what to calculate. im calling this dirty because ill clean it by removing spaces
dirty_input = input("Prompt(words only eg five plus three): \n")

#now ill clean the input and split the words and put them in the clean input
clean_input = dirty_input.lower().split()
#this list will hold the values and signs after conversion to symbols
compute = []
#this will hold the final answer
final_answer = 0

#loop through the words in the input
for word in clean_input:
    #now, check and return the value for each number
    match word:
        case "zero":
            compute.append(0)
        case "one":
            compute.append(1)
        case "two":
            compute.append(2)
        case "three":
            compute.append(3)
        case "four":
            compute.append(4)
        case "five":
            compute.append(5)
        case "six":
            compute.append(6)
        case "seven":
            compute.append(7)
        case "eight":
            compute.append(8)
        case "nine":
            compute.append(9)
        case _:
            pass

#check the function to be computed mul
if "multiply" in clean_input or "times" in clean_input or "multiplied" in clean_input or "product" in clean_input:
    final_answer = math.prod(compute)
elif "divide" in clean_input or "divided" in clean_input:
    final_answer = reduce(operator.truediv, compute)
    print("divide")
elif "add" in clean_input or "sum" in clean_input or "plus" in clean_input:
    final_answer = sum(compute)
elif "subtract" in clean_input or "minus" in clean_input:
    final_answer = reduce(operator.sub, compute)
else:
    final_answer = "Couldnt get final answer (rephrase input or check spelling errors)"

print(final_answer)


#im adding this line so that ill test out how git branch works :)
#im adding this line so that ill test out how git branch works :)