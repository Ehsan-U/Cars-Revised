from web_poet import field
from .pages import CarPage
import json


############### Autotrader.com ################

class AutoTrader_Page(CarPage):

    def json_data(self):
        raw_data = self.xpath("//div[@id='mountNode']/following-sibling::script[1]/text()").get()
        data = self.get_data(raw_data, load=True)
        return data

    @field
    def source(self):
        return "autotrader.com"

    @field
    def year(self):
        data = self.json_data()
        return next(iter(list(data.get("initialState").get("inventory").values())), {}).get("year")

    @field
    def description(self):
        data = self.json_data()
        return next(iter(list(data.get("initialState").get("inventory").values())), {}).get("additionalInfo").get("vehicleDescription")

    @field
    def price(self):
        data = self.json_data()
        return next(iter(list(data.get("initialState").get("inventory").values())), {}).get("pricingDetail").get("salePrice")

    @field
    def comment_count(self):
        data = self.json_data()
        return next(iter(list(data.get("initialState").get("inventory").values())), {}).get("kbbConsumerReviewCount")

    @field
    def engine(self):
        data = self.json_data()
        return next(iter(list(data.get("initialState").get("inventory").values())), {}).get("specifications").get("engineDescription").get("value")

    @field
    def drivetrain(self):
        data = self.json_data()
        return next(iter(list(data.get("initialState").get("inventory").values())), {}).get("specifications").get("driveType").get("value")

    @field
    def mileage(self):
        data = self.json_data()
        return next(iter(list(data.get("initialState").get("inventory").values())), {}).get("specifications").get("mileage").get("value")

    @field
    def vin(self):
        data = self.json_data()
        return next(iter(list(data.get("initialState").get("inventory").values())),{}).get("vin")

    @field
    def transmission(self):
        data = self.json_data()
        return next(iter(list(data.get("initialState").get("inventory").values())), {}).get("specifications").get("transmission").get("value")

    @field
    def exterior(self):
        data = self.json_data()
        return next(iter(list(data.get("initialState").get("inventory").values())), {}).get("exteriorColorSimple")

    @field
    def interior(self):
        data = self.json_data()
        return next(iter(list(data.get("initialState").get("inventory").values())), {}).get("interiorColorSimple")

    @field
    def body_style(self):
        data = self.json_data()
        return ", ".join(next(iter(list(data.get("initialState").get("inventory").values())), {}).get("bodyStyleCodes", []))

    @field
    def model(self):
        data = self.json_data()
        return next(iter(list(data.get("initialState").get("inventory").values())), {}).get("model")

    @field
    def make(self):
        data = self.json_data()
        return next(iter(list(data.get("initialState").get("inventory").values())), {}).get("make")

    @field
    def location(self):
        data = self.json_data()
        return " ".join(next(iter(list(data.get("initialState").get("owners").values())), {}).get("location", {}).get("address",{}).values())

    @field
    def seller(self):
        data = self.json_data()
        return next(iter(list(data.get("initialState").get("owners").values())), {}).get("name")

    @field
    def seller_type(self):
        data = self.json_data()
        return next(iter(list(data.get("initialState").get("owners").values())), {}).get("dealer", 'dealer')

    @field
    def reserve(self):
        return True

    @staticmethod
    def get_data(response, load=None):
        try:
            if not load:
                return json.loads(response.xpath("//pre/text()").get())
            else:
                return json.loads(response.split("DATA__=")[-1])
        except json.decoder.JSONDecodeError:
            return None

