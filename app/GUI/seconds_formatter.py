from datetime import datetime, timedelta, time


class SecondsFormatter:
    def __init__(self, seconds):
        self.seconds = seconds

    def __str__(self):
        return self.format_seconds()

    def format_seconds(self):
        seconds_to_add = timedelta(seconds=self.seconds)
        time_object = datetime.combine(datetime.today(), time())
        resulting_time = time_object + seconds_to_add
        return resulting_time.strftime('%M:%S')

    def __add__(self, value):
        return SecondsFormatter(self.seconds + value)
