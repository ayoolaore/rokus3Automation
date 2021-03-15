import boto3
import json
import urllib
import validators
import requests

urls = []

titles = []

dataList = {}
data = ""
stringWord = ""

def yesno():
    """Simple Yes/No Function."""

    ans = input("would you like to upload new showcase? (y/n/exit/d)\n").strip().lower()
    if ans not in ['y', 'n', 'exit', 'd']:
        print(f'{ans} is invalid, please try again...')
        return yesno()
    if ans == 'y':
        return True
    if ans == 'd':
        ans2 = input("Are you sure you want to delete an item y/n \n")
        if ans2 == 'y':
            deleteTitle = input("Enter Title you would like deleted")
            dataList.pop(deleteTitle, None)
            print(f'{dataList.pop(deleteTitle,None)} has been deleted from library')
        else:
            yesno()
    if ans == 'exit':
        return False
    return False


def content():
    newUrl = input("Enter new Showcase URl \n")
    newTitle = input("Enter new Showcase title \n")

    valid = validators.url(newUrl)
    if valid != True or newTitle == "":
        print("Wrong URL format or Title cannot be empty")
        return content()
    # append any new content
    urls.append(newUrl)
    titles.append(newTitle)


def grabFiles():
    titleFile = open('titles.txt', 'r+')
    urlFile = open('urls.txt', 'r+')

    urlLine = urlFile.readline()
    while urlLine:
        urlLine = urlLine.rstrip()
        urls.append(urlLine)  # append lines from url file to array
        urlLine = urlFile.readline()

    titleLine = titleFile.readline()
    while titleLine:
        titleLine = titleLine.rstrip()
        titles.append(titleLine)  # append lines from url file to array
        titleLine = titleFile.readline()

    if yesno():
        content()
    urlFile.seek(0)
    titleFile.seek(0)
    for item in urls:
        # print(item)
        urlFile.write("%s\n" % item)
    for stuff in titles:
        # print(stuff)
        titleFile.write("%s\n" % stuff)
    urlFile.close()
    titleFile.close()


def processUrl(url, title):
    response = requests.get(url)
    string = response.text

    string = string + ","
    string = string[1:-1]
    string = string.replace("shortFormVideos", title)
    string = string.replace("movies", title)
    dataList1 = eval(string)
    dataList.update(dataList1)
    #return string #returns string of content from url after replacing title
    # print(urls)
    # print(titles)


def parseThrough():
    string = ""

    for i in range(len(urls)):
        processUrl(urls[i], titles[i])
        #print(dataList)
    #return string


def jsonProcess():
    parseThrough()
    #data = json.loads(string)
    data = json.dumps(dataList, indent=4)
    f = open("data.json", "w")
    f.write(data)
    f.close()
    #data = json.loads(data)
    #print(data)
# def addContent():
# context = yesno()
# if context == True:
# content()
'''def upload():
    s3 = boto3.resource('s3',
                        aws_access_key_id='AKIAQ5G23FWMXLRVSKXR',
                        aws_secret_access_key='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')
    s3object = s3.Object('rokucotr', 'Json Files/data.json')

    s3object.put(
        Body=(bytes(data.encode('UTF-8'))),
        ContentType='application/json',
        ACL='public-read'
    )
    print("file merged and uploaded to S3, SUCESS!!!")'''


def main():
    grabFiles()
    #stringWord = parseThrough()
    jsonProcess()
    #print(stringWord)
    #print(urls)
    #print(titles)


main()
