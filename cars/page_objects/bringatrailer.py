import json
from web_poet import field
from .pages import CarPage
from w3lib.html import remove_tags


############### Bringatrailer.com ################

class BringaTrailer_Page(CarPage):

    @field
    def source(self):
        return 'bringatrailer.com'

    @field
    def year(self):
        return self.xpath("//h1[@class='post-title listing-post-title']/text()").re_first('\d{4}')

    @field
    def description(self):
        return "\n".join(self.xpath("//div[contains(@class, 'post')]/div/p/text()").getall())

    @field
    def price(self):
        return self.xpath("//span[@class='info-value noborder-tiny']/strong/text()").get()

    @field
    def comment_count(self):
        return self.xpath("//span[@class='comments_header_html']/span[@class='info-value']/text()").get()

    @field
    def engine(self):
        return self.xpath(f"//div[@class='item']/ul/li[3]/text()").get()

    @field
    def mileage(self):
        return self.xpath(f"//div[@class='item']/ul/li[2]/text()").get()

    @field
    def vin(self):
        return self.xpath(f"//div[@class='item']/ul/li[1]/a/text()").get()

    @field
    def transmission(self):
        return self.xpath(f"//div[@class='item']/ul/li[4]/text()").get()

    @field
    def model(self):
        return self.xpath(f"//strong[contains(text(), 'Model')]/following-sibling::text()").get()

    @field
    def make(self):
        return self.xpath(f"//strong[contains(text(), 'Make')]/following-sibling::text()").get()

    @field
    def location(self):
        return self.xpath("//strong[contains(text(), 'Location')]/following-sibling::a/text()").get()

    @field
    def seller(self):
        return self.xpath("//strong[contains(text(), 'Seller')]/following-sibling::a/text()").get()

    @field
    def seller_type(self):
        return self.xpath("//strong[contains(text(), 'Party')]/following-sibling::text()").get()

    @field
    def reserve(self):
        no_reserve = self.xpath("//div[@class='item-tag item-tag-noreserve']")
        if no_reserve:
            return False
        return True

    @field
    def auction_end_date(self):
        return self.convert_date_string(self.xpath("//span[@data-ends]/text()").get())

    @field
    def bid_count(self):
        return self.xpath("//td[@class='listing-stats-value number-bids-value']/text()").get()


    @field
    def comment_text(self):
        comments = []
        try:
            rawdata = self.xpath("//script[@id='bat-theme-viewmodels-js-extra']/text()").get()
            if rawdata:
                data = json.loads(rawdata.split("VMS =")[-1].strip().replace('\n', '').rstrip(';'))
                for comment in data.get("comments", []):
                    try:
                        text = remove_tags(comment.get("markup"))
                    except Exception as e:
                        text = comment.get("markup")
                    comments.append(text)
        except Exception:
            pass
        return comments

    @field
    def title_status(self):
        return self.xpath("//h1[@class='post-title listing-post-title']/text()").get()

    @field
    def bids(self):
        bids = []
        try:
            rawdata = self.xpath("//script[@id='bat-theme-viewmodels-js-extra']/text()").get()
            if rawdata:
                data = json.loads(rawdata.split("VMS =")[-1].strip().replace('\n', '').rstrip(';'))
                for bid in data.get("comments", []):
                    bid_amount = bid.get("bidAmount", 0)
                    if bid_amount:
                        bids.append({
                            "bidder": bid.get("authorName"),
                            "amount": f"{bid_amount}$",
                            "timestamp": bid.get("timestamp")
                        })
        except Exception:
            pass
        return bids

