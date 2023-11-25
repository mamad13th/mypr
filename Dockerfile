FROM ubuntu:jammy
RUN apt-get update
RUN apt-get upgrade -y
RUN apt-get install -y python3
RUN apt-get install -y python3-pip
COPY . .
RUN pip3 install --no-cache-dir -r requirements.txt
EXPOSE 5000 7000 8000
CMD python3 fastapipage.py &
RUN sleep 2
CMD python3 djangopage.py &
RUN sleep 2
CMD python3 flaskpage/flaskpage.py &
RUN sleep 2
CMD python3 tester.py > result.txt &
RUN sleep 2
CMD echo "$(cat result.txt)"

