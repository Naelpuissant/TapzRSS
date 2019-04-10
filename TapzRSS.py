#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import config
import click
import utils.Crawler as Crawler


@click.command()
@click.option('--listen', '-l', is_flag=True, help='Run as listener mode.')
@click.option('--verbose', '-v', is_flag=True, help='Run as verbose mode.')
@click.option('--outputfile', '-f', default='./output/output.json', help='Set output file name')
@click.option('--outputtype', '-t', default='JSON', type=click.Choice(['JSON', 'STDOUT']), help='Set output file name')
def crawl(listen, verbose, outputfile, outputtype):
    c = Crawler.Crawler(urls=config.URLS)
    if listen:
        c.listener = True
    if verbose:
        c.verbose = True
    c.output_file = outputfile
    c.output_type = outputtype
    c.run()


if __name__ == "__main__":
    crawl()