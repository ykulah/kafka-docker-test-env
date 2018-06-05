#!/usr/bin/env python
import threading, logging, time
import multiprocessing
import sys
from kafka import KafkaConsumer, KafkaProducer
import datetime
import json

def TimestampMillisec64():
    return int((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds() * 1000) 

if __name__ == "__main__":
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
        )
    producer = KafkaProducer(bootstrap_servers='{}:{}'.format(sys.argv[1],sys.argv[2]))

    filepath = '/workspace/Amazon_Unlocked_Mobile.csv'
    while True:  
        with open(filepath) as fp:  
            line = fp.readline()
            while line:
                v = dict()
                v["customField"] = line
                producer.send(topic=sys.argv[3], value=json.dumps(v), timestamp_ms=TimestampMillisec64())
                print "Pushed: " + line
                line = fp.readline()
                #time.sleep(1)
    producer.close()
