from weatherterm.core import ForecastType

class WeatherComParser:

	def __init__(self):
		self._forecast = {
			ForeCastType.TODAY:self._today_forecast,
			ForeCastType.FIVEDAY:self._five_and_ten_days_forecast,
			ForeCastType.TENDAY:self._five_and_ten_days_forecast,
			ForeCastType.WEEKEND:self._weekend_forecast,
		}

	def _today_forecast(sefl, args):
		raise NotImplementedError()

	def _five_and_ten_days_forecast(sefl, args):
		raise NotImplementedError()

	def _weekend_forecast(sefl, args):
		raise NotImplementedError()

	def run(self, args):
		self._forecast_type = args.forecast_option
		forecast_function = self._forecast[args.forecast_option]
		return forecast_function(args)