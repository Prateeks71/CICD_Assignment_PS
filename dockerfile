FROM python:latest 
WORKDIR /app
COPY data ./app/data
COPY train.py  ./app/train.py
COPY requirements.txt ./app/requirements.txt
RUN pip install --no-cache-dir -r ./app/requirements.txt
RUN python ./app/train.py
COPY test.py ./app/test.py
EXPOSE 9000
#WORKDIR .
#RUN cd /app
ENTRYPOINT [ "python","./app/test.py" ]
#CMD ["ML_MODEL_TEST","test.py","--host","0.0.0.0","--port","9000"]