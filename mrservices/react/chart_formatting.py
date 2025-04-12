
from mrservices.react.utils import generate_hsl_colors

def nivo_bar_chart(bar_chart):
    chart = {
        "title": bar_chart['plot_title'],
        "description": bar_chart['description'],
        "keys": [bar_chart['y_axis_title']],
        "indexBy": bar_chart['x_axis_title']
    }
    
    assert(len(bar_chart['x_axis_data']) == len(bar_chart['y_axis_data']))
    data = []
    for k in range(0,len(bar_chart['x_axis_data'])):
        info = {
            bar_chart["x_axis_title"]: bar_chart["x_axis_data"][k],
            bar_chart["y_axis_title"]: bar_chart["y_axis_data"][k]
        }
        data.append(info)
        
    chart['data'] = data
    
    return chart

def nivo_pie_chart(pie_chart):
    
    chart = {
        "title": pie_chart['plot_title'],
        "description": pie_chart['description'],
    }
    
    assert(len(pie_chart['values']) == len(pie_chart['labels']))

    data = []
    n = len(pie_chart['values'])
    colors = generate_hsl_colors(n)
            
    for k in range(0,n):
        info = {
            "id": pie_chart["labels"][k],
            "label": pie_chart["labels"][k],
            "value": pie_chart["values"][k],
            "color": colors[k]
        }
        data.append(info)
        
    chart['data'] = data
    
    return chart


def nivo_line_chart(line_chart):
    
    chart = {
        "title": line_chart['plot_title'],
        "description": line_chart['description'],
        "legend": line_chart['x_axis_title']
    }
    
    data = []
    n = len(line_chart['line_series'])
    colors = generate_hsl_colors(n)
            
    for k in range(0,n):
        series_plot = []
        for j in range(0,len(line_chart["x_values"])):
            x_y = {
                "x": line_chart['x_values'][j],
                "y": line_chart["line_series"][k]["y_values"][j]
            }
            series_plot.append(x_y)
        
        info = {
            "id": line_chart["line_series"][k]["label"],
            "color": colors[k],
            "data": series_plot
        }
        data.append(info)
        
    chart['data'] = data
    
    return chart