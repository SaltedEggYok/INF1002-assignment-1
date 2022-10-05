import dash_core_components as dashCoreComp
import dash_html_components as dashHTMLComp
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dashBootComp

from app import server
from app import app
# put filenames here
# from apps import

dropdown = dashBootComp.DropdownMenu(
    children=[
        dashBootComp.DropdownMenuItem("Home")
    ]
)