from django.test import TestCase
from LinkedLiving.views import GetDailyView

class SimpleTest(TestCase):
	#Test if get_daily api function working correctly
	def test_api_get_daily_view_wrong_range(self):
		daily = GetDailyView()
		response = daily.returnData(-1,-1)
		self.assertEqual([],response)

