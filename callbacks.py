import dash
from dash.dependencies import Input, Output
from layout import app
from config import get_database_connection
import plotly.express as px


@app.callback(
    Output('database-data-graph', 'figure'),
    [Input('update-button', 'n_clicks')]
)
def update_database_data(n_clicks):
    if n_clicks is None:
        return dash.no_update

    conn = get_database_connection()
    cursor = conn.cursor()

    # Query the database
    cursor.execute("SELECT name, year, views FROM Views")
    rows = cursor.fetchall()

    # Close the cursor and database connection
    cursor.close()
    conn.close()

    # Process the data and create a graph
    data = {
        "name": [row[0] for row in rows],
        "year": [row[1] for row in rows],
        "views": [row[2] for row in rows],
    }

    fig = px.bar(data, x="name", y="views", title="Data from SQL Server")
    return fig
