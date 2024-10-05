from datetime import datetime
class DateValidator:
    def __init__(self, date_format = '%d-%m-%Y'):
        self.date_format = date_format

    def is_valid_date(self, date_input):
        try:
            datetime.strptime(date_input, self.date_format)
            return True
        except ValueError:
            return False



