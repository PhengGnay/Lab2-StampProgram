
# start 
# get the numbers of sheets
# sheets / 5
# round answer to next numbers
# output the result to the user
# end

sheet = 1000
answer = round(sheet / 5)
print("sheet is : ", sheet)
print("The answer is: ", answer)
print("rounded is: ", rounded)



def calculate(sheet):
    answer = round(sheet / 5)
    rounded = round(answer, 1)
    print("sheet is : ", sheet)
    print("The answer is: ", answer)
    print("rounded is: ", rounded)
    return rounded


calculate(16)
