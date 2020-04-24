#-*- coding: utf-8 -*-
#scrape data from termbin
#
# ooooo   ooooo ooooooooooooo ooooooooo.
# `888'   `888' 8'   888   `8 `888   `Y88.
#  888     888       888       888   .d88'
#  888ooooo888       888       888ooo88P'
#  888     888       888       888
#  888     888       888       888
# o888o   o888o     o888o     o888o
#     made by <L 3 0 N 1 D U S>
import requests
import time
def main():
    file = open("list.txt", "r")
    list = file.readlines()
    for string in list:
        r = requests.get(F"https://termbin.com/{string}")
        check_status = r.status_code
        data = r.text
        if check_status == 200:
            new = open(f"{string}.txt", "w")
            new.write(data, "w")
            print("[+] saving: {string} to file...")
            file.close()
            time.sleep(0.3)
        else:
            print(f"skipping {string}: 404")
            time.sleep(0.3)

main()
