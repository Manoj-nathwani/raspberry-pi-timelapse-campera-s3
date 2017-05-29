# Raspberry Pi Timelapse Camera to S3

- Takes a picture using the [Raspberry Pi camera module](https://www.raspberrypi.org/products/camera-module-v2/)
- Uploads the images to [AWS S3](https://aws.amazon.com/s3/) and sets the image to expire in 24hrs

# Setup
Setup raspberry pi by following:
https://gist.github.com/Manoj-nathwani/51d312eb20011cd2526024f072a417f9

Install everything
```
$ sudo apt-get install python-imaging
$ pip install -r requirements.txt
$ sudo raspi-config # enable camera
```

Set up your enviroment variables by editing your `/etc/environment` and adding:
```
export S3_KEY=xxxxxxxxxxxxxxxxxxxx
export S3_SECRET=xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
export S3_BUCKET=xxxxxxxxxxxxxxxxxxxx
```
Then simply add app.py as a cronjob & give the pi a reboot
