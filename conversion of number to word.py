string_no = []
def len1(number):
	if number in range(0,10):
		if number == 0:
			return " zero"
		if number == 1:
			return " one"
		if number == 2:
			return " Two"
		if number == 3:
			return " Three"
		if number == 4:
                	return " Four"
        	if number == 5:
                	return " Five"
        	if number == 6:
                	return " Six"
        	if number == 7:
                	return " Seven"
  		if number == 8:
                	return " Eight"
        	if number == 9:
                	return " Nine"
	

def len2(number):
	integer = int(number[0]+number[1])
	if integer in range(10,100,10):
		if integer == 10:
			return " Ten"
                if integer == 20:
                        return " Twenty"
                if integer == 30:
                        return " Thirty"
                if integer == 40:
                        return " Fourty"
                if integer == 50:
                        return " Fifty"
                if integer == 60:
                        return " Sixty"
                if integer == 70:
                        return " Seventy"
                if integer == 80:
                        return " Eighty"
                if integer == 90:
                        return " Ninety"
	if integer in range(11,20):
		if integer == 11:
                        return " eleven"
                if integer == 12:
                        return " Twelve"
                if integer == 13:
                        return " Thirteen"
                if integer == 14:
                        return " Fourteen"
                if integer == 15:
                        return " Fifteen"
                if integer == 16:
                        return " Sixteen"
                if integer == 17:
                        return " Seventeen"
                if integer == 18:
                        return " Eighteen"
                if integer == 19:
                        return " Nineteen"

	if int(number[0]) in range(2,10):
		if int(number[0]) == 2:
			return " Twenty"+len1(int(number[1]))
		if int(number[0]) == 3:
                        return " Thirty"+len1(int(number[1]))
		if int(number[0]) == 4:
                        return " Fourty"+len1(int(number[1]))
		if int(number[0]) == 5:
                        return " Fifty"+len1(int(number[1]))
		if int(number[0]) == 6:
                        return " Sixty"+len1(int(number[1]))
		if int(number[0]) == 7:
                        return " seventy"+len1(int(number[1]))
		if int(number[0]) == 8:
                        return " Eighty"+len1(int(number[1]))
		if int(number[0]) == 9:
                        return " Ninety"+len1(int(number[1]))
	if int(number[0]) == 0:
		return len1(int(number[1]))
		
		
def len3(number):
	temp = number[1:3]
	if int(number[0]) == 1:
		return " one hundred and"+len2(temp)
	if int(number[0]) == 2:
                return " two hundred and"+len2(temp)
	if int(number[0]) == 3:
                return " three hundred and"+len2(temp)
	if int(number[0]) == 4:
                return " four hundred and"+len2(temp)
	if int(number[0]) == 5:
                return " five hundred and"+len2(temp)
	if int(number[0]) == 6:
                return " six hundred and"+len2(temp)
	if int(number[0]) == 7:
                return " seven hundred and"+len2(temp)
	if int(number[0]) == 8:
                return " eight hundred and"+len2(temp)
	if int(number[0]) == 9:
                return " nine hundred and"+len2(temp)
	if int(number[0]) == 0:
		return len2(temp)

		
def len4(number):
	temp = number[1:len(number)]
	if int(number[0]) == 1:
                return " one thousand"+len3(temp)
        if int(number[0]) == 2:
                return " two thousand"+len3(temp)
        if int(number[0]) == 3:
                return " three thousand"+len3(temp)
        if int(number[0]) == 4:
                return " four thousand"+len3(temp)
        if int(number[0]) == 5:
                return " five thousand"+len3(temp)
        if int(number[0]) == 6:
                return " six thousand"+len3(temp)
        if int(number[0]) == 7:
                return " seven thousand"+len3(temp)
        if int(number[0]) == 8:
                return " eight thousand"+len3(temp)
        if int(number[0]) == 9:
                return " nine thousand"+len3(temp)
        if int(number[0]) == 0:
                return len3(temp)


def len5(number):
	temp = number[2:len(number)]	
	t1   = number[0:2]
	if int(number[0]) == 0:
		return len4(number[1:len(number)])
	else:
		return len2(t1)+" Thousand"+len3(temp)


