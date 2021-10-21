""" funcnet

Gene Function Subnetwork

"""

import pandas as pd
import networkx as nx
import logging

from config import cfg

logger = logging.getLogger(__name__)

class FN:
    def __init__(self) -> None:
        
        self.networkfile = cfg['NETWORKFILE']

        linkdf = pd.read_csv(self.networkfile, sep="\t", header=None)
        linkdf.columns = ['source', 'target', 'weight']
        self.G = nx.from_pandas_edgelist(linkdf, 'source', 'target', 'weight', nx.Graph())

        logger.info('# of edges: {}'.format(self.G.number_of_edges()))
        logger.info('# of nodes: {}'.format(self.G.number_of_nodes()))



