from bs4 import BeautifulSoup
import re, io, glob

for htm in glob.glob("*.htm"):
    match = re.search("([0-9][0-9])\.htm",htm)
    fileid = match[1]

    with io.open(htm,'r',encoding="ISO-8859-1") as f:
        html_doc = f.read()

    soup = BeautifulSoup(html_doc, 'html.parser')
    body = soup.body

    text = []
    for p in body.find_all('p'):
        if('onmouseover' in p.attrs):
            text.append(p.text)

    ofile = "mutineersmoon_%s.txt"%(fileid)
    print("writing file %s"%(ofile))
    with open(ofile,'w') as f:
        f.write("\n".join(text))

