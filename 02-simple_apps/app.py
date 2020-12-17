import dash
import flask
import json
import os



# Create the app
#
app = dash.Dash(__name__)
app.title = 'Web app exercise' #this gets displayed in the window name
app.config['suppress_callback_exceptions'] = True#setting to False may be helpful when debugging


# Overwrite the default Dash favicon
#
server = app.server
@server.route('/favicon.ico')
def favicon():
	return flask.send_from_directory(
		os.path.join(server.root_path, 'static'), 
		'favicon.ico'
	)
