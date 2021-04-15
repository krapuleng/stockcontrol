from django.test import TestCase

# Create your tests here.


    @property
	def get_transactions_total(self):
		transactionlines = self.StockTransactionlines.all()
		total = sum([StockTransactionlines.LinePrice for item in StockTransactionlines])
		return total 

		I would like to extend my stay in south Africa so that I may further my studies and be close to my spouse who is a south African resident