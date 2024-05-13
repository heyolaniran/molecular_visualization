import json
import urllib.request as req 
from dash import Dash, html, Input, Output, callback
import dash_bio as dashbio 

app = Dash(__name__,title="Molecular visualization") ; 

model_data = req.urlopen('https://git.io/mol2d_buckminsterfullerene.json').read().decode('utf-8')


model_data = json.loads(model_data)



app.layout = html.Div([
    dashbio.Molecule2dViewer(
        id='molecule-2d', 
        modelData=model_data
    ), 

    html.Hr(), 

    html.Div(id='default-output')
])

@callback(
    Output('default-output', 'children'), 
    Input('molecule-2d', 'selectedAtomIds')
)

def update_selected_atoms(ids) : 
    if ids is None or len(ids) == 0 : 
        return "Aucun atome selectionné"
    return "Atoms selectionnées : {}".format(','.join([str(i) for i in ids ]))


if __name__ == '__main__':
    app.run(debug=True); 
