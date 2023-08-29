from .pages import CarPage
from web_poet import field
import dateparser


############### CarsandBids.com ################

class CarsandBids(CarPage):

    @field
    def source(self):
        return 'carsandbids.com'

    @field
    def year(self):
        return self.xpath("//title/text()").re_first('\d{4}')

    @field
    def description(self):
        return "".join(self.xpath("//div[@class='auction-title ']/following-sibling::div/h2/text()").getall())

    @field
    def price(self):
        return "".join(self.xpath("//div[contains(@class, 'current-bid')]//span[@class='bid-value']//text()").getall())

    @field
    def comment_count(self):
        return self.xpath("//li[@class='num-comments']/span[@class='value']/text()").get()

    @field
    def engine(self):
        return self.xpath(f"//div[@class='quick-facts']//dl//dt[contains(text(), 'Engine')]/following-sibling::dd//text()").get()

    @field
    def drivetrain(self):
        return self.xpath(f"//div[@class='quick-facts']//dl//dt[contains(text(), 'Drivetrain')]/following-sibling::dd//text()").get()

    @field
    def mileage(self):
        return self.xpath(f"//div[@class='quick-facts']//dl//dt[contains(text(), 'Mileage')]/following-sibling::dd//text()").get()

    @field
    def vin(self):
        return self.xpath(f"//div[@class='quick-facts']//dl//dt[contains(text(), 'VIN')]/following-sibling::dd//text()").get()

    @field
    def transmission(self):
        return self.xpath(f"//div[@class='quick-facts']//dl//dt[contains(text(), 'Transmission')]/following-sibling::dd//text()").get()

    @field
    def exterior(self):
        return self.xpath(f"//div[@class='quick-facts']//dl//dt[contains(text(), 'Exterior Color')]/following-sibling::dd//text()").get()

    @field
    def interior(self):
        return self.xpath(f"//div[@class='quick-facts']//dl//dt[contains(text(), 'Interior Color')]/following-sibling::dd//text()").get()

    @field
    def body_style(self):
        return self.xpath(f"//div[@class='quick-facts']//dl//dt[contains(text(), 'Body Style')]/following-sibling::dd//text()").get()

    @field
    def model(self):
        return self.xpath(f"//div[@class='quick-facts']//dl//dt[contains(text(), 'Model')]/following-sibling::dd//text()").get()

    @field
    def make(self):
        return self.xpath(f"//div[@class='quick-facts']//dl//dt[contains(text(), 'Make')]/following-sibling::dd//text()").get()

    @field
    def location(self):
        return self.xpath(f"//div[@class='quick-facts']//dl//dt[contains(text(), 'Location')]/following-sibling::dd//text()").get()

    @field
    def seller(self):
        return self.xpath(f"//div[@class='quick-facts']//dl//dt[contains(text(), 'Seller')]/following-sibling::dd//text()").get()

    @field
    def seller_type(self):
        return self.xpath(f"//div[@class='quick-facts']//dl//dt[contains(text(), 'Seller Type')]/following-sibling::dd//text()").get()

    @field
    def reserve(self):
        no_reserve = self.xpath("//div[@class='row auction-heading']//span[@class='no-reserve']")
        if no_reserve:
            return False
        return True

    @field
    def auction_end_date(self):
        return self.convert_date_string("".join(self.xpath("//span[@class='time-ended']/text()").getall()))

    @field
    def bid_count(self):
        return self.xpath("//li[@class='num-bids']/span[@class='value']/text()").get()

    @field
    def comment_text(self):
        comments = []
        try:
            for comment in self.xpath("//li[@class='comment']"):
                text = " ".join(comment.xpath(".//div[@class='message']//text()").getall())
                comments.append(text)
        except Exception:
            pass
        return comments

    @field
    def title_status(self):
        return self.xpath(f"//div[@class='quick-facts']//dl//dt[contains(text(), 'Title Status')]/following-sibling::dd//text()").get()

    @field
    def bids(self):
        bids = []
        try:
            for bid in self.xpath("//li[@class='bid']"):
                bids.append({
                    "bidder": bid.xpath(".//div[@class='username']//div[@class='text']//a[@class='user']/@title").get(),
                    "amount": "".join(bid.xpath(".//dd/text()").getall()),
                    "timestamp": int(dateparser.parse(
                        bid.xpath(".//div[@class='text']//span[@class='time']/@data-full").get()).timestamp())
                })
        except Exception:
            pass
        return bids
