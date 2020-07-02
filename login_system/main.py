import json,sys
ans=int(input("Welcome to the dashboard. Type 1 if you want to signup. Type 2 if you want to login"))
if ans==1:
	print("You are now registering")
	while True:
		username=input("Enter your name")
		if username=="quit":
			break
		with open("data.json","r+") as f:
			data=json.load(f)
			for i in data.keys():
				if i==username:
					print("Username already exists")
					sys.exit()
		password=input("Enter the password")
		newdict={}
		newdict[username]=password
		print(newdict)
		with open("data.json","r+") as f:
			data=json.load(f)
			data.update(newdict)
			f.seek(0)
			json.dump(data,f)
if ans==2:
	print("Ok . Now enter the credentials")
	user_id=input("Enter the details")
	with open("data.json") as f:
		data=json.load(f)
		for i in data.keys():
			if i==user_id:
				print("user exists")
				pass_wd=input("Enter the password")
				if data[i]==pass_wd:
					print("Authentication successful")
					break
		else:
			print("user doesnt exists")
