import calendar

class HighlightCalendar(calendar.TextCalendar):
    def __init__(self, highlight_day):
        super().__init__()
        self.highlight_day = highlight_day

    def formatday(self, day, weekday, width):
        if day == self.highlight_day:
            return f'[{day:2d}]'
        else:
            return super().formatday(day, weekday, width)

# Example usage
highlight_day = int(input("Enter a day: "))
month = int(input("Enter the month: "))
cal = HighlightCalendar(highlight_day)
cal.prmonth(2024, month)