FROM python:3.10

ENV HOME /app
WORKDIR $HOME

ADD requirements.txt .
RUN python3 -m pip install --no-cache -r requirements.txt
ADD . .

CMD ['python', 'app.py']
