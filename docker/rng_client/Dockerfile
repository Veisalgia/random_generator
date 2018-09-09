FROM python:3

WORKDIR /usr/src/app
ENV PYTHONPATH "${PYTHONPATH}:/"
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 1883
EXPOSE 9001

CMD [ "python","-u","./src/app/client.py" ]