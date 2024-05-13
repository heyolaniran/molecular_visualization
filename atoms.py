import json
import urllib.request as req 
import dash_bio as dashbio 
from dash import Dash , html 

app =  Dash(__name__ , title="Update atoms") 

model_data = req.urlopen('https://git.io/mol2d_buckminsterfullerene.json').read().decode('utf-8')

model_data = json.loads(model_data)

for atom in model_data["nodes"] : 
    atom.update(atom='H')

for bond in model_data['links']: 
    bond.update(distance=50, strength=0.5)

app.layout = html.Div([
    dashbio.Molecule2dViewer(
        id='molecule2d-modeldata', 
        modelData=model_data
    )
])





if __name__ == "__main__" : 
     app.run(debug=True)