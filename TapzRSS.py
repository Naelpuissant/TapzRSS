#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import config
import click
import utils.Crawler as Crawler
from utils.persistence.Persistence import Persistence


@click.command()
@click.option('--listen', '-l', is_flag=True, help='Run as listener mode.')
@click.option('--verbose', '-v', is_flag=True, help='Run as verbose mode.')
@click.option('--outputfile', '-f', default='./output/output.json', help='Set output file name')
@click.option('--outputype', '-t', default='JSON', type=click.Choice(['Json']), help='Set output file name')
def crawl(listen, verbose, outputfile):
    c = Crawler.Crawler(urls=config.URLS)
    if listen:
        c.listener = True
    if verbose:
        c.verbose = True
    if outputfile:
        c.outputfile = './output/' + outputfile
        
    c.run()


if __name__ == "__main__":
    crawl()