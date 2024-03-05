import calendar
name = input("Name: ")
money = input("Money invested: ")
interest_rate = input("Interest Rate (%): ")


class HighlightCalendar(calendar.TextCalendar):
    def __init__(self, highlight_day):
        super().__init__()
        self.highlight_day = highlight_day

    def formatday(self, day, weekday, width):
        if day == self.highlight_day:
            return f'[{day:2d}]'
        else:
            return super().formatday(day, weekday, width)

highlight_day = int(input("Enter checkout day: "))
month = int(input("Enter the month: "))
cal = HighlightCalendar(highlight_day)

money = float(money)

interest_rate = float(interest_rate) *.01
n = int(input("Duration (in 3 weeks): "))
for i in range (n):
    money = money + (money * interest_rate)
    
print(f"Hi {name}, your accumulated revenue on investment after 3 weeks is {money :.2f} Naira only, for the date in the calendar below.")
cal.prmonth(2024, month)