# coding=utf-8
import os
import logging
from ethernodes import Ethernodes

# PEERS_FILE_PATH = os.environ.get('PEERS_FILE_PATH', './peers.txt')

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    en = Ethernodes()
    # en.import_peers()
    # https://www.ethernodes.org/tor-seed-nodes
    # 使用前把节点从上面的网站复制到peers.txt文件中
    en.load_peers()

    # en.make_peers_file(PEERS_FILE_PATH)
    # logging.info('File {} created'.format(PEERS_FILE_PATH))