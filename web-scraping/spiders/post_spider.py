""" Import scrapy package """
import scrapy
import time
""" Inheritance spider from scrapy package """

class PostSpider(scrapy.Spider):
    """ Name of crawler """
    name = 'posts'

    """ Set number of product we want to get their information """
    item_number = 300

    """
    This list set start urls to crawl data from those
    (we have 4 groups of product in this crawler)
    """

    start_urls = [
        'https://www.houzz.com/products/sofas-and-sectionals',
        'https://www.houzz.com/products/dining-tables',
        'https://www.houzz.com/products/beds-and-headboards',
        'https://www.houzz.com/products/artwork'
    ]
    """
        First function:
        this method find product ulr and give it to second function
        to capture data from it.
        In the second part of this function we go to new page 
        and find new product.
    """

    def parse(self, response):

        """Find products urls in page"""
        for href in response.css('a[class="hz-product-card__link"]::attr(href)'):
            url = response.urljoin(href.extract())
            """ 
                Check how many item does captured
                if we have enough item exit scraping! 
            """
            if self.item_number < 1:
                time.sleep(5)
                return
            if url:
                self.item_number -= 1
                """give url to second function to capture data from it"""
                yield scrapy.Request(url, callback=self.parse_dir_contents)

        """Find new page address"""
        next_page = response.css('a.hz-pagination-link--next::attr(href)').get()

        """If new page is exist
        just call back this function for new page and keep
        going until new page be None!
        """
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)

    """Second function:
        Find html tags product element in product page
        and capture them and added to dictionary variable
        and finally yield it. 
    """

    def parse_dir_contents(self, response):
        """create dictionary item"""
        item = dict()
        """
            Temp list for added url picture to text processing
            on them and get picture with better quality.
        """
        temp = []

        """ Find product specifications """
        item['name'] = response.css('span.view-product-title::text').get()
        item['tags'] = response.css('li.product-keywords__word::text').extract()
        """Get just 2 pictures !!!"""
        first_urls = response.css('.alt-images__thumb img::attr(src)').extract()[:2]

        """
            If product have one picture we have empty list in above list!
            and we should check it out if have empty list go to capture 
            one picture in middle of the page!
        """
        if not first_urls:
            temp.append(response.css('img.view-product-image-print::attr(src)').get())
        else:
            """ If list not empty 
                we processing picture urls to find pictures with better quality.
            """
            for url in first_urls:
                temp.append(url.split('-w')[0].replace('fimgs', 'simgs').replace('_', '_9-'))

        item['pics'] = temp

        # delete the temp list
        del temp

        """yield item and write it to file!"""
        yield item
