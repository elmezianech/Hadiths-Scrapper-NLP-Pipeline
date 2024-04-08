import scrapy
import pymongo

class MySpider(scrapy.Spider):
    name = "myspider"
    start_urls = [
        "https://mawdoo3.com/أحاديث_نبوية_قصيرة",
        "https://mawdoo3.com/أحاديث_نبوية_شريفة_قصيرة",
        "https://mawdoo3.com/أحاديث_شريفة",
        "https://mawdoo3.com/أحاديث_شريفة_عن_الأم",
        "https://mawdoo3.com/أحاديث_نبوية_صحيحة",
        "https://mawdoo3.com/أحاديث_متعلقة_بآداب_الطعام_والشراب",
        "https://mawdoo3.com/أحاديث_عن_الوالدين",
        "https://mawdoo3.com/أحاديث_نبوية_شريفة_عن_التعامل_مع_الناس",
        "https://mawdoo3.com/أحاديث_عن_العدل",
        "https://mawdoo3.com/احاديث_أبي_هريرة",
        "https://mawdoo3.com/أحاديث_عن_الوضوء"
    ]

    def __init__(self, *args, **kwargs):
        super(MySpider, self).__init__(*args, **kwargs)
        self.collected_items = []

    def parse(self, response):
        # Parse HTML using XPath to extract data from <ul>, <li>, and <b> elements together
        ul_elements = response.xpath('//ul')
        for ul in ul_elements:
            li_b_pairs = ul.xpath('.//li/b')
            for pair in li_b_pairs:
                li_text = pair.xpath('./preceding-sibling::text()').get(default='').strip()
                b_text = pair.xpath('.//text()').get(default='').strip()
                self.collected_items.append({'text': b_text, '': li_text})
                hadith = f"{li_text}{b_text}"
                yield {'text': hadith}  # Yield with a single key 'text'
                #yield {'text1': b_text, 'text2': li_text}

    def closed(self, reason):
        # Connect to MongoDB
        client = pymongo.MongoClient('mongodb://localhost:27017/')
        db = client['hadith_database']
        collection = db['hadiths1']

        # Store collected data in MongoDB
        for item in self.collected_items:
            collection.insert_one(item)
