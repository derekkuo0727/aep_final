from django.test import TestCase
from LinkedLiving.views import GetDailyView, GetTrendView, GetActivityView, GetHealthInfoView, GearData

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
		self.assertEqual({"time_stamp": 1427896800, "avg_hr": "68"}, response[0])
	#Test if get_trend api function return an empty list while input range is wrong
	def test_api_get_trend_view_input_wrong_range(self):
		trend = GetTrendView()
		response = trend.returnData(-1,-1)
		self.assertEqual([],response)
	#Test if get_trend api function return the correct json file while input range is correct
	def test_api_get_trend_view_input_correct_range(self):
		trend = GetTrendView()
		response = trend.returnData(1427871600,1429167599)
		self.assertEqual(13,len(response))
		self.assertEqual({"max_hr_baseline": 197.0, "avg_hr_rest": 80, "sleep_duration_hours_baseline": 7.5, "sleep_duration_hours": 6.5, "intense_exercise_duration_minutes": 0, "percent_of_time_above_high_baseline": 0.1, "avg_hr_sleep_baseline": 70.0, "exercise_duration_minutes": 14, "intense_exercise_duration_minutes_baseline": 10, "exercise_duration_minutes_baseline": 20, "percent_of_time_above_low_baseline": 9.1, "max_hr": 197, "percent_of_time_above_high": 0.1, "percent_of_time_above_low": 9.1, "avg_hr_rest_baseline": 80.0, "time_stamp": 1427871600, "avg_hr_sleep": 70, "total_steps_baseline": 2500, "total_steps": 2911},response[0])
	#Test if get_activity api function return an empty list while input range is wrong
	def test_api_get_activity_view_input_wrong_range(self):
		activity = GetActivityView()
		response = activity.returnData(-1,-1)
		self.assertEqual([],response)
	#Test if get_activity api function return the correct json file while input range is correct
	def test_api_get_activity_view_input_correct_range(self):
		activity = GetActivityView()
		response = activity.returnData(1427871600,1427957999)
		self.assertEqual(3,len(response))
		self.assertEqual('168',response[0]["max_hr"])
	#Test if get_health_info api function return an empty list while input range is wrong
	def test_api_get_health_info_view_input_wrong_range(self):
		healthinfo = GetHealthInfoView()
		response = healthinfo.returnData(-1,-1)
		self.assertEqual([],response)	
	#Test if get_health_info api function return the correct json file while input range is correct
	def test_api_get_health_info_view_input_correct_range(self):
		healthinfo = GetHealthInfoView()
		response = healthinfo.returnData(1427871600,1427957999)
		self.assertEqual(12,len(response))
		self.assertEqual({'total_steps_target': 2500, 'total_steps': 2911, 'avg_hr_storyline': 'Average heart rate is in regular range.', 'avg_hr_target': 80, 'exercise_time': 14, 'avg_hr': 80, 'avg_hr_weekly_benchmark': 82.0, 'exercise_time_weekly_benchmark': 29.0, 'total_steps_weekly_benchmark': 76096.5, 'exercise_time_storyline': 'Exercise time is less than the average on Wednesday', 'exercise_time_target': 20, 'total_steps_storyline': 'Total steps are less than the average on Wednesday'},response)
	#Test if GearData load correct activity detection table
	def test_gear_data_activity_detection_data_load_correctly(self):
		geardata = GearData()
		self.assertEqual(24, len(geardata.activity_detection_data))
	#Test if GearData load correct daily_aggre_table
	def test_gear_data_daily_aggre_data_load_correctly(self):
		geardata = GearData()
		self.assertEqual(15, len(geardata.daily_aggre_data))

