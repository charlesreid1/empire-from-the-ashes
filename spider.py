from bs4 import BeautifulSoup
from urllib.request import urlopen
from urllib.parse import urlparse
import io, os, re

def main():
    baseurl = "http://baencd.freedoors.org/Books/Empire%20From%20the%20Ashes/"
    myurl = baseurl + "0743435931___1.htm"
    text = urlopen(myurl).read()
    soup = BeautifulSoup(text,'html.parser')
    body = soup.body
    text = []

    nexturl = ""
    for a in body.find_all('a'):
        if(a.text=="Next"):
            nexturl = a.attrs['href']

    while(nexturl!=""):
        print("Processing url: %s"%(myurl))

        path = urlparse(myurl).path
        fileparts = path.split('/')
        htm = fileparts[-1]
        match = re.search("([0-9]{1,})\.htm",htm)
        try:
            fileid = match[1]
        except TypeError:
            print("All done.")
            exit()


        text = urlopen(myurl).read()
        soup = BeautifulSoup(text,'html.parser')
        body = soup.body
        text = []

        for p in body.find_all('p'):
            if('onmouseover' in p.attrs):
                text.append(p.text)

        ofile = "empire_from_the_ashes_%s.txt"%(fileid)
        print("Writing to file: %s"%(ofile))
        with open(ofile,'w') as f:
            f.write("\n".join(text))

        nexturl = ""
        for a in body.find_all('a'):
            if(a.text=="Next"):
                nexturl = baseurl + a.attrs['href']
                break

        myurl = nexturl


if __name__=="__main__":
    main()

