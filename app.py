import os, time, datetime

import operator
from PIL import Image
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

print 'running histogram equalization on picture'
# credit: http://effbot.org/zone/pil-histogram-equalization.htm
def equalize(h):
    lut = []
    for b in range(0, len(h), 256):
        step = reduce(operator.add, h[b:b+256]) / 255
        n = 0
        for i in range(256):
            lut.append(n / step)
            n = n + h[i+b]
    return lut
    im = Image.open(file_name)
    lut = equalize(im.histogram())
    im = im.point(lut)
    im.save(file_name)

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
