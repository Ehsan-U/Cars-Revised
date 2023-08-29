from .pages import CarPage
from web_poet import field
import json


############### Cars.com ################

class CarsDCom_Page(CarPage):

    @field
    def source(self):
        return "cars.com"

    @field
    def year(self):
        return self.xpath("//h1[@class='listing-title']/text()").re_first('\d{4}')

    @field
    def description(self):
        return self.xpath("//div[@class='sellers-notes']/text()").get()

    @field
    def price(self):
        return self.xpath("//div[@class='price-section ']/span[@class='primary-price']/text()").get()

    @field
    def comment_count(self):
        return self.xpath("//div[@class='reviews-collection']/following-sibling::a[@data-linkname='research-consumer-reviews']/text()").re_first('\d+')

    @field
    def engine(self):
        target = 'engine'
        for name, val in zip(self.xpath("//dl[@class='fancy-description-list']/dt/text()").getall(),
                             self.xpath("//dl[@class='fancy-description-list']/dd/text()").getall()):
            if target.lower() in name.lower():
                return val

    @field
    def drivetrain(self):
        target = 'drivetrain'
        for name, val in zip(self.xpath("//dl[@class='fancy-description-list']/dt/text()").getall(),
                             self.xpath("//dl[@class='fancy-description-list']/dd/text()").getall()):
            if target.lower() in name.lower():
                return val

    @field
    def mileage(self):
        target = 'mileage'
        for name, val in zip(self.xpath("//dl[@class='fancy-description-list']/dt/text()").getall(),
                             self.xpath("//dl[@class='fancy-description-list']/dd/text()").getall()):
            if target.lower() in name.lower():
                return val

    @field
    def vin(self):
        target = 'vin'
        for name, val in zip(self.xpath("//dl[@class='fancy-description-list']/dt/text()").getall(),
                             self.xpath("//dl[@class='fancy-description-list']/dd/text()").getall()):
            if target.lower() in name.lower():
                return val

    @field
    def transmission(self):
        target = 'transmission'
        for name, val in zip(self.xpath("//dl[@class='fancy-description-list']/dt/text()").getall(),
                             self.xpath("//dl[@class='fancy-description-list']/dd/text()").getall()):
            if target.lower() in name.lower():
                return val

    @field
    def exterior(self):
        target = 'exterior'
        for name, val in zip(self.xpath("//dl[@class='fancy-description-list']/dt/text()").getall(),
                             self.xpath("//dl[@class='fancy-description-list']/dd/text()").getall()):
            if target.lower() in name.lower():
                return val

    @field
    def interior(self):
        target = 'interior'
        for name, val in zip(self.xpath("//dl[@class='fancy-description-list']/dt/text()").getall(),
                             self.xpath("//dl[@class='fancy-description-list']/dd/text()").getall()):
            if target.lower() in name.lower():
                return val

    @field
    def body_style(self):
        rawdata = self.xpath("//div[@class='vehicle-badging']/@data-override-payload").get()
        if rawdata:
            data = json.loads(rawdata)
            bodystyle = data.get("bodystyle")
            return bodystyle

    @field
    def model(self):
        rawdata = self.xpath("//div[@class='vehicle-badging']/@data-override-payload").get()
        if rawdata:
            data = json.loads(rawdata)
            model = data.get("model")
            return model

    @field
    def location(self):
        return self.xpath("//div[@class='dealer-address']/text()").get()

    @field
    def seller(self):
        return self.xpath("//h3[contains(@class, 'seller-name')]/text()").get()

    @field
    def seller_type(self):
        rawdata = self.xpath("//script[@id='initial-activity-data']/text()").get()
        if rawdata:
            data = json.loads(rawdata)
            seller_type = data.get("seller_type")
            return seller_type

    @field
    def reserve(self):
        return True

