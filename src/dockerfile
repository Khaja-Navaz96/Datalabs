from alpine:latest

RUN apk add --no-cache python3-dev \
        && pip3 install --upgrade pip

WORKDIR /maincode

COPY . /maincode
RUN pip3 --no-cache-dir install -r requirements.txt

RUN pip3 --no-cache-dir install mysql-server python3-mysqldb








EXPOSE 5000



CMD ["python3","app.py"]
