import pandas as pd
import re

AC = 43560
propNam =[]
propCity =[]
propSale =[]
propUse =[]
propLoc =[]
propSite =[]
propSaleD =[]
propSize =[]
propSF =[]
propSAC =[]
propSSF =[]
propNOI =[]
propDis =[]
propPark =[]

def menu():
    print("LAND COMPARE\n")
    fileName = input("Enter the text file to be read: ")
    readFile(fileName)

def readFile(fileName):
    regex = re.compile(r'(?::).*$')
    with open(fileName) as fp:
        for line in fp:
            if "Property Name:" in line:
                res = re.search(regex,line)
                res = re.sub('[:]','',res.group())
                propNam.append(res)

            elif "Location:" in line:
                res = re.search(regex,line)
                res = re.sub('[:]','',res.group())
                propCity.append(res)

            elif "Sale Price:" in line:
                res = re.search(regex,line)
                res = re.sub('[:]','',res.group())
                propSale.append(res)

            elif "Tenancy Type:" in line:
                res = re.search(regex, line)
                res = re.sub('[:]', '', res.group())
                propUse.append(res)

            elif "Condition:" in line:
                res = re.search(regex, line)
                res = re.sub('[:]', '', res.group())
                propLoc.append(res)

            elif "Sale Date:" in line:
                res = re.search(regex, line)
                res = re.sub('[:]', '', res.group())
                propSaleD.append(res)

            elif "Site Area:" in line:
                res = re.search(regex, line)
                res = re.sub('[:]', '', res.group())
                propSize.append(res)

            elif "NOI:" in line:
                res = re.search(regex, line)
                res = re.sub('[:]', '', res.group())
                propNOI.append(res)

            elif "Distance from Subject:" in line:
                res = re.search(regex, line)
                res = re.sub('[:]', '', res.group())
                propDis.append(res)

            elif "Number of Parking Spaces:" in line:
                res = re.search(regex, line)
                res = re.sub('[:]', '', res.group())
                propPark.append(res)

    print("Done")
    fp.close()

    df = pd.DataFrame(
        {'Name': propNam,
         'City': propCity,
         'Sale Price': propSale,
         'NOI': propNOI,
         'Use': propUse,
         'Quality': propLoc,
         'SDate': propSaleD,
         'pDis': propDis,
         'Park': propPark,
         'Size': propSize
         }
    )
    df.to_csv('Cost_Approach.csv',index=False)

def main():
    menu()

if __name__ == '__main__':
    main()
