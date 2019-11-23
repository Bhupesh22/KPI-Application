import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input,Output
import plotly.graph_objs as go
import pandas as pd


app=dash.Dash()
df=pd.read_csv("kpi.csv")

name_option=list()
for name in df['Name']:
    name_option.append({'label':str(name),'value':name})

app.layout=html.Div([
                html.H1(children='KPI Dasboard Task'),
                html.Div([dcc.Dropdown(id='name_picker',options=name_option,placeholder='Select a Name')]),
                html.Div([dcc.Graph(id='graph')])


])
#@app.callback(Output('graph','figure'),[Input('name_picker','value')])
@app.callback(
    dash.dependencies.Output('graph', 'figure'),
    [dash.dependencies.Input( 'name_picker','value')])

def update_figure(name_picker):
    filtered_name=df[df['Name']==name_picker]
    traces=[]

    try:
        dfb = df[df['Name']==name_picker].index.values.astype(int)[0]
    except:
        dfb=0

    labels=["Communication Skills","Problem Solving","Team Work","Learning Agility","Motivated","Reliabilty","Resilience","Emotional Intelligence","Integrity"]
    #values=df.iloc[(df['Name']==selected_name).index[0],1:].tolist()
    #values=df.iloc[(df['Name']==name_picker).index[0],1:].tolist()
    values=df.iloc[(df['Name']==name_picker).index[dfb],:].tolist()
    traces.append(go.Pie(
            labels=labels,
            values=values
            ))
    return{'data':traces,'layout':go.Layout(title='KPI pie')}
    #"layout": {"title":"KPI Donut demo",
                    #"annotations": [{"font": {"size": 20},"showarrow": False,"text": "KPI","x": 0.50,"y": 0.5}]}

    # 'layout': { go.Layout(title='KPI pie') }
    #return { 'data': [ {'labels': labels, 'values': values, 'type': 'pie', 'name': value} ],"layout": {"title":"KPI Donut demo",
                    #"annotations": [{"font": {"size": 20},"showarrow": False,"text": "KPI","x": 0.50,"y": 0.5}]}}


if __name__=='__main__':
    app.run_server(debug=True)
