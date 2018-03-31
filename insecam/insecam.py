from requests import session
from bs4 import BeautifulSoup
import socket
from http.server import BaseHTTPRequestHandler, HTTPServer
import time
import threading
import random

header = {
    'Host': 'www.insecam.org',
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
    'Accept-Language': 'en-US,en;q=0.5',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1'
}

url = "http://www.insecam.org/en/bynew/?page="
hostName = "localhost"
hostPort = 8000
link = ""
current = []

class MyServer(BaseHTTPRequestHandler):

    def do_GET(self):
        global link
        global current
        self.send_response(200)
        self.send_header('Content-type','text/html')
        self.end_headers()
        self.wfile.write("<html><head><meta http-equiv=\"refresh\" content=\"30\" /></head>\n".encode('utf-8'))
        #if link == "":
        #    link = self.getNextSite()
        if not current:
            current = getNewSite(random.randint(1,1000))
        self.wfile.write("<body bgcolor=\"#000000\" background=>\n".encode('utf-8'))
        self.wfile.write("<table style=\"width:100%\" align=\"right\" \n<tr>\n ".encode('utf-8'))
        #for l in current:
        threading.Timer(0, self.getNextSite()).start()
        tag = '<th> <img src=\"'+ link +'\" width="1300cm" height="750cm"> </th>\n '
        self.wfile.write(tag.encode('utf-8'))
        self.wfile.write("</tr>\n ".encode('utf-8'))
        self.wfile.write("</body>\n </html>".encode('utf-8'))

    def getNextSite(self):
        global link
        global current
        if not current:
            current = getNewSite(random.randint(1,1000))
        link = current.pop(0)

def run_server():
    myServer = HTTPServer((hostName, hostPort), MyServer)
    print(time.asctime(), "Server Starts - %s:%s" % (hostName, hostPort))

    try:
        myServer.serve_forever()
    except KeyboardInterrupt:
        pass

    myServer.server_close()
    print(time.asctime(), "Server Stops - %s:%s" % (hostName, hostPort))

def getNewSite(n):
    with session() as c:
        response = c.get(url=url+str(n), headers=header)
        html_root = response.text
        soup = BeautifulSoup(html_root, 'html.parser')
        links = [x['src'] for x in soup.findAll('img',{'class': "thumbnail-item__img img-responsive"})]
        return links

run_server()
