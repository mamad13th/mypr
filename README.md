# mypr
my first project, a simple web service written by three framework Django, Flask and fastapi. The input could be anything and the output is the same for any input

first of all you should install the requirements that write in the requirements.txt . run the command:


///  pip3 install --no-cache-dir -r requirements.txt ///


then you should run the servers 

Run djangopage.py & flaskpage/flaskpage.py & fastapipage.py with the below commands:


///
python3 djangopage.py

python3 flaskpage/flaskpage.py 

python fastapipage.py
///


Django runs on http://127.0.0.1:8000

Flask runs on http://127.0.0.1:7000

Fastapi runs on http://127.0.0.1:5000

all the servers run by UVICORN

when they completly run you can run the tester

tester.py is a test for comparing html content of them but you can check http headers manually 

in docker you should just pull and run. Commands for docker:

///
docker pull mamad13th/mypr

docker run -it --rm mypr
///
