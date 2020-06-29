import requests
username=input("Enter your username :")
url="https://api.github.com/users/"+username
if requests.get(url):
	dic=requests.get(url).json()
	for i in dic.keys():
		print(f'{i} - {dic[i]}')
else:
	print("username doesn't exist , try again !")
