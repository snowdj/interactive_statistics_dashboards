from dash import Dash
from werkzeug.wsgi import DispatcherMiddleware
import flask
from werkzeug.serving import run_simple
import dash_html_components as html
from dash_apps.museums import museums
from dash_apps.gva import gva

server = flask.Flask(__name__)
dash_app1 = museums.create_museums_app(server)
dash_app2 = gva.create_gva_app(server)
#dash_app1.layout = html.Div([html.H1('Hi there, I am app1 for dashboards')])
#dash_app2.layout = html.Div([html.H1('Hi there, I am app2 for reports')])
@server.route('/')
@server.route('/hello')
def hello():
    return flask.redirect("https://www.gov.uk/government/organisations/department-for-digital-culture-media-sport/about/statistics")

@server.route('/dashboard')
def render_dashboard():
    return flask.redirect('/dash1')


@server.route('/reports')
def render_reports():
    return flask.redirect('/dash2')

app = DispatcherMiddleware(server, {
    '/dash1': dash_app1.server,
    '/dash2': dash_app2.server
})

#run_simple('0.0.0.0', 8080, app, use_reloader=False, use_debugger=False)
