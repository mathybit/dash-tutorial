import dash_core_components as dcc
import dash_html_components as html
import dash_table as dt
from dash.dependencies import Input, Output, State
from dash.exceptions import PreventUpdate
import json
import requests
import pandas as pd
#import plotly.graph_objs as go

from app import app #needed to define the @app.callbacks





dt_style_table = {# width is set by CSS
	'height': '300px',
	'maxHeight': '300px'
}
dt_style_header = {
	'color': '#ffffff',
	'backgroundColor': '#565666',
	'fontSize': '1.05em',
	'fontWeight': 'bold',
	'fontFamily': 'Calibri'
}
dt_style_cell = {
	'minWidth': '150px',
	'overflow': 'hidden',
	'textOverflow': 'ellipsis',
	'color': '#222222',
	'fontSize': '1.05em',
	'backgroundColor': '#fdfcfb'
}
dt_style_data_conditional = [#alternating row colours
	{
		'if': {'row_index': 'odd'},
		'backgroundColor': '#f8f6f4'
	}
]



def layout():
	return html.Div(children=[
		html.H2('Coronavirus data'),
		html.Div('App content'),
		html.Br(),
		
		html.H4('Illinois coronavirus data'),
		html.Button(id='app2-button', className='app-button', children='Load API data', n_clicks=0),
		
		html.Div(className='app2-table-wrapper', children=[
			#https://dash.plotly.com/dash-core-components/graph
			dt.DataTable(
				id='app2-table',
				data=[],
				columns=[#Define the table columns
					#The column 'id' should match the key of the data element/row
					#The 'name' will be the display text
					{'id': 'date', 'name': 'Date'},
					{'id': 'positive', 'name': 'Positive tests'},
					{'id': 'total', 'name': 'Total tests'},
					{'id': 'rate', 'name': 'Positivity rate'},
				],
				fixed_rows={'headers': True, 'data': 0},
				style_table=dt_style_table,
				style_header=dt_style_header,
				style_cell=dt_style_cell,
				style_data_conditional=dt_style_data_conditional,
				editable=False,
				#sort_action='native',
			)
		])
	])






# Loads the data from the API, and updates the table
# API documentation: https://covidtracking.com/data/api
#
@app.callback(
	Output('app2-table', 'data'),
	[ Input('app2-button', 'n_clicks') ])
def load_covid_data(n_clicks):
	if n_clicks == 0:
		raise PreventUpdate
	
	# Makes the call to the API
	response = requests.get(
		'https://api.covidtracking.com/v1/states/daily.json',
		proxies=None,
		verify=False,#avoids SSL errors
	)
	
	# Turns the API response data into a list of JSON objects (equivalently Python dictionaries)
	data = json.loads(response.content)

	# We are only interested in date, state, positive, totalTestResults FOR ILLINOIS ONLY
	table_data = [
		{
			'date': row['date'],
			'state': row['state'],
			'positive': row['positive'],
			'total': row['totalTestResults'],
			'rate': '{:.2f}'.format(int(row['positive']) / int(row['totalTestResults']))
		} for row in data if row['state'] == 'IL'
	]
	
	# The DataTable component accepts a list of dictionaries for it's 'data' property,
	# and this is exactly the format we have, so we don't need anything else!
	return table_data