def len6(number):
	temp = number[1:len(number)]
        if int(number[0]) == 1:
                return " one Lac"+len5(temp)
        if int(number[0]) == 2:
                return " two lac"+len5(temp)
        if int(number[0]) == 3:
                return " three lac"+len5(temp)
        if int(number[0]) == 4:
                return " four lac"+len5(temp)
        if int(number[0]) == 5:
                return " five lac"+len5(temp)
        if int(number[0]) == 6:
                return " six lac"+len5(temp)
        if int(number[0]) == 7:
                return " seven lac"+len5(temp)
        if int(number[0]) == 8:
                return " eight lac"+len5(temp)
        if int(number[0]) == 9:
                return " nine lac"+len5(temp)
        if int(number[0]) == 0:
                return len5(temp)

	
def len7(number):
        temp = number[2:len(number)]
        t1   = number[0:2]
        if int(number[0]) == 0:
                return len6(number[1:len(number)])
        else:
                return len2(t1)+" lac"+len5(temp)


def len8(number):
	temp = number[1:len(number)]
        if int(number[0]) == 1:
                return " one crore"+len7(temp)
        if int(number[0]) == 2:
                return " two crore"+len7(temp)
        if int(number[0]) == 3:
                return " three crore"+len7(temp)
        if int(number[0]) == 4:
                return " four crore"+len7(temp)
        if int(number[0]) == 5:
                return " five crore"+len7(temp)
        if int(number[0]) == 6:
                return " six crore"+len7(temp)
        if int(number[0]) == 7:
                return " seven crore"+len7(temp)
        if int(number[0]) == 8:
                return " eight crore"+len7(temp)
        if int(number[0]) == 9:
                return " nine crore"+len7(temp)
        if int(number[0]) == 0:
                return len7(temp)

def len9(number):
        temp = number[2:len(number)]
        t1   = number[0:2]
        if int(number[0]) == 0:
                return len8(number[1:len(number)])
        else:
                return len2(t1)+" crore"+len7(temp)


def len10(number):
	temp = number[3:len(number)]
        t1   = number[0:3]
        if int(number[0]) == 0:
                return len9(number[1:len(number)])
        else:
                return len3(t1)+" crore"+len7(temp)

def len11(number):
	temp = number[4:len(number)]
        t1   = number[0:4]
        if int(number[0]) == 0:
                return len10(number[1:len(number)])
        else:
                return len4(t1)+" crore"+len7(temp)



def len12(number):
	temp = number[5:len(number)]
        t1   = number[0:5]
        if int(number[0]) == 0:
                return len11(number[1:len(number)])
        else:
                return len5(t1)+" crore"+len7(temp)

def len13(number):
	temp = number[6:len(number)]
        t1   = number[0:6]
        if int(number[0]) == 0:
                return len12(number[1:len(number)])
        else:
                return len6(t1)+" crore"+len7(temp)
def len14(number):
	temp = number[7:len(number)]
        t1   = number[0:7]
        if int(number[0]) == 0:
                return len13(number[1:len(number)])
        else:
                return len7(t1)+" crore"+len7(temp)


def len15(number):
	temp = number[8:len(number)]
        t1   = number[0:8]
        if int(number[0]) == 0:
                return len14(number[1:len(number)])
        else:
                return len8(t1)+" crore"+len7(temp)





	
a = list(str(raw_input("************************ENTER A VALUE***********************************\n")))

if len(a) == 1:
	print "\n"+len1(int(a[0])) +"\n"
if len(a) == 2:
        print "\n"+len2(a)+"\n"

if len(a) == 3:
        print "\n"+len3(a)+"\n"

if len(a) == 4:
        print "\n"+len4(a)+"\n"

if len(a) == 5:
        print "\n"+len5(a)+"\n"

if len(a) == 6:
        print "\n"+len6(a)+"\n"

if len(a) == 7:
        print "\n"+len7(a)+"\n"

if len(a) == 8:
        print "\n"+len8(a)+"\n"

if len(a) == 9:
        print "\n"+len9(a)+"\n"

if len(a) == 10:
        print "\n"+len10(a)+"\n"

if len(a) == 11:
        print "\n"+len11(a)+"\n"

if len(a) == 12:
        print "\n"+len12(a)+"\n"

if len(a) == 13:
        print "\n"+len13(a)+"\n"

if len(a) == 14:
        print "\n"+len14(a)+"\n"

if len(a) == 15:
	print "\n"+len15(a)+"\n"




	
