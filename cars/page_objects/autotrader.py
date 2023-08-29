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
        try:
            return list(data.get("initialState").get("inventory").values())[0].get("year")
        except Exception:
            return ''

    @field
    def description(self):
        data = self.json_data()
        try:
            return list(data.get("initialState").get("inventory").values())[0].get("additionalInfo").get("vehicleDescription")
        except Exception:
            return ''

    @field
    def price(self):
        data = self.json_data()
        try:
            return list(data.get("initialState").get("inventory").values())[0].get("pricingDetail").get("salePrice")
        except Exception:
            return ''

    @field
    def comment_count(self):
        data = self.json_data()
        try:
            return list(data.get("initialState").get("inventory").values())[0].get("kbbConsumerReviewCount")
        except Exception:
            return ''

    @field
    def engine(self):
        data = self.json_data()
        try:
            return list(data.get("initialState").get("inventory").values())[0].get("specifications").get("engineDescription").get("value")
        except Exception:
            return ''

    @field
    def drivetrain(self):
        data = self.json_data()
        try:
            return list(data.get("initialState").get("inventory").values())[0].get("specifications").get("driveType").get("value")
        except Exception:
            return ''

    @field
    def mileage(self):
        data = self.json_data()
        try:
            return list(data.get("initialState").get("inventory").values())[0].get("specifications").get("mileage").get("value")
        except Exception:
            return ''

    @field
    def vin(self):
        data = self.json_data()
        try:
            return list(data.get("initialState").get("inventory").values())[0].get("vin")
        except Exception:
            return ''

    @field
    def transmission(self):
        data = self.json_data()
        try:
            return list(data.get("initialState").get("inventory").values())[0].get("specifications").get("transmission").get("value")
        except Exception:
            return ''

    @field
    def exterior(self):
        data = self.json_data()
        try:
            return list(data.get("initialState").get("inventory").values())[0].get("exteriorColorSimple")
        except Exception:
            return ''

    @field
    def interior(self):
        data = self.json_data()
        try:
            return list(data.get("initialState").get("inventory").values())[0].get("interiorColorSimple")
        except Exception:
            return ''

    @field
    def body_style(self):
        data = self.json_data()
        try:
            return ", ".join(list(data.get("initialState").get("inventory").values())[0].get("bodyStyleCodes"))
        except Exception:
            return ''

    @field
    def model(self):
        data = self.json_data()
        try:
            return list(data.get("initialState").get("inventory").values())[0].get("model")
        except Exception:
            return ''

    @field
    def make(self):
        data = self.json_data()
        try:
            return list(data.get("initialState").get("inventory").values())[0].get("make")
        except Exception:
            return ''

    @field
    def location(self):
        data = self.json_data()
        try:
            return " ".join(list(data.get("initialState").get("owners").values())[0].get("location").get("address").values())
        except Exception:
            return ''

    @field
    def seller(self):
        data = self.json_data()
        try:
            return list(data.get("initialState").get("owners").values())[0].get("name")
        except Exception:
            return ''

    @field
    def seller_type(self):
        data = self.json_data()
        try:
            return list(data.get("initialState").get("owners").values())[0].get("dealer", 'dealer')
        except Exception:
            return ''

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

