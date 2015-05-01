from django.test import TestCase
from LinkedLiving.views import GetDailyView

class SimpleTest(TestCase):
	#Test if get_daily api function return an empty list while input range is wrong
	def test_api_get_daily_view_input_wrong_range(self):
		daily = GetDailyView()
		response = daily.returnData(-1,-1)
		self.assertEqual([],response)
	#Test if get_daily api function return the correct json file while input range is correct
	def test_api_get_daily_view_input_correct_range(self):
		daily = GetDailyView()
		response = daily.returnData(1427871600,1427957999)
		self.assertEqual(758,len(response))

