#ABC Company uses AWS S3bucket to collect network equipment logs
#Said company uses Azure for it analytics uing S3 data
#automate automate pulling logs from S3and upload to Azure bucket every 12 am daily

import boto3
import urllib
import requests

url = "https://vimeo.com/showcase/7674137/feed/roku/6e7f763cbc"
title = "A greater passion"


def processUrl(url, title):
    response = requests.get(url)
    string = response.text
    string = string.replace("shortFormVideos", title)
    return string




def main():
    """Run main function."""
    processUrl(url, title)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

main()