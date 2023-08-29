from .pages import CarPage
from web_poet import field



############### Cargurus.com ################

class Cargurus(CarPage):

    @staticmethod
    def get_value(response, key):
        try:
            response = response.json()
            if isinstance(key, tuple):
                if len(key) == 2:
                    value = response.get("listing").get(key[0], {}).get(key[1])
                elif len(key) == 3:
                    value = response.get("listing").get(key[0], {}).get(key[1], {}).get(key[2])
                    if isinstance(value, list):
                        value = " ".join(value)
            else:
                value = response.get("listing").get(key)
            return value
        except Exception:
            pass


    @field
    def source(self):
        return 'cargurus.com'

    @field
    def year(self):
        return self.get_value(self.response, 'year')

    @field
    def description(self):
        return self.get_value(self.response, 'description')

    @field
    def price(self):
        return self.get_value(self.response, 'priceString')

    @field
    def comment_count(self):
        return self.get_value(self.response, 'reviewCount')

    @field
    def engine(self):
        return self.get_value(self.response, 'localizedEngineDisplayName')

    @field
    def drivetrain(self):
        return self.get_value(self.response, 'localizedDriveTrain')

    @field
    def mileage(self):
        return self.get_value(self.response, 'mileageString')

    @field
    def vin(self):
        return self.get_value(self.response, 'vin')

    @field
    def transmission(self):
        return self.get_value(self.response, "localizedTransmission")

    @field
    def exterior(self):
        return self.get_value(self.response, "localizedExteriorColor")

    @field
    def interior(self):
        return self.get_value(self.response, "localizedInteriorColor")

    @field
    def body_style(self):
        return self.get_value(self.response, ("autoEntityInfo", "bodyStyle"))

    @field
    def model(self):
        return self.get_value(self.response, "modelName")

    @field
    def make(self):
        return self.get_value(self.response, "makeName")

    @field
    def location(self):
        return self.get_value(self.response, ("seller", "address", "addressLines"))

    @field
    def seller(self):
        return self.get_value(self.response, ("seller", "name"))

    @field
    def seller_type(self):
        return self.get_value(self.response, ("seller", "sellerType"))

    @field
    def reserve(self):
        return True

