import scrapy
from panoramafirm_crawler.items import Firma
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors import LinkExtractor

class PanoramafirmSpider(CrawlSpider):
    name = "panoramafirm"
    download_delay = 6
    allowed_domains = ["panoramafirm.pl"]
    start_urls = [
        # ## wielkopolska informatyka
        # "http://panoramafirm.pl/szukaj?k=informatyka&l=wielkopolskie",
        # ## wielkopolskie systemy i uslugi telekomunikacyjne
        # "http://panoramafirm.pl/szukaj?k=systemy+i+us%C5%82ugi+telekomunikacyjne&l=wielkopolskie",
        # ## wielkopolskie systemy i technologie multimedialne
        # "http://panoramafirm.pl/szukaj?k=systemy+i+technologie+multimedialne&l=wielkopolskie",
        # ## wielkopolskie stacje radiowe i telewizyjne
        # "http://panoramafirm.pl/szukaj?k=stacje+radiowe+i+telewizyjne&l=wielkopolskie",
        # ## wielkopolskie sprzet radiokomunikacyjny
        # "http://panoramafirm.pl/szukaj?k=sprz%C4%99t+radiokomunikacyjny&l=wielkopolskie",
        # ## wielkopolskie sprzet i centrale telefoniczne
        # "http://panoramafirm.pl/szukaj?k=sprz%C4%99t+i+centrale+telefoniczne&l=wielkopolskie",
        # ## wielkopolskie sieci komputerowe i integracja systemow
        # "http://panoramafirm.pl/szukaj?k=sieci+komputerowe+i+integracja+system%C3%B3w&l=wielkopolskie",
        # ## wielkopolskie serwisy informacyjne
        # "http://panoramafirm.pl/szukaj?k=serwisy+informacyjne&l=wielkopolskie",
        # ## wielkopolskie serwis komputerow
        # "http://panoramafirm.pl/szukaj?k=serwis+komputer%C3%B3w&l=wielkopolskie",
        # ## wielkopolskie oprogramowanie komputerowe
        # "http://panoramafirm.pl/szukaj?k=oprogramowanie+komputerowe&l=wielkopolskie",
        # ## wielkopolskie operatorzy komunikacyjni
        # "http://panoramafirm.pl/szukaj?k=operatorzy+telekomunikacyjni&l=wielkopolskie",
        # ## wielkopolskie odzyskiwanie i ochrona danych komputerowych
        # "http://panoramafirm.pl/szukaj?k=odzyskiwanie+i+ochrona+danych+komputerowych&l=wielkopolskie",
        # ## wielkopolskie internet
        # "http://panoramafirm.pl/szukaj?k=internet&l=wielkopolskie",
        # ## wielkopolskie audyty oprogramowania i sprzetu komputerowego
        # "http://panoramafirm.pl/szukaj?k=audyty+oprogramowania+i+sprz%C4%99tu+komputerowego&l=wielkopolskie",
        # ## wielkopolskie anteny
        # "http://panoramafirm.pl/szukaj?k=anteny&l=wielkopolskie",

        # # lodzkie anteny
        # "http://panoramafirm.pl/szukaj?k=anteny&l=%C5%82%C3%B3dzkie",
        # # lodzkie audyty oprogramowania i sprzetu komputerowego
        # "http://panoramafirm.pl/szukaj?k=audyty+oprogramowania+i+sprz%C4%99tu+komputerowego&l=%C5%82%C3%B3dzkie",
        # # lodzkie informatyka
        # "http://panoramafirm.pl/szukaj?k=informatyka&l=%C5%82%C3%B3dzkie",
        # # lodzkie internet
        # "http://panoramafirm.pl/szukaj?k=internet&l=%C5%82%C3%B3dzkie",
        # # lodzkie odzyskiwanie i ochrona danych komputerowych
        # "http://panoramafirm.pl/szukaj?k=odzyskiwanie+i+ochrona+danych+komputerowych&l=%C5%82%C3%B3dzkie",
        # # lodzkie operatorzy komunikacyjni
        # "http://panoramafirm.pl/szukaj?k=operatorzy+telekomunikacyjni&l=%C5%82%C3%B3dzkie"
        # # lodzkie oprogramowanie komputerowe
        # "http://panoramafirm.pl/szukaj?k=oprogramowanie+komputerowe&l=%C5%82%C3%B3dzkie",
        # # lodzkie serwis komputerow
        #  "http://panoramafirm.pl/szukaj?k=serwis+komputer%C3%B3w&l=%C5%82%C3%B3dzkie",
        # # lodzkie serwisy informacyjne
        # # brak wynikow
        # # lodzkie sieci komputerowe i integracja systemow
        # "http://panoramafirm.pl/szukaj?k=sieci+komputerowe+i+integracja+system%C3%B3w&l=%C5%82%C3%B3dzkie",
        # # lodzkie sprzet i centrale telefoniczne
        # "http://panoramafirm.pl/szukaj?k=sprz%C4%99t+i+centrale+telefoniczne&l=%C5%82%C3%B3dzkie",
        # # lodzkie sprzet radiokomunikacyjny
        # "http://panoramafirm.pl/szukaj?k=sprz%C4%99t+radiokomunikacyjny&l=%C5%82%C3%B3dzkie",
        # # lodzkie systemy i uslugi telekomunikacyjne
        # "http://panoramafirm.pl/szukaj?k=systemy+i+us%C5%82ugi+telekomunikacyjne&l=%C5%82%C3%B3dzkie",
        # # lodzkie systemy i uslugi multimedialne
        # "http://panoramafirm.pl/szukaj?k=systemy+i+technologie+multimedialne&l=%C5%82%C3%B3dzkie",
        # # lodzkie stacje radiowe i telewizyjne
        # "http://panoramafirm.pl/szukaj?k=stacje+radiowe+i+telewizyjne&l=%C5%82%C3%B3dzkie",

        # poznan it
        "http://panoramafirm.pl/szukaj?k=informatyka&l=Pozna%C5%84+%28wielkopolskie%29",
        "http://panoramafirm.pl/szukaj?k=internet&l=Pozna%C5%84+%28wielkopolskie%29",
        "http://panoramafirm.pl/szukaj?k=systemy+i+us%C5%82ugi+telekomunikacyjne&l=Pozna%C5%84+%28wielkopolskie%29",
        "http://panoramafirm.pl/szukaj?k=systemy+i+technologie+multimedialne&l=Pozna%C5%84+%28wielkopolskie%29",
        "http://panoramafirm.pl/szukaj?k=sieci+komputerowe+i+integracja+system%C3%B3w&l=Pozna%C5%84+%28wielkopolskie%29",
        "http://panoramafirm.pl/szukaj?k=serwisy+informacyjne&l=Pozna%C5%84+%28wielkopolskie%29",
        "http://panoramafirm.pl/szukaj?k=serwis+komputer%C3%B3w&l=Pozna%C5%84+%28wielkopolskie%29",
        "http://panoramafirm.pl/szukaj?k=oprogramowanie+komputerowe&l=Pozna%C5%84+%28wielkopolskie%29",
        "http://panoramafirm.pl/szukaj?k=operatorzy+telekomunikacyjni&l=Pozna%C5%84+%28wielkopolskie%29",
        "http://panoramafirm.pl/szukaj?k=sprz%C4%99t+radiokomunikacyjny&l=Pozna%C5%84+%28wielkopolskie%29",
        "http://panoramafirm.pl/szukaj?k=odzyskiwanie+i+ochrona+danych+komputerowych&l=Pozna%C5%84+%28wielkopolskie%29",
        "http://panoramafirm.pl/szukaj?k=audyty+oprogramowania+i+sprz%C4%99tu+komputerowego&l=Pozna%C5%84+%28wielkopolskie%29",
        "http://panoramafirm.pl/szukaj?k=sprz%C4%99t+i+centrale+telefoniczne&l=Pozna%C5%84+%28wielkopolskie%29",
        "http://panoramafirm.pl/szukaj?k=stacje+radiowe+i+telewizyjne&l=Pozna%C5%84+%28wielkopolskie%29",
        "http://panoramafirm.pl/szukaj?k=anteny&l=Pozna%C5%84+%28wielkopolskie%29",

        # lodz it
        # "http://panoramafirm.pl/serwis_komputer%C3%B3w/%C5%82%C3%B3dzkie,,%C5%82%C3%B3d%C5%BA",
        # "http://panoramafirm.pl/szukaj?k=audyty+oprogramowania+i+sprz%C4%99tu+komputerowego&l=%C5%81%C3%B3d%C5%BA+%28%C5%82%C3%B3dzkie%29",
        # "http://panoramafirm.pl/szukaj?k=informatyka&l=%C5%81%C3%B3d%C5%BA+%28%C5%82%C3%B3dzkie%29",
        # "http://panoramafirm.pl/szukaj?k=internet&l=%C5%81%C3%B3d%C5%BA+%28%C5%82%C3%B3dzkie%29",
        # "http://panoramafirm.pl/szukaj?k=odzyskiwanie+i+ochrona+danych+komputerowych&l=%C5%81%C3%B3d%C5%BA+%28%C5%82%C3%B3dzkie%29",
        # "http://panoramafirm.pl/szukaj?k=operatorzy+telekomunikacyjni&l=%C5%81%C3%B3d%C5%BA+%28%C5%82%C3%B3dzkie%29",
        # "http://panoramafirm.pl/szukaj?k=oprogramowanie+komputerowe&l=%C5%81%C3%B3d%C5%BA+%28%C5%82%C3%B3dzkie%29",
        # "http://panoramafirm.pl/szukaj?k=systemy+i+us%C5%82ugi+telekomunikacyjne&l=%C5%81%C3%B3d%C5%BA+%28%C5%82%C3%B3dzkie%29",
        # "http://panoramafirm.pl/szukaj?k=systemy+i+technologie+multimedialne&l=%C5%81%C3%B3d%C5%BA+%28%C5%82%C3%B3dzkie%29",
        # "http://panoramafirm.pl/szukaj?k=sprz%C4%99t+i+centrale+telefoniczne&l=%C5%81%C3%B3d%C5%BA+%28%C5%82%C3%B3dzkie%29",
        # "http://panoramafirm.pl/szukaj?k=sieci+komputerowe+i+integracja+system%C3%B3w&l=%C5%81%C3%B3d%C5%BA+%28%C5%82%C3%B3dzkie%29",
        # "http://panoramafirm.pl/szukaj?k=serwisy+informacyjne&l=%C5%81%C3%B3d%C5%BA+%28%C5%82%C3%B3dzkie%29",
        # "http://panoramafirm.pl/szukaj?k=sprz%C4%99t+radiokomunikacyjny&l=%C5%81%C3%B3d%C5%BA+%28%C5%82%C3%B3dzkie%29",
        # "http://panoramafirm.pl/szukaj?k=stacje+radiowe+i+telewizyjne&l=%C5%81%C3%B3d%C5%BA+%28%C5%82%C3%B3dzkie%29",
        ]

    rules = (
        Rule(LinkExtractor(
            restrict_xpaths=("//a[contains(@class, 'addax-cs_hl_nextpage')]")), callback="parse_item", follow=True),
    )

    def parse_start_url(self, response):
        return self.parse_item(response)

    def parse_item(self, response):
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
                address = sel. \
                    xpath("div[@class='contacts']/*/following-sibling::text()"). \
                    extract()[0].encode('utf-8').strip().split(", ")
                firma['address'] = address[0]
                firma['city'] = address[1]
                firma['area'] = ""
            except:
                try:
                    address = sel. \
                        xpath("div/div[@class='companyAddress popoverShow']/*/text()"). \
                        extract()[0].encode('utf-8').strip().split(", ")
                    firma['address'] = address[0]
                    firma['city'] = address[1]
                    firma['area'] = ''.join(sel. \
                        xpath("div/div[@class='companyAddress popoverShow']/text()"). \
                        extract()).encode('utf-8').strip(),
                except:
                    firma['address'] = ""
            try:
                firma['description'] = ''. \
                    join(sel.xpath("div[@class='text hidePhone crl']//text()"). \
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
