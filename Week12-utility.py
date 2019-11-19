# Roy Lundeen
# CSCI 102 - Section B
# Week 12 Part A


# PrintOutput
def PrintOutput(string):
    print('OUTPUT', string)

# LoadFile
def LoadFile(string, lines):
    with open(string, 'r') as file:
        contents = file.readlines()
        return(contents)
