
import time
import random
import wget
import requests


i=920

urls=[]
folder="get_files/down/"


while i<=1250:
    i_s=str(i)
    url="http://www.theweekinchess.com/zips/twic%sg.zip" % (i_s)
    urls.append(url)


    i+=1


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.54 Safari/537.36'}

for url in urls:
    time.sleep(random.random()*3)
    # Downloading the file by sending the request to the URL
    req = requests.get(url, headers=headers)
    
    # Split URL to get the file name
    filename = url.split('/')[-1]
    
    # Writing the file to the local file system
    with open(filename,'wb') as output_file:
        output_file.write(req.content)
    print('Downloading Completed')