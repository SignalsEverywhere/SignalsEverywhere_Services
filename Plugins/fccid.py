import re
from bs4 import BeautifulSoup
import requests


#Function to input code from bot and return the response
#def grab_general(fccid):
#    fccID = fccid
#    url = ('http://fccid.io/%s' % fccID)
#    fcc_query = requests.get(url)
#    content = fcc_query.text
#
#    rel = '<h1>FCC ID 2ADUIESP-12</h1>(.*?)</h4>'
#    rg = re.compile(rel, re.IGNORECASE | re.DOTALL)
#    m = rg.search(content.decode('utf-8'))
#    if m:
#        general_data = m.group(1)
#        print("FCC Holder: (" + general_data + ")" + "\n")
#
#    send_back = general_data
#    return send_back

def start(pageRequest, id):
    #page = requests.get("http://fccid.io/%s" % fccid)
    #print(page.content)
    soup = BeautifulSoup(pageRequest.content, "lxml")

    title = soup.findAll("title")
    dev = re.findall("<title>FCC ID " + id + ".(.*?)</title>", str(title))


    freqs = soup.findAll("div", { "class" : "panel panel-primary" })
    print(dev)
    #print(soup.prettify())
    #soup = soup.select('<h4>')
    #print(soup)

def manu(pageRequest, id):
    #page = requests.get("http://fccid.io/%s" % fccid)
    soup = BeautifulSoup(pageRequest.content, "lxml")
    title = soup.findAll("title")
    data = re.findall("<title>FCC ID " + id + ".(.*?)</title>", str(title))
    return(data[0])


def freq(pageRequest):
    #page = requests.get("http://fccid.io/%s" % fccid)
    soup = BeautifulSoup(pageRequest.content, "lxml")
    freqs = soup.findAll("div", {"class": "panel panel-primary"})
    #printme = re.findall("lower=(.*?)</a></td><td>",str(freqs))
    try:
        printme = re.findall("lower=(.*?)</a>", str(freqs))
        printme2 = re.findall(r'>.*?z', str(printme[0]))
        finalfreq = printme2[0].replace('>', 'Frequency range: ')
        return(finalfreq)
    except:
        return(' ')





def power(pageRequest):
    #page = requests.get("http://fccid.io/%s" % fccid)
    soup = BeautifulSoup(pageRequest.content, "lxml")
    try:
        power = soup.findAll("div", {"class": "panel panel-primary"})
        radiostring = re.findall("Hz(.*?)_blank", str(power))
        stripped = re.findall("</td><td>(.*?)</td><td>", str(radiostring[0]))
        pwout = stripped[0]
        #print(pwout)
        return('Power: ' + pwout)
    except:
        return('Power: ??')





def internal(pageRequest):
    #page = requests.get("http://fccid.io/%s" % fccid)
    soup = BeautifulSoup(pageRequest.content, "lxml")
    grabclass = soup.findAll("div", {"class": "tab-pane fade active in"})
    graburl = re.findall("href.*?Internal Photo", str(grabclass))
    try:
        edit1 = graburl[0].replace('href="', 'Internal Photos: <')
        #edit2 = edit1.replace('">Internal Photo', '.pdf')
        edit2 = re.sub('">Int(.*)', '.pdf', edit1)
        #print(edit2)
        edit3 = edit2 + ">"
        return(edit3)
    except:
        return(' ')

def diagram(pageRequest):
    #page = requests.get("http://fccid.io/%s" % fccid)
    soup = BeautifulSoup(pageRequest.content, "lxml")
    grabclass = soup.findAll("div", {"class": "tab-pane fade active in"})
    graburl = re.findall("href.*?Block Diagram", str(grabclass))
    try:
        edit1 = graburl[0].replace('href="', 'Block Diagram: ')
        edit2 = edit1.replace('">Block Diagram', '.pdf')
        return (edit2)
    except:
        return (' ')

def schematics(pageRequest):
    #page = requests.get("http://fccid.io/%s" % fccid)
    soup = BeautifulSoup(pageRequest.content, "lxml")
    grabclass = soup.findAll("div", {"class": "tab-pane fade active in"})
    graburl = re.findall("href.*?Schematics<", str(grabclass))
    try:
        edit1 = graburl[0].replace('href="', 'Schematics: <')
        edit2 = edit1.replace('">Schematics<', '.pdf')
        edit3 = edit2 + ">"
        return (edit3)
    except:
        return (' ')

def part(pageRequest):
    #page = requests.get("http://fccid.io/%s" % fccid)
    soup = BeautifulSoup(pageRequest.content, "lxml")
    try:
        power = soup.findAll("div", {"class": "panel panel-primary"})
        radiostring = re.findall("ecfr.io/Title(.*?)</", str(power))
        stripped = re.findall(">(.*?)\Z", str(radiostring[0]))
        #pwout = stripped[0]
        #print(stripped)
        #print(stripped[0])
        return('Part: ' + str(stripped[0]))
    except:
        return('')

def isValid(pageRequest):     #Checks to see if an ID is valid based on scraped output from the fccid website
    #page = requests.get("http://fccid.io/%s" % fccid)
    soup = BeautifulSoup(pageRequest.content, "lxml")
    search = soup.findAll("div", {"class": "jumbotron"})
    strip = re.findall("May Not Be Valid", str(search))
    try:
        if strip[0] == "May Not Be Valid":
            return(False)
    except:
        return(True)

#print(isValid('EW780-5735-02'))

#part('R6TRFM308RD')
#power('GB8SD-700A')
#internal('EW780-5735-02')
#start('EW780-5735-02')
#freq('EW780-5735-02')
###to do, remove bad char and replace with nice looking shit on print out
