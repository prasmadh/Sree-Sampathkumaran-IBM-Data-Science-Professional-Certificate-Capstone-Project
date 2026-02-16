# Import required libraries
import pandas as pd
import dash
from dash import html
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px

# Read the SpaceX data into pandas dataframe
spacex_df = pd.read_csv("spacex_launch_dash.csv")

launch_sites = sorted(spacex_df["Launch Site"].unique())

site_options = [{"label": "All Sites", "value": "ALL"}] + [
    {"label": site, "value": site} for site in launch_sites
]

max_payload = spacex_df['Payload Mass (kg)'].max()
min_payload = spacex_df['Payload Mass (kg)'].min()

# Create a dash application
app = dash.Dash(__name__)

# Create an app layout
app.layout = html.Div(children=[html.H1('SpaceX Launch Records Dashboard',
                                        style={'textAlign': 'center', 'color': '#503D36',
                                               'font-size': 40}),
                                # TASK 1: Add a dropdown list to enable Launch Site selection
                                # The default select value is for ALL sites
                                dcc.Dropdown(id='site-dropdown',
                                    options=site_options,
                                    value="ALL",
                                    placeholder="Select a Launch Site",
                                    searchable=True),
                            html.Br(),

                                # TASK 2: Add a pie chart to show the total successful launches count for all sites
                                # If a specific launch site was selected, show the Success vs. Failed counts for the site
                                html.Div(dcc.Graph(id='success-pie-chart')),
                                html.Br(),

                                html.P("Payload range (Kg):"),
                                # TASK 3: Add a slider to select payload range
                                dcc.RangeSlider(id='payload-slider',
                                    min=0, max=max_payload, step=1000,
                                    marks={min_payload: str(min_payload), max_payload: str(max_payload)},
                                    value=[min_payload, max_payload]),
                                html.Br(),

                                # TASK 4: Add a scatter chart to show the correlation between payload and launch success
                                html.Div(dcc.Graph(id='success-payload-scatter-chart')),
                                ])

# TASK 2:
# Add a callback function for `site-dropdown` as input, `success-pie-chart` as output
@app.callback(
    Output("success-pie-chart", "figure"),
    Input("site-dropdown", "value")
)

def get_pie_chart(selected_site):
    if selected_site == "ALL":
        # Group by Launch Site and sum class (assuming 1=success, 0=failure)
        site_success = (
            spacex_df.groupby("Launch Site")["class"]
            .sum()
            .reset_index())

        fig = px.pie(
            site_success,
            names="Launch Site",
            values="class",
            title="Total Successful Launches by Site",)
    
    else:
        # Filter to the selected site only
        filtered_df = spacex_df[spacex_df["Launch Site"] == selected_site]

        # Count how many successes (1) and failures (0) appear
        outcome_counts = (
            filtered_df["class"]
            .value_counts()
            .reset_index())

        # Map the numeric outcomes to readable labels
        outcome_counts["Outcome Label"] = outcome_counts["class"].map(
            {1: "Success", 0: "Failure"})

        fig = px.pie(
            outcome_counts,
            names="Outcome Label",
            values="Count",
            title=f"Success vs Failure for {selected_site}",)
        
        return fig


# TASK 4:
# Add a callback function for `site-dropdown` and `payload-slider` as inputs, `success-payload-scatter-chart` as output
@app.callback(
    Output("success-payload-scatter-chart", "figure"),
    [Input("site-dropdown", "value"),
     Input("payload-slider", "value"),
    ],
)
def update_scatter_plot(selected_site, payload_range):
    min_payload_selected, max_payload_selected = payload_range

    # Filter by payload range first
    payload_filtered = spacex_df[
        (spacex_df["Payload Mass (kg)"] >= min_payload_selected) &
        (spacex_df["Payload Mass (kg)"] <= max_payload_selected)
    ]

    if selected_site == "ALL":
        fig = px.scatter(
            payload_filtered,
            x="Payload Mass (kg)",
            y="class",
            color="Booster Version Category",
            title="Payload vs Mission Outcome for All Sites",
            hover_data=["Launch Site"],
        )

    else:
        site_filtered = payload_filtered[payload_filtered["Launch Site"] == selected_site]

        fig = px.scatter(
            site_filtered,
            x="Payload Mass (kg)",
            y="class",
            color="Booster Version Category",
            title=f"Payload vs Mission Outcome for {selected_site}",
            hover_data=["Launch Site"],
        )

    return fig



# Run the app
if __name__ == '__main__':
    app.run()
