FROM python:2.7

RUN mkdir /workspace
ADD kafkaProduce.py /workspace

ADD Amazon_Unlocked_Mobile.csv /workspace
ENV SECURE_ENV=1

RUN echo $KAFKA_HOST
WORKDIR /workspace

RUN pip install kafka-python

CMD python kafkaProduce.py $KAFKA_HOST $KAFKA_PORT $TOPIC
