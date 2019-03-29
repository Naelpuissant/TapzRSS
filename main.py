import config
import utils.Crawler as Crawler

def main():
    c = Crawler.Crawler(urls=config.URLS)
    c.run()

if __name__ == "__main__":
    main()