import scrapy
from panoramafirm_crawler.items import Firma

class PanoramafirmSpider(scrapy.Spider):
    name = "panoramafirm"
    allowed_domains = ["panoramafirm.pl"]
    start_urls = [
        "http://panoramafirm.pl/serwis_komputer%C3%B3w/%C5%82%C3%B3dzkie,,%C5%82%C3%B3d%C5%BA"
    ]

    def parse(self, response):
        for sel in response.xpath("//li[contains(@class, 'vcard')]"):
            firma = Firma()
            try:
                firma['name'] = sel. \
                    xpath("*/h2/*/text()").extract()[0].encode('utf-8')
            except:
                firma['name'] = ""
            try:
                firma['panoramafirm'] = sel. \
                    xpath("*/h2/a/@href").extract()[0].encode('utf-8')
            except:
                firma['panoramafirm'] = ""
            try:
                firma['business'] = sel. \
                    xpath("//div[@id='tradeDesc']//text()"). \
                    extract()[0].encode('utf-8')
            except:
                firma['business'] = ""
            try:
                firma['url'] = sel. \
                    xpath("*/div[contains(@class, 'contactsLink')]"). \
                    css("a[class*=icon-link-ext]").xpath('@href'). \
                    extract()[0].encode('utf-8')
            except:
                firma['url'] = ""
            try:
                firma['email'] = sel. \
                    xpath("*/div[contains(@class, 'contactsLink')]"). \
                    css("a[class*=icon-mail]").xpath('@href'). \
                    extract()[0].encode('utf-8').split('mailto:')[1]
            except:
                firma['email'] = ""
            try:
                firma['phone'] = ''.join(sel. \
                    xpath("div[@class='contacts']/*/strong/text()"). \
                    extract()[0].encode('utf-8').strip().split(" "))
            except:
                try:
                    firma['phone'] = ''.join(sel. \
                        xpath("div[@class='contacts cross']/a//text()"). \
                        extract()[0].encode('utf-8').strip().split(" "))
                except:
                    firma['phone'] = ""
            try:
                firma['address'] = sel. \
                    xpath("div[@class='contacts']/*/following-sibling::text()"). \
                    extract()[0].encode('utf-8').strip()
            except:
                try:
                    firma['address'] = '; '. \
                        join(
                            [''.join(sel. \
                                xpath("div/div[@class='companyAddress popoverShow']/text()"). \
                                extract()).encode('utf-8').strip(),
                            sel. \
                                xpath("div/div[@class='companyAddress popoverShow']/*/text()"). \
                                extract()[0].encode('utf-8')])
                except:
                    firma['address'] = ""
            try:
                firma['description'] = \
                    ''.join(sel.xpath("div[@class='text hidePhone crl']//text()"). \
                    extract()).encode('utf-8').strip()
            except:
                firma['description'] = ""
            try:
                firma['facebook'] = sel. \
                    xpath("div/h2/a[contains(@class, 'facebookIcon')]/@href"). \
                    extract()[0].encode('utf-8')
            except:
                firma['facebook'] = ""

            yield firma
