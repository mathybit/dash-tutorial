import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from datetime import datetime

from app import app



def layout():
	return html.Div(children=[
		html.H2('Button clicks app'),
		html.Div('Clicking the button updates the number of times it was clicked'),
		html.Br(),
		
		html.Div(children=[
			html.Button(id='app1-button', className='app-button', children='Click me!', n_clicks=0),
			html.Br(),
			html.Div([
				html.Span('The button was clicked: '),
				html.Span(id='app1-output', children=None),
				html.Span(' times.'),
			]),
			html.Div([
				html.Span('The last click occurred at: '),
				html.Span(id='app1-output2', children=None),
			])
		])
	])



# Modifies the 'children' property of the element with ID 'app1-output'
# The 'children' property is whatever is stored within a HTML tag: <div>children go here</div>
# Children can be a list of elements or a single element
#
@app.callback(
	[
		Output('app1-output', 'children'),
		Output('app1-output2', 'children'),
	],
	[ Input('app1-button', 'n_clicks') ])
def update_click_count(n_clicks):
	if n_clicks == 0:
		timestamp = 'never'
	else:
		timestamp = datetime.today().strftime('%Y-%m-%d %H:%M:%S')
	return n_clicks, timestamp
