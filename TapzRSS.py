#!/usr/bin/env python3
import config
import click
import utils.Crawler as Crawler


@click.command()
@click.option('--listen', '-l', is_flag=True, help='Run as listener mode.')
@click.option('--verbose', '-v', is_flag=True, help='Run as verbose mode.')
@click.option('--output', help='Store result into a json file')
def crawl(listen, output):
    c = Crawler.Crawler(urls=config.URLS)
    if listen:
        c.listener = True
    if output:
        c.output = output
    c.run()


if __name__ == "__main__":
    crawl()