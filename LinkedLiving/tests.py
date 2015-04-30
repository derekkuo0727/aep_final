from django.test import TestCase
from LinkedLiving.views import GetActivityView

class SimpleTest(TestCase):
	#Test if get_trend api function
	def test_api_get_daily_view(self):
		jsonResponse = GetActivityView.get("http://127.0.0.1:8000/api/get_trend/?user_id=123&start_datetime=1427871600")
		self.assertEqual("{\"table\": []}",jsonResponse)

