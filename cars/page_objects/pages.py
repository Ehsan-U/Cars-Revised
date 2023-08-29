import datetime
from web_poet.pages import WebPage
from web_poet import field
import dateparser


############### Base ################

class CarPage(WebPage):

    @field
    def source(self):
        return ''

    @field
    def year(self):
        return ''

    @field
    def description(self):
        return ''

    @field
    def price(self):
        return ''

    @field
    def comment_count(self):
        return ''

    @field
    def engine(self):
        return ''

    @field
    def drivetrain(self):
        return ''

    @field
    def mileage(self):
        return ''

    @field
    def vin(self):
        return ''

    @field
    def transmission(self):
        return ''

    @field
    def exterior(self):
        return ''

    @field
    def interior(self):
        return ''

    @field
    def body_style(self):
        return ''

    @field
    def model(self):
        return ''

    @field
    def make(self):
        return ''

    @field
    def location(self):
        return ''

    @field
    def seller(self):
        return ''

    @field
    def seller_type(self):
        return ''

    @field
    def reserve(self):
        return ''

    @field
    def scraped_date(self):
        return datetime.datetime.now().date().strftime("%m/%d/%Y")

    # not common fields
    @field
    def auction_end_date(self):
        return 'N/A'

    @field
    def bid_count(self):
        return 'N/A'

    @field
    def comment_text(self):
        return 'N/A'

    @field
    def title_status(self):
        return "N/A"

    @field
    def bids(self):
        return 'N/A'

    @staticmethod
    def convert_date_string(date_str):
        try:
            formatted_date_str = dateparser.parse(date_str).strftime(f'%m/%d/%Y')
            return formatted_date_str
        except Exception:
            today = datetime.datetime.today().strftime(f'%m/%d/%Y')
            return today


