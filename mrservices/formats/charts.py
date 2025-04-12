from pydantic import BaseModel
from typing import Literal

from typing import List, Literal, Union

class LineSeries(BaseModel):
    label: str                       # Label for this line (e.g., "Healthcare Revenue")
    y_values: List[Union[int, float]]  # Y-axis values for this line

class LineChart(BaseModel):
    type_chart: Literal["line_chart"]
    plot_title: str                  # Title of the chart
    description: str                 # Short explanation of the chart
    x_axis_title: str               # Label for x-axis (e.g., "Year")
    x_values: List[Union[int, float]] # Shared x-axis values (e.g., years)
    line_series: List[LineSeries]   # One or more lines plotted on the chart


class BarChart(BaseModel):
    type_chart: Literal["bar_chart"]
    plot_title: str
    description: str
    x_axis_data: list[str|int|float]
    x_axis_title: str
    y_axis_data: list[int|float]
    y_axis_title: str

class PieChart(BaseModel):
    type_chart: Literal["pie_chart"]
    plot_title: str
    description: str
    values: list[int|float]
    labels: list[str]


class Charts(BaseModel):
    charts: list[PieChart|BarChart|LineChart]

class SingleChart(BaseModel):
    chart: PieChart|BarChart|LineChart