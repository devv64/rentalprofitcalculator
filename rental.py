import matplotlib.pyplot as plt

class Property:
    def __init__(self, total_price, annual_income, annual_expenses, down_payment, interest_rate, loan_term):
        self.total_price = total_price
        self.annual_income = annual_income
        self.annual_expenses = annual_expenses
        self.down_payment = down_payment
        self.interest_rate = interest_rate
        self.loan_term = loan_term

    def calculate_profit(self):
        # Convert down payment from percent (if percent)
        down_payment = self.total_price*self.down_payment if self.down_payment < 1 else self.down_payment 

        # Calculate loan amount
        loan_amount = self.total_price - down_payment    

        # Calculate monthly mortgage payment
        monthly_interest_rate = self.interest_rate / 100 / 12
        total_payments = self.loan_term * 12
        mortgage_payment = loan_amount * (monthly_interest_rate / (1 - (1 + monthly_interest_rate) ** (-total_payments)))

        # Calculate the annual profit
        annual_profit = self.annual_income - self.annual_expenses - (mortgage_payment * 12)

        # Calculate the return on investment
        roi = (annual_profit / down_payment) * 100
        return annual_profit, roi

    def pricefinder(self):
        total_price = 100000000
        property = Property(total_price, annual_income, annual_expenses, down_payment, interest_rate, loan_term)
        annual_profit, roi = property.calculate_profit()
        while roi < 10:
            total_price *= .99
            property = Property(total_price, annual_income, annual_expenses, down_payment, interest_rate, loan_term)
            annual_profit, roi = property.calculate_profit()
        return total_price

print("enter total price: ")
total_price = float(input())
print("enter annual income: ")
annual_income = float(input())
print("enter annual expenses: ")
annual_expenses = float(input())
print("enter down payment: ")
down_payment = float(input())
print("enter interest rate: ")
interest_rate = float(input())
print("enter loan term: ")
loan_term = float(input())

# print("pricefinder test:", pricefinder(300000, 60000, 775000, 6.5, 30))

prop = Property(total_price, annual_income, annual_expenses, down_payment, interest_rate, loan_term)

annual_profits, rois = prop.calculate_profit()

print("yearly returns:", annual_profits)
print("yearly roi:", rois)

if rois < 10:
    print("price needed for a good deal:", prop.pricefinder())

# fig, ax = plt.subplots()
# ax.bar(initial_investments, annual_profits, label='Annual Profit')
# ax.bar(initial_investments, rois, label='ROI')
# ax.legend()
# ax.set_xlabel('Initial Investment')
# ax.set_ylabel('Dollar Amount / %')
# plt.show()