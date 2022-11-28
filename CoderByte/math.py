def MathChallenge(num):
    num = str(num)
    a = [int(i) for i in num]
    if len(a) < 2:
        return "not possible"

    def recursiveHealperFunc(updatedArray, updatedSum):

        if len(updatedArray) == 1:
            if  updatedSum + updatedArray[0] == 0:
                return '+'     
            elif updatedSum - updatedArray[0] == 0:
                return '-'
            else:
                return 'not possible'

        string2 = recursiveHealperFunc(updatedArray[1:], updatedSum - updatedArray[0])

        if string2 != 'not possible':
            return '-' + string2
        
        string1 = recursiveHealperFunc(updatedArray[1:], updatedSum + updatedArray[0])

        if string1 != 'not possible':
            return '+' + string1
        
        return 'not possible'
    return recursiveHealperFunc(a[1:], a[0])


print(MathChallenge(26712))


