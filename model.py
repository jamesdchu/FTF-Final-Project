##FTF-Final Project

#This function converts data from mongodb to a list
def convert(data):
    converted = data.find({})
    convertedData = []
    for i in converted:
        convertedData.append(i)
    return(convertedData.reverse())


