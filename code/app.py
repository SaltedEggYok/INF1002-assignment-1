import dash
import dash_bootstrap_components as dashBootComp

#bootstrap theme
ext_stylesheets = [dashBootComp.themes.LUX]

app = dash.Dash(__name__,  external_stylesheets= ext_stylesheets)

server = app.server
app.config.suppress_callback_exceptions = True