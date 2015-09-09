# Hackathon Concierge Bell
Raspberry Pi that uses [IDOL OnDemand](https://idolondemand.com) [face detection API](https://www.idolondemand.com/developer/apis/detectfaces#overview) to alert Developer Evangelists of attendees who need help at an event.

# How it works
Hackathon attendee who wants help comes over to the "bell". The onboard camera will check to see there is person actually standing there. When it detects a face via [IDOL OnDemand](https://idolondemand.com) [face detection API](https://www.idolondemand.com/developer/apis/detectfaces#overview), the large button (aka the"bell") illuminates. The attendee then holds the "bell" down until another LED turns on indicating the Raspberry Pi is sending the image via [Twilio](https://www.twilio.com/). The image of the attendee is then delivered to the Developer Evangelists at the event so they can easily find them once they are available.

## Setup
* ssh into the Raspberry Pi via the following command `ssh pi@192.168.1.131`
* Download a VNC on Raspberry Pi and Computer. Tuturial [here](https://www.raspberrypi.org/documentation/remote-access/vnc/)
* Other commands can be found [here](https://www.raspberrypi.org/guides/teachers/vnc-classroom-guide.md) to help start on Raspberry Pi
* Once on the Raspberry Pi, cd into the directory of the app and run `sudo python index.py`

## Libraries used
* [HP IDOL OnDemand Python Wrapper](https://github.com/HP-IDOL-OnDemand/iod-python)
* [Twilio Python Wrapper](https://github.com/twilio/twilio-python)
* [AWS Python Wrapper (aka Boto)](https://github.com/boto/boto)
* [Raspberry Pi Camera Module](https://www.raspberrypi.org/help/camera-module-setup/)

## Hardware
* [1 Raspberry Pi](https://www.adafruit.com/product/2358)
* [1 Raspberry Pi Camera Module](https://www.adafruit.com/products/1367)
* [1 Massive button](https://www.adafruit.com/products/1185)
* [1 LED](https://www.adafruit.com/products/300)
* [1 Wifi Dongle](https://www.adafruit.com/products/814)
