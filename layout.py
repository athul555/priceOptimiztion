import dash_bootstrap_components as dbc
import dash_html_components as html
import dash_core_components as dcc
import pandas as pd

CONTENT_STYLE = {
    # "margin-left": "18rem",
    # "margin-right": "2rem",
    "padding": "2em",
}

df= pd.read_csv("dash\data.csv")
optimum_df= pd.read_csv("dash\output.csv")

product_options=[{"label": product, "value": product} for product in df.NAME]
zone_options=[{"label": product, "value": product} for product in df.ZONE.unique()]
mrp_options=[]



title_card= dbc.Card(
    dbc.CardBody(
        [
            html.H3(html.Center("PRIZE OPTIMIZATION"), className="card-title"),
        ]
    )
)

product_dropdown = html.Div(
    [
        dbc.Label("Select the product", html_for="product"),
        dcc.Dropdown(
            id="product_dropdown",
            options= product_options,
            value=product_options[0]['value']
        ),
    ],
    className="mb-3",
)

zone_dropdown = html.Div(
    [
        dbc.Label("Select the zone", html_for="zone"),
        dcc.Dropdown(
            id="zone_dropdown",
            options= zone_options,
            value=zone_options[0]['value']
        ),
    ],
    className="mb-3",
)

mrp_dropdown = html.Div(
    [
        dbc.Label("Select the MRP", html_for="mrp"),
        dcc.Dropdown(
            id="mrp_dropdown",
            options= mrp_options,
        ),
    ],
    className="mb-3",
)

body_card= dbc.Card(
    dbc.CardBody(
        [
            html.H6("Please select a product to see the optimum price", className="card-body", id="body"),
        ]
    )
)




layout= dbc.Container([
    dbc.Row(title_card, style= CONTENT_STYLE),
    dbc.Row([
        dbc.Col(product_dropdown),
        dbc.Col(zone_dropdown),
        dbc.Col(mrp_dropdown),
    ], style= CONTENT_STYLE),
    # dbc.Row(product_dropdown,style= CONTENT_STYLE),
    # dbc.Row(zone_dropdown, style= CONTENT_STYLE),
    # dbc.Row(mrp_dropdown, style= CONTENT_STYLE),
    dbc.Row(body_card, style= CONTENT_STYLE),
])