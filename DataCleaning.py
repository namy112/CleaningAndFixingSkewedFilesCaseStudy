import csv
import os, re, time
#Readline function will take in the filename and use the filename to create a new temporoary file with datetime as a postfix.
def readLines(filename):
   
    timestr=time.strftime("%Y%m%d-%H%M%S")
    filenameSplit=filename.split('.')
    fileWriter= open (filenameSplit[0] + '_DataProcessed_' + timestr+ '.csv' ,'w') 
    
    with open(filename) as file:
        rows=file.readlines()
    
        cleanLines(rows,filename,fileWriter)

#cleanLines function will read each row from the input file and remove any spaces of "00:00" from each cell.
#Later ot will seperate each column with a comma seperator.
def cleanLines(rows,filename,fileWriter):
    
    newDataRow=[]
    for row in rows:
        #print(rows[0])
        dataFields=[]
        rowFixed=[]
        newDataRow = row.rstrip().replace("00:00:00","").split(',')
        cleanString(newDataRow,filename,fileWriter)
        
        
 #cleanString will remove any special charrectors.      
def cleanString (originalString,filename,fileWriter):
    cleanedString = []

    #Iterate through all the words in the argument string and clean the special and hidden characters 
    for word in originalString:
        cleanedWord = re.sub('[^A-Za-z0-9.:-]+', '', word, flags=re.IGNORECASE)
        cleanedString.append(cleanedWord)   
    
    if filename =='promotion.csv':
        fixRow(cleanedString, fileWriter)
    else:
        fileWriter.write(','.join(cleanedString) + '\n')
        #join function will reattached the fields
def fixRow(row,fileWriter):
    #fix the skewness in the data and creating a new file based on fixed position of the fields.
    promotionId= row[0]
    promotionDistrictId=row[1]
    promotionName=row[2]
    cost=row[-3]
    startDate=row[-2]
    endDate=row[-1]
    endIndex=int(len(row))-3
    mediaType= '|'.join (row[3 : endIndex])
    newDataRow= ','.join([promotionId,promotionDistrictId,promotionName,mediaType,cost,startDate,endDate])
    
    fileWriter.write(newDataRow + '\n')
    
    