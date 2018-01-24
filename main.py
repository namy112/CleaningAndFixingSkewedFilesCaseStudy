from DataCleaning import readLines



def main ():
    filename1='transactions.csv'
    instanceOne=readLines(filename1)
    filename2='promotion.csv'
    instanceTwo=readLines(filename2)
    filename3='product.csv'
    instanceThree=readLines(filename3)
    
    
    print(instanceOne)
    print(instanceTwo)
    print(instanceThree)
     

main()