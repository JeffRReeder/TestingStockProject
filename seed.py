from models import db, User, Stock
from datetime import datetime
from app import app

# Create all tables
db.drop_all()
db.create_all()

# password is '123'
user1 = User(username='test1', password='$2b$12$uixTQhtpGqTgO0XeAo30g.M9h2mSfTTOEwFO3vjfRo2UHQojguT7C')
user2 = User(username='test2', password='$2b$12$RmrRz7X1ojWnLZaRN4n75uIIfVAVvGwBjvrgeG7tPp46kOWZ5tRUi')
#user2 = User(username='test', password='123')

stock1 = Stock(company_name="cisco", ticker_symbol="CSCO", price=45.00, owner=1)
stock2 = Stock(company_name="apple", ticker_symbol="AAPL", price=250.00, owner=1)
stock3 = Stock(company_name="Tesla", ticker_symbol="TSLA", price=700.00, owner=1)
stock4 = Stock(company_name="3M", ticker_symbol="MMM", price=175.00, owner=1)
stock5 = Stock(company_name="amazon", ticker_symbol="AMZN", price=1750.00, owner=2)



db.session.add(user1)
db.session.add(user2)
db.session.commit()



db.session.add_all([stock1, stock2, stock3, stock4, stock5])
db.session.commit()



# user_stock1 = UserStock(user_id=user1.id, stock_id=stock1.id)
# user_stock2 = UserStock(user_id=user1.id, stock_id=stock2.id)
# user_stock3 = UserStock(user_id=user2.id, stock_id=stock3.id)

#db.session.add_all([user_stock1, user_stock2])
#db.session.commit()

# select ticker_symbol from stocks JOIN users_stocks ON stocks.id=users_stocks.stock_id JOIN users ON users.id=users_stocks.
# user_id WHERE users.id=1;
