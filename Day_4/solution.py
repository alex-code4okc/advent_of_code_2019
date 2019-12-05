def isIncreasingOrPlateau(number):
    '''Takes a number as a string and checks that each digit from left to right is increasing or stays that same'''
    increasing = True

    compare = number[0]
    for digit in number[1:]:
        if( int(digit) >= int(compare)):
            pass
        else:
            increasing = False
            return increasing
        compare = digit
    return increasing

def isDoubleDigitPresent(number):
    '''Takes a number as a string and checks if there is at least 1 repeating adjacent digit'''
    present = False

    compare = number[0]
    for digit in number[1:]:
        if(int(digit)==int(compare)): # found at least 1 repeat return true
            present = True
            return present
        else:
            pass # keep searching
        compare = digit
    return present # present would be false if returned at this level

def isNotGrouped(number):
    '''Takes a number as a string, and checks that the number does not contain a repeated group larger than 2'''
    double = False
    number_counts = {}
    for digit in range(0,10,1): # not including 10
        number_counts[digit] = number.count(str(digit))
        # number passes if there is at least 1 digit with a count of 2
    for key,value in number_counts.items():
        if(value == 2):
            double = True
            return double
    return double # no unique double found

    
start = 265275 # valid number starts with 266XXX
end = 781584 # valid number ends with 77XXXX

criteria = []
for number in range(start,end+1,1):
    s_number = str(number)
    if(isIncreasingOrPlateau(s_number)):
        if(isDoubleDigitPresent(s_number)):
            if(isNotGrouped(s_number)):
                criteria.append(number)

print(len(criteria))


# a dictionary with '1': count of '1's, '2': count of '2's etc
# if there are multiple repeated digits, the largest of these must be a pair
# otherwise it does not meet the criteria