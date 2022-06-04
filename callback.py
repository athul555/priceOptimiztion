from dash.dependencies import Input, Output
from pyparsing import col
from layout import df, optimum_df
import pandas as pd
import numpy as np

def get_optimum_price(df, name, mrp):
# df= pd.read_csv('ui\\templates\\output.csv')

    value = df.loc[df['NAME']==name]

    SP = [] # new list


    for i in np.arange(mrp/2, mrp, 0.01):
        SP.append(i)
        
    N = []
    R = []
    Dis = []
    Disper = []

    intercept = value['Intercept'][0]
    spcoef = value['SPcoeff'][0]
    uccoef = value['Uccoeff'][0]
    cost = value['Unitcost'][0]
    gst = value['Unitgst'][0]

    for p in SP:
        nsu = (intercept) + (spcoef)*p + (uccoef)*cost
        N.append(nsu)
        
        # profit function
        rev = nsu*(p - cost - gst)
        R.append(rev)
        dis = mrp - p 
        disper = dis/mrp*100
        Dis.append(dis)
        Disper.append(disper)

    # profit= pd.DataFrame([N,SP,R,Dis,Disper], columns=['NSU', 'Price', 'Revenue', 'Discount','Discount'])
        
    # profit = pd.DataFrame({'NSU':N, 'Price': SP, 'Revenue': R, 'Discount': Dis, 'Discount%': Disper})

    profit=pd.DataFrame()
    profit['NSU']=np.array(N)
    profit['Price']=np.array(SP)
    profit['Revenue']=np.array(R)
    profit['Discount']=np.array(Dis)
    profit['Discount%']=np.array(Disper)
    profit.reset_index(inplace=True)
    # profit1 = profit[profit['NSU']>0]

    profit['NSU x Revenue'] = profit['NSU'] * profit['Revenue']
    idx= profit['NSU x Revenue'].idxmax()


    # for checking optimized price
    # optimal_price = profit[profit['NSU x Revenue'] == max(profit['NSU x Revenue'])]['Price']
    # optimal_price= profit.index
    optimal_price= profit['Price'][idx]

    return optimal_price



def callback(app):

    @app.callback(Output(component_id='mrp_dropdown', component_property= 'options'),
              [Input(component_id='product_dropdown', component_property= 'value'),
              Input(component_id='zone_dropdown', component_property= 'value')])
    def update_body(product, zone):
        MRP_list= df.loc[(df.NAME==product) & (df.ZONE==zone)]['MRP']

        return [{"label": mrp, "value": mrp} for mrp in MRP_list]
    
    @app.callback(Output(component_id='body', component_property= 'children'),
            [Input(component_id='product_dropdown', component_property= 'value'),
            Input(component_id='mrp_dropdown', component_property= 'value')])
    def update_body(product, mrp):
        optimum_price=get_optimum_price(optimum_df, product, mrp)
        return f"The optimum price for {product} is {optimum_price}"