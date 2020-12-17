import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
from datetime import datetime

from app import app
from apps import app1, app2


# Overall app layout. The visible content is rendered based on the URL
#
app.layout = html.Div(children=[
	dcc.Location(id='url', refresh=False),
	
	html.Div(className='app-body-wrapper', children=[
		html.Div(id='app-body', className='app-body', children=[]),
		
		html.Div(className='app-vertical-separator'),
		
		html.Div(className='app-navigation', children=[
			dcc.Link('Index', href='/'),
			html.Br(),
			dcc.Link('Button clicks', href='/app1'),
			html.Br(),
			dcc.Link('Coronavirus data', href='/app2'),
		])
	])
])



# Layout for the index page
#
def layout():
	return html.Div(children=[
		html.H3('Index'),
		html.Div('Place your index page body content here.'),
		#html.Div('Add some links to navigate between /app1 and /app2'),
	])



# This is used for navigation between index, app1, and app2.
#
@app.callback(
	Output('app-body', 'children'),
	[ Input('url', 'pathname') ])
def display_page(pathname):
	if pathname == '/': #index page
		return layout()
	elif pathname == '/app1':
		return app1.layout()
	elif pathname == '/app2':
		return app2.layout()
	else:
		return html.H2('404 Page not found')



# Starts the server when running index.py
#
if __name__ == '__main__':
	print('\nStarting server at: {}'.format(datetime.today()))
	app.run_server(port=8000, debug=True)
