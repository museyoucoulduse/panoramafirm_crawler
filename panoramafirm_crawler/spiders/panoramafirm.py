import scrapy
from panoramafirm_crawler.items import Firma

class PanoramafirmSpider(scrapy.Spider):
    name = "panoramafirm"
    allowed_domains = ["panoramafirm.pl"]
    start_urls = [
        "http://panoramafirm.pl/serwis_komputer%C3%B3w/%C5%82%C3%B3dzkie,,%C5%82%C3%B3d%C5%BA"
    ]

    def parse(self, response):
        firma = Firma()
        firma['name'] = response.xpath("//li[contains(@class, 'vcard')]/*/h2/*/text()")[0].extract().encode('utf-8')
        firma['business'] = response.xpath("//div[@id='tradeDesc']//text()"). \
            extract()[0].encode('utf-8')
        firma['url'] = response. \
            xpath("//li[contains(@class, 'vcard')]/*/div[contains(@class, 'contactsLink')]")[0]. \
            css("a[class*=icon-link-ext]").xpath('@href'). \
            extract()[0].encode('utf-8')
        firma['email'] = response. \
            xpath("//li[contains(@class, 'vcard')]/*/div[contains(@class, 'contactsLink')]")[0]. \
            css("a[class*=icon-mail]").xpath('@href'). \
            extract()[0].encode('utf-8')
        firma['phone'] = response. \
            xpath("//li[contains(@class, 'vcard')]/div[@class='contacts']/*/strong/text()")[0]. \
            extract().encode('utf-8')
        firma['address'] = response. \
            xpath("//li[contains(@class, 'vcard')]/div[@class='contacts']/*/following-sibling::text()")[0]. \
            extract().encode('utf-8')

        yield firma
