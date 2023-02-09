def removeConsecutiveRepeatingCharacters(inputstring):
    '''
    first we check the given string is empty or not.if it is empty it returns the inputstring.
    otherwise it compares the characheters of the string.if they are same it shifts the character one by one until 
    it reaches the new charachter.
    '''
    if len(inputstring)<2:
        return inputstring
    if inputstring[0]!=inputstring[1]:
        return inputstring[0]+removeConsecutiveRepeatingCharacters(inputstring[1:])
    return removeConsecutiveRepeatingCharacters(inputstring[1:])
inputstring="ssaggfdddasss"
output=removeConsecutiveRepeatingCharacters(inputstring)
print(output)
