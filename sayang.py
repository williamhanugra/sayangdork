#!/usr/bin/env python3

import requests
import urllib3
import argparse
from concurrent.futures import ThreadPoolExecutor

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def openFile(filename):
    with open(filename) as f:
        content = f.readlines()
    return [f"https://github.com/search/count?q=%22{arg_menu.company}%22%20{x.strip().replace(' ','%20')}&type=Code" for x in content]

def save_value_file(value: str, file: str):
    myFile = open(file, 'a+')
    myFile.write(value)
    myFile.close()

def github(target):
    try:
        result = requests.get(target, headers=burp0_headers, cookies=burp0_cookies).text
        result = result.split('type="Code">')[1].split('</span>')[0].replace("K","000")
        target = target.replace("/count","")
        target2 = target.split("%22%20")[1].split("&type=Code")[0]

        if result != "0" and arg_menu.output:
            save_value_file(f"{result},{target2},{target}\n",arg_menu.output)
        if arg_menu.silent and result != "0":
                print(f"{target}")
        elif result != "0":
                print(f"{bcolors.OKGREEN}[+]({result}){bcolors.ENDC} DORK = {target2} | {target}")
    except:
        print(f"CEK_SESSION_KEMUNGKINAN_RATE_LIMIT_ATAU_HARUS_LOGIN_LAGI")
        save_value_file(f"CEK_SESSION_KEMUNGKINAN_RATE_LIMIT_ATAU_HARUS_LOGIN_LAGI\n",arg_menu.output)

def start(filename):
    try:
        RANGE = openFile(filename)
        executor = ThreadPoolExecutor(max_workers=MAX_CONECTION_THREAD)
        executor.map(github, RANGE)
        executor.shutdown(wait=True)
    except Exception as e: 
        print(e)
        pass
TIME_SLEEP = 3

urllib3.disable_warnings()

parser_arg_menu = argparse.ArgumentParser(
    prog='python3 sayang.py', formatter_class=lambda prog: argparse.HelpFormatter(prog, max_help_position=20)
)
parser_arg_menu.add_argument(
    "--company", help="Domain name Eg. tesla.com",
    metavar="tesla.com", required=True
)
parser_arg_menu.add_argument(
    "--dork", help="dork file",
    metavar="dorks.txt", required=True
)
parser_arg_menu.add_argument(
    "--session", help="user_session_github",
    metavar="user_session_github", required=True
)
parser_arg_menu.add_argument(
    "--thread", help="Eg. 50 (Default: 20)",
    metavar="50", default=20, required=False
)
parser_arg_menu.add_argument(
    "--output", help="output file name", required=False
)
parser_arg_menu.add_argument(
    "--silent", help="clean output", action='store_true', required=False
)

arg_menu = parser_arg_menu.parse_args()
MAX_CONECTION_THREAD = int(arg_menu.thread)

burp0_cookies = {"user_session": arg_menu.session}
burp0_headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36", "Connection": "close"}

start(arg_menu.dork)
