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
