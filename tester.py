import requests

r1 = requests.get('http://localhost:8000')
r2 = requests.get('http://localhost:7000')
r3 = requests.get('http://localhost:5000')

if r1.text == r2.text == r3.text:
    print("\n\n\n\t Servers are running & The outputs of them are the same. Finnaly it works!")
else:
    print(r1.text)
    print(r2.text)
    print(r3.text)
    print("something goes wrong!!!!")
