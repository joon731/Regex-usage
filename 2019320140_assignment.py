import re

## conf
INPUT = "./input.txt"
OUTPUT = "./output.txt"

def date_validity(month, day):
    if month == 2:
        if day > 28:
            return False
    elif month == 4 or month == 6 or month == 9 or month == 11:
        if day > 30:
            return False
    else:
        if day > 31:
            return False
    return True

def checksum_validity(match):

    match = match.replace("-", "")
    values = list(match)
    values.pop()
    multiplier = 2
    total = 0
    for i in range(len(values)):
        
        total += int(values[i]) * multiplier
        multiplier += 1

        if multiplier == 10:
            multiplier = 2
    
    total = total % 11
    total = 11 - total
    if total > 9:
        total = total % 10
    return(total)


def main():
    protectedBody = ""
    fres = open(OUTPUT, 'w', encoding = "UTF-8")
    with open(INPUT, 'r', encoding = "UTF-8") as fp:
        body = ''.join(fp.readlines())
        print ("** UNPROTECTED INPUT **")
        print (body) # Check the input file.

        pattern = re.compile(r'\d\d\d\d\d\d\s*-\s*\d\d\d\d\d\d\d')
        matches = pattern.findall(body)
        
        for match in matches:
            valid = True
            twenty_century = False
            matchCheck = match.replace(" ", "")

            year = int(matchCheck[0:2])
            month = int(matchCheck[2:4])
            day = int(matchCheck[4:6])
            gender = int(matchCheck[7])

            if year >= 24:
                twenty_century = True
            
            if date_validity(month, day) == False:
                print("Invalid Date: " + match)
                valid = False
                continue

            if (((twenty_century == True) and gender not in {1,2}) or ((twenty_century == False) and gender not in {3,4})):
                print("Invalid Gender: " + match)
                valid = False
                continue
            
            if(checksum_validity(matchCheck) != int(matchCheck[13])):
                print("Invalid Checksum: " + match)
                valid = False
                continue

            print("Valid Registration Number: " + match)
            body = body.replace(match, "******-*******")


        print ("** PROTECTED OUTPUT **")
        protectedBody = body
        print (protectedBody)
        fres.write(protectedBody)
        fres.close()

""" EXECUTE """
if __name__ == "__main__":
	main()

