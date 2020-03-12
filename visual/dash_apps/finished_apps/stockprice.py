import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import pandas_datareader as web
import pandas as pd
import numpy as np
import os
from datetime import datetime, timedelta
from django_plotly_dash import DjangoDash

code_df = pd.read_csv('data/kcompany_codes.csv', dtype='object')

def company_url(company_name):
    code = code_df.query("name=='{}'".format(company_name))['code'].to_string(index=False).strip()
    url = 'http://finance.naver.com/item/sise_day.nhn?code={}'.format(code)
    return url


def company_data(url, start, end):
    df = pd.DataFrame()

    page = 1
    slist = []
    dbreak = True

    while start not in slist:
        pg_url = '{url}&page={page}'.format(url=url, page=page)
        listpage = pd.read_html(pg_url, header=0)[0]

        slist = pd.Series(listpage['날짜'].values)
        slist = slist.dropna()
        for i in slist:
            if pd.to_datetime(i) <= start:
                dbreak = False
                break

        df = df.append(listpage, ignore_index=True)

        if dbreak == False:
            break

        page += 1

    # df.dropna()를 이용해 결측값 있는 행 제거
    df = df.dropna()

    #컬럼명을 영문으로 전환
    df = df.rename(columns={'날짜':'date', '종가':'close', '전일비':'diff',
                        '시가':'open', '고가':'high', '저가':'low',
                        '거래량':'volume'})

    # 데이터의 타입을 int형으로 바꿔줌
    df[['close', 'diff', 'open', 'high', 'low', 'volume']] \
        = df[['close', 'diff', 'open', 'high', 'low', 'volume']].astype(int)

    # 컬럼명 'date'의 타입을 date로 바꿔줌
    df['date'] = pd.to_datetime(df['date'])

    # 일자(date)를 기준으로 오름차순 정렬
    df = df.sort_values(by='date', ascending=True)

    df.set_index('date', inplace=True)

    df = df[start:end]

    return df


def company_stock(company_name, start, end):
    url = company_url(company_name)
    df = company_data(url, start, end)
    return df


app = DjangoDash('StockPrice')

app.layout = html.Div([
    html.H1('Stock Price Graph'),
    html.H3('기업명과 조회기간을 입력하세요:'),
    html.Span('기업명: '),
    dcc.Input(id='company_name', value='삼성전자'),
    html.Span('시작일자(예:2019-01-01): '),
    dcc.Input(id='start_date', value='', placeholder='Start date in YYYY-MM-DD'),
    html.Span('종료일자(예:2019-12-31): '),
    dcc.Input(id='end_date', value='', placeholder='End date in YYYY-MM-DD'),
    dcc.Graph(id='my_graph',
              figure={'data':[
                  {'x':[1,2], 'y':[3,1]}
              ], 'layout':{'title':'Default Title'}}
    )
])

@app.callback(Output('my_graph','figure'),
              [Input('company_name', 'value'),
               Input('start_date', 'value'),
               Input('end_date', 'value')]
              )
def update_graph(company_name, start_date, end_date):
    syear, smonth, sday = map(int, start_date.split('-'))
    start = datetime(syear, smonth, sday)
    eyear, emonth, eday = map(int, end_date.split('-'))
    end = datetime(eyear, emonth, eday)
    df = company_stock(company_name, start, end)
    fig = {'data':[{'x':df.index, 'y':df['close']}],
          'layout':{'title':company_name}
    }
    return fig
