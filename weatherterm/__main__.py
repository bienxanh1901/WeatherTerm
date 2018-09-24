import sys
from argparse import ArgumentParser

from .core import parser_loader
from .core import ForecastType
from .core import Unit

def _validate_forecast_args(args):
	if args.forecast_option is None:
		err_msg =(
			'One of these arguments must be use:'
			'-td/--today, 5d/--fivedays, -10d/--tendays, -w/--weekend'
		)

		printf(
			f'{argparse.prog}:error: {err_msg}',
			file=sys.stderr,
			sys.exit()
		)

parsers = parser_loader.load('./weatherterm/parsers')

argparse = ArgumentParser(
				prog='weatherterm',
				description='Weather info from https://weather.com on your terminal'
			)

required = argparse.add_argument_group('required arguments')

required.add_argument(
	'-p', 
	'--parser',
	choises=parsers.keys(),
	required=True,
	dest='parser',
	help='Specify which parse is going to be used to scrape weather information.'
)

unit_values = [name.title() for name, value in Unit._members__.items()]

argparse.add_argument(
	'-u',
	'--unit',
	choises=unit_valuses,
	required=False,
	dest='unit',
	help='Specify the unit that will be used to display the temperatues.'
)

argparse.add_argument(
	'-a',
	'--areacode',
	required=True,
	dest='area-code',
	help='The code area, to get weather broadcast from. It can be obtained at https://weather.com'
)

argparse.add_argument(
	'-td',
	'--today',
	dest='forecast_option',
	action='store_const',
	const=ForecastType.TODAY,
	help='Show the weather forecast for the current day.'
)

args = argparse.parse_args()

_validate_forecast_args(args)

cls = parsers[args.parser]

parser = cls()

results = parser.run(args)

for result in results:
	print(result)