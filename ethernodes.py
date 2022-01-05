# -*- coding: utf-8 -*-  

import logging
import requests
import os

class Ethernodes:
    def __init__(self):
        pass

    def make_request(self):
        url = 'https://www.ethernodes.org/data?draw=36&' \
              'columns%5B0%5D%5Bdata%5D=id&' \
              'columns%5B0%5D%5Bname%5D=&' \
              'columns%5B0%5D%5Bsearchable%5D=true&' \
              'columns%5B0%5D%5Borderable%5D=true&' \
              'columns%5B0%5D%5Bsearch%5D%5Bvalue%5D=&' \
              'columns%5B0%5D%5Bsearch%5D%5Bregex%5D=false&' \
              'columns%5B1%5D%5Bdata%5D=host&' \
              'columns%5B1%5D%5Bname%5D=&' \
              'columns%5B1%5D%5Bsearchable%5D=true&' \
              'columns%5B1%5D%5Borderable%5D=true&' \
              'columns%5B1%5D%5Bsearch%5D%5Bvalue%5D=&' \
              'columns%5B1%5D%5Bsearch%5D%5Bregex%5D=false&' \
              'columns%5B2%5D%5Bdata%5D=isp&' \
              'columns%5B2%5D%5Bname%5D=&' \
              'columns%5B2%5D%5Bsearchable%5D=true&' \
              'columns%5B2%5D%5Borderable%5D=true&' \
              'columns%5B2%5D%5Bsearch%5D%5Bvalue%5D=&' \
              'columns%5B2%5D%5Bsearch%5D%5Bregex%5D=false&' \
              'columns%5B3%5D%5Bdata%5D=country&' \
              'columns%5B3%5D%5Bname%5D=&' \
              'columns%5B3%5D%5Bsearchable%5D=true&' \
              'columns%5B3%5D%5Borderable%5D=true&' \
              'columns%5B3%5D%5Bsearch%5D%5Bvalue%5D=&' \
              'columns%5B3%5D%5Bsearch%5D%5Bregex%5D=false&' \
              'columns%5B4%5D%5Bdata%5D=client&' \
              'columns%5B4%5D%5Bname%5D=&' \
              'columns%5B4%5D%5Bsearchable%5D=true&' \
              'columns%5B4%5D%5Borderable%5D=true&' \
              'columns%5B4%5D%5Bsearch%5D%5Bvalue%5D=&' \
              'columns%5B4%5D%5Bsearch%5D%5Bregex%5D=false&' \
              'columns%5B5%5D%5Bdata%5D=clientVersion&' \
              'columns%5B5%5D%5Bname%5D=&columns%5B5%5D%5Bsearchable%5D=true&' \
              'columns%5B5%5D%5Borderable%5D=true&columns%5B5%5D%5Bsearch%5D%5Bvalue%5D=&' \
              'columns%5B5%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B6%5D%5Bdata%5D=os&' \
              'columns%5B6%5D%5Bname%5D=&columns%5B6%5D%5Bsearchable%5D=true&columns%5B6%5D%5Borderable%5D=true&' \
              'columns%5B6%5D%5Bsearch%5D%5Bvalue%5D=&' \
              'columns%5B6%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B7%5D%5Bdata%5D=lastUpdate&' \
              'columns%5B7%5D%5Bname%5D=&columns%5B7%5D%5Bsearchable%5D=true&' \
              'columns%5B7%5D%5Borderable%5D=true&columns%5B7%5D%5Bsearch%5D%5Bvalue%5D=&' \
              'columns%5B7%5D%5Bsearch%5D%5Bregex%5D=false&columns%5B8%5D%5Bdata%5D=inSync&' \
              'columns%5B8%5D%5Bname%5D=&columns%5B8%5D%5Bsearchable%5D=true&columns%5B8%5D%5Borderable%5D=true&' \
              'columns%5B8%5D%5Bsearch%5D%5Bvalue%5D=&columns%5B8%5D%5Bsearch%5D%5Bregex%5D=false&order%5B0%5D%5Bcolumn%5D=8&' \
              'order%5B0%5D%5Bdir%5D=desc&start=0&' \
              'length=50&search%5Bvalue%5D=United%20States&' \
              'search%5Bregex%5D'
            #   'length=50&search%5Bvalue%5D=United%20States&' \
        try:
            return requests.get(url).json()['data']
        except Exception as e:
            logging.error(e)
            return None

    def get_peers(self):
        nodes = []

        data = self.make_request()
        if not data:
            return []

        for i in data:
            print(i)
            if not i['inSync']:
                continue
            nodes.append('enode://{id}@{host}:{port}'.format(id=i['id'], host=i['host'], port=i['port']))

        return nodes

    def make_peers_file(self, file_path):
        with open(file_path, 'w') as peer_file:
            peer_file.writelines([peer + '\n' for peer in self.get_peers()])

    def import_peers(self):
        peers=self.get_peers()
        with open('./peers.txt', 'w') as peer_file:
            peer_file.writelines([peer + '\n' for peer in peers])
        # for peer in peers:
        #     command=f"geth.exe attach http://localhost:8545 --exec \"admin.addPeer(\'{peer}\')\""
        #     os.system(command)
            # print(command)

    def load_peers(self):
        with open('./peers.txt', 'r') as peer_file:
            peer=peer_file.readline()
            while peer:
                # print(peer)
                command=f"gethr.exe attach http://localhost:8545 --exec \"admin.addPeer(\'{peer[:-1]}\')\""
                os.system(command)
                peer=peer_file.readline()

    def load_peers_linux(self):
        with open('./peers.txt', 'r') as peer_file:
            peer=peer_file.readline()
            while peer:
                # print(peer)
                command="/root/projects/geth/build/bin/geth  attach http://localhost:8545 --exec \"admin.addPeer(\'"
                command+=peer[:-1]
                command+="\')\""
                os.system(command)
                peer=peer_file.readline()

    