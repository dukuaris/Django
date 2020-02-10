from django_plotly_dash import DjangoDash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import pandas as pd
import base64

df = pd.read_csv('data/wheels.csv')

app = DjangoDash('MultipleOutputs')


#이미지 파일을 plotly html 파일에 삽입가능한 포맷으로 전환
def encode_image(image_file):
    encoded = base64.b64encode(open(image_file, 'rb').read())
    return 'data:image/png;base64,{}'.format(encoded.decode())

app.layout = html.Div([
            dcc.RadioItems(id='wheels',
                          options=[{'label':i,'value':i} for i in df['wheels'].unique()],
                          value=1
                          ),
            html.Div(id='wheels-output'),
            html.Hr(),
            dcc.RadioItems(id='colors',
                          options=[{'label':i,'value':i} for i in df['color'].unique()],
                          value='blue'
                          ),
            html.Div(id='colors-output'),
            html.Img(id='display-image', src='children', height=300)
], style={'fontFamily':'helvetica', 'fontSize':18})

@app.callback(Output('wheels-output','children'),
              [Input('wheels','value')])
def callback_a(wheels_value):
    return "You chose {}".format(wheels_value)


@app.callback(Output('colors-output','children'),
              [Input('colors','value')])
def callback_b(colors_value):
    return "You chose {}".format(colors_value)


@app.callback(Output('display-image', 'src'),
             [Input('wheels', 'value'),
              Input('colors', 'value')])
def callback_image(wheel, color):
    path = 'data/images/'
    return encode_image(path+df[(df['wheels']==wheel) & \
    (df['color']==color)]['image'].values[0])
