def check(numbers):
	count=0
	for i in range(len(numbers)):
		if numbers[i]=='0' or  numbers[i]=='1':
			count=count+0
		else:
			count=count+1
	if count==0:
		return True
	else:
		return "something is wrong in your function"
		
def convert(number):
	string=str(number)
	revstr=string[::-1]
	if check(revstr) == True:
		decimal=int(revstr)
		finalsum=0
		for i in range(0,len(revstr)):
			digit=revstr[i]
			numdigit=int(digit)
			final=numdigit*(2**(i))
			finalsum=final+finalsum
#		print(check(revstr))	
		return finalsum
def printing_answer(input):
	if convert(input) == None:
		print("You have not entered a string",input," this contains digits other than 0 or 1 . please try again")
	else:
		print("You have given the binary input ",input, "and its decimal value is " , convert(input))
userinput=input("Enter the binary input consisting of 0 or 1 ")
printing_answer(userinput)


