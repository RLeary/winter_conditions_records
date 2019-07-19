# class for temp records, each day is new Record object

class Record:
    def __init__(self, freezing_level, temp_at_900, date_today, area_id):
        self.freezing_level = freezing_level
        self.temp_at_900 = temp_at_900
        self.date_today = date_today
        self.area_id = area_id



    def __eq__(self, other):
        if self.__class__ != other.__class__:
            return False
        return self.__dict__ == other.__dict__

