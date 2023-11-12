from web_poet import field
from .pages import CarPage
import json


############### Autotrader.com ################

class AutoTrader_Page(CarPage):

    def get_json_data(self):
        raw_data = self.xpath("//div[@id='mountNode']/following-sibling::script[1]/text()").get()
        self.json_data = self.get_data(raw_data, load=True)

    @field
    def source(self):
        if not hasattr(self, 'json_data'):
            self.get_json_data()
        return "autotrader.com"

    @field
    def year(self):
        return next(iter(list(self.json_data.get("initialState",{}).get("inventory",[]).values())), {}).get("year")

    @field
    def description(self):
        return next(iter(list(self.json_data.get("initialState").get("inventory").values())), {}).get("additionalInfo", {}).get("vehicleDescription")

    @field
    def price(self):
        return str(next(iter(list(self.json_data.get("initialState").get("inventory").values())), {}).get("pricingDetail", {}).get("salePrice"))

    @field
    def comment_count(self):
        return next(iter(list(self.json_data.get("initialState").get("inventory").values())), {}).get("kbbConsumerReviewCount")

    @field
    def engine(self):
        return next(iter(list(self.json_data.get("initialState").get("inventory").values())), {}).get("specifications", {}).get("engineDescription", {}).get("value")

    @field
    def drivetrain(self):
        return next(iter(list(self.json_data.get("initialState").get("inventory").values())), {}).get("specifications", {}).get("driveType", {}).get("value")

    @field
    def mileage(self):
        return next(iter(list(self.json_data.get("initialState").get("inventory").values())), {}).get("specifications", {}).get("mileage", {}).get("value")

    @field
    def vin(self):
        return next(iter(list(self.json_data.get("initialState").get("inventory").values())),{}).get("vin")

    @field
    def transmission(self):
        return next(iter(list(self.json_data.get("initialState").get("inventory").values())), {}).get("specifications", {}).get("transmission", {}).get("value")

    @field
    def exterior(self):
        return next(iter(list(self.json_data.get("initialState").get("inventory").values())), {}).get("exteriorColorSimple")

    @field
    def interior(self):
        return next(iter(list(self.json_data.get("initialState").get("inventory").values())), {}).get("interiorColorSimple")

    @field
    def body_style(self):
        return ", ".join(next(iter(list(self.json_data.get("initialState").get("inventory").values())), {}).get("bodyStyleCodes", []))

    @field
    def model(self):
        return next(iter(list(self.json_data.get("initialState").get("inventory").values())), {}).get("model")

    @field
    def make(self):
        return next(iter(list(self.json_data.get("initialState").get("inventory").values())), {}).get("make")

    @field
    def location(self):
        return " ".join(next(iter(list(self.json_data.get("initialState").get("owners").values())), {}).get("location", {}).get("address",{}).values())

    @field
    def seller(self):
        return next(iter(list(self.json_data.get("initialState").get("owners").values())), {}).get("name")

    @field
    def seller_type(self):
        return next(iter(list(self.json_data.get("initialState").get("owners").values())), {}).get("dealer", 'dealer')

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

