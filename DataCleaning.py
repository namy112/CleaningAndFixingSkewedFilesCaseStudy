import csv
import os, re, time

def readLines(filename):
   
    timestr=time.strftime("%Y%m%d-%H%M%S")
    filenameSplit=filename.split('.')
    fileWriter= open (filenameSplit[0] + '_DataProcessed_' + timestr+ '.csv' ,'w') 
    
    with open(filename) as file:
        rows=file.readlines()
    
        cleanLines(rows,filename,fileWriter)

def cleanLines(rows,filename,fileWriter):
    
    newDataRow=[]
    for row in rows:
        #print(rows[0])
        dataFields=[]
        rowFixed=[]
        newDataRow = row.rstrip().replace("00:00:00","").split(',')
        cleanString(newDataRow,filename,fileWriter)
        
        
        
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
            
def fixRow(row,fileWriter):
     
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
    
    