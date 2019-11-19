# Roy Lundeen
# CSCI 102 - Section B
# Week 12 Part A


# PrintOutput
def PrintOutput(string):
    print('OUTPUT', string)

# LoadFile
def LoadFile(string):
    with open(string, 'r') as file:
        contents = file.readlines()
        return(contents)
    
# UpdateString
def UpdateString(string, new, index):
    newlist = []
    for char in string:
        newlist.append(char)
    
    newlist[index] = new
    string = ''.join(newlist)
    return string

# FindWordCount
def FindWordCount(list1, string):
    count = 0
    for x in list1:
        if string in x:
            count += x.count(string)
    return count

# ScoreFinder
def ScoreFinder(list1, list2, string):
    for x in range(len(list1)):
        if (string.lower()) in ((list1[x]).lower()):
            score = list2[x]
            return 'OUTPUT {} got a score of {}'.format(list1[x], score)
        else:
            found = False
    if found == False:
        return 'player not found.'

# Union
def Union(list1, list2):
    newlist = list1 + list2
    return newlist

# Intersection
def Intersection(list1, list2):
    newlist = []
    for x in list1:
        if x in list2:
            newlist.append(x)
    return newlist
