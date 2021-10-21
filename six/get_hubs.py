
import click
import sys
import logging

from config import init_logging
from network.funcnet import FN

init_logging()

logger = logging.getLogger(__name__)

@click.command()
def make():
    fn = FN()


if __name__ == '__main__':
    make()