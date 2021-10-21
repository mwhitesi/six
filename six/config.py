
import logging
import os

cfg = {
    'NETWORKFILE': os.path.join( os.path.dirname(os.path.realpath(__file__)), '../../data/network/HumanNet-FN-20211020.tsv')
}

def init_logging():
    logging.basicConfig(level=logging.DEBUG)