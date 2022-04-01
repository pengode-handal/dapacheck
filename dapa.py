#Copyright Babwa Wibu AKA Kenzawaa
from colorama import Fore
b = '\033[1m'+Fore.LIGHTBLUE_EX
red = '\033[1m'+Fore.LIGHTRED_EX
g = '\033[1m'+Fore.LIGHTGREEN_EX
c = '\033[1m'+Fore.LIGHTCYAN_EX
w = '\033[1m'+Fore.LIGHTWHITE_EX
import requests
import argparse
from bs4 import BeautifulSoup

def getUrl(url):
    urls = []
    with open(url, "r") as ufile:
        semua = ufile.readlines()
        for i in range(len(semua)):
            urls.append(semua[i].strip('\n'))
        return urls

def scan(web: str):
    data = {
	"url": web,
	"pa": "pa",
	"mr": "mr",
	"ss": "ss",
	"go": "Gaskan"
}
    url = 'http://v1.exploits.my.id:1337/?tools=dapa' #Makasi Unknownsec buat webna:v 
    res = requests.post(url, data=data)
    soup = BeautifulSoup(res.content, 'html.parser')
    nganu = soup.find('pre').text
    return b+nganu.replace('[+] Loading ... ( 1 sites )', '').replace('[~] Done', '')


parse = argparse.ArgumentParser()
parse.add_argument('-d', '--domain', help='Domainya')
parse.add_argument('-f', '--file', help='Mass scanner, input file list')
args = parse.parse_args()

if args.domain:
    print(scan(args.domain))
elif args.file:
    uhh = getUrl(args.file)
    for semua in uhh:
        print(scan(semua))
    print(c+'Done')
else:
    print(red+'Input Argument')
    