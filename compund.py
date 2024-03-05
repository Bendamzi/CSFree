import calendar

class InvestmentCalculator:
    def __init__(self, name, money, interest_rate, duration):
        self.name = name
        self.money = money
        self.interest_rate = interest_rate
        self.duration = duration

    def calculate_interest(self):
        for _ in range(self.duration):
            self.money += self.money * (self.interest_rate / 100)

    def display_calendar(self, highlight_day, year, month):
        cal = calendar.TextCalendar()
        for day in cal.itermonthdays(year, month):
            if day == highlight_day:
                print(f'[{day:2d}]', end=' ')
            else:
                print(f'{day:2d}', end=' ')
            if day % 7 == 0:
                print()
    
    def display_result(self):
        print(f"Hi {self.name}, your accumulated revenue on investment after {self.duration} weeks is {self.money:.2f} Naira only.")
        

def main():
    name = input("Name: ")
    money = float(input("Money invested: "))
    interest_rate = float(input("Interest Rate (%): "))
    duration = int(input("Duration (in weeks): "))
    highlight_day = int(input("Enter checkout day: "))
    month = int(input("Enter the month: "))
    
    calculator = InvestmentCalculator(name, money, interest_rate, duration)
    calculator.calculate_interest()
    calculator.display_result()
    print("Calendar:")
    calculator.display_calendar(highlight_day, 2024, month)

if __name__ == "__main__":
    main()
