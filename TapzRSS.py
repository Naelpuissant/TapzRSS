#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import config
import click
import utils.Crawler as Crawler
from utils.persistence.Persistence import Persistence


@click.command()
@click.option('--listen', '-l', is_flag=True, help='Run as listener mode.')
@click.option('--verbose', '-v', is_flag=True, help='Run as verbose mode.')
@click.option('--output', '-o', help='Store result into a json file')
def crawl(listen, verbose, output):
    c = Crawler.Crawler(urls=config.URLS)
    if listen:
        c.listener = True
    if verbose:
        c.verbose = True
    if output:
        c.output = './output/' + output
        
    c.run()


if __name__ == "__main__":
    crawl()