from datetime import datetime

class TimeValidator:
    def __init__(self, time_format = '%H:%M'):
        self.time_format = time_format


    def is_valid_time(self, time_input):
        try:
            datetime.strptime(time_input, self.time_format)
            return True
        except ValueError:
            return False
