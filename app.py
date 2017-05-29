import os, time, datetime

import RPi.GPIO as GPIO
import picamera
import boto


print 'taking picture'
timestamp = str(time.time()).split('.')[0]
file_name = timestamp + '.jpg'
with picamera.PiCamera() as camera:
    time.sleep(5) # plenty of time to focus
    camera.resolution = (2592, 1944) # for the pi camera v1.2
    camera.vflip = False
    camera.hflip = False
    camera.capture(file_name)

print 'uploading image to s3'
connection = boto.s3.connect_to_region(
    'eu-west-1',
    aws_access_key_id=os.environ['S3_KEY'],
    aws_secret_access_key=os.environ['S3_SECRET']
)
bucket = connection.get_bucket(os.environ['S3_BUCKET'])
key = bucket.new_key(file_name)
key.set_contents_from_filename(file_name)
key.make_public()

print 'all done, deleting image'
os.remove(file_name)
