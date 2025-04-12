PROMPT_CREATE_JSON_PLOTS = """Analyse the information provided and determine the plots that can be created. The plots
can be of different types, such as: BarChart, LineChart or PieChart. 
Provide:
- A list of the different plots to be created
- Each plot should contain a title, description
- The type of chart to be created is precised in the description
- For a pie chart, you should precise the values and labels
- For a bar chart, you should precise the x data and y data, also the title for the x axis and y axis
- For a line chart, you should precise the x axis title, the x values and the list of line series
- Each line series should contain a label and the y values"""

PROMPT_CREATE_JSON_PLOTS_2 = """You are an assistant that analyzes business or analytical text and extracts structured data about visual plots that can be generated from the content. Your goal is to detect every relevant chart (LineChart, BarChart, PieChart), extract its key characteristics, and format the information in a structured way to populate predefined Pydantic models.

For each chart you find, provide the following:

General Requirements:
The chart type: one of "line_chart", "bar_chart", or "pie_chart"
A clear plot_title and description explaining what the chart represents

For a LineChart (type_chart = "line_chart"):
x_axis_title: title for the x-axis
x_values: list of values (e.g., years or time)
line_series: list of LineSeries, where each item includes:
line_label: name of the line
y_values: list of values corresponding to the x_values

For a BarChart (type_chart = "bar_chart"):
x_axis_data: categories or labels on the x-axis
x_axis_title: title for the x-axis
y_axis_data: list of corresponding numeric values
y_axis_title: title for the y-axis (if available)

For a PieChart (type_chart = "pie_chart"):
labels: list of segment names
values: list of corresponding numeric values

Return the result as a list of plots, each formatted to match its respective structure.
The list of plots should contain maximum 3 plots.
"""


def prompt_user_make_plots(subsection: str) -> str:
    """
    Provides a prompt for the user to propose plots.
    Args:
        subsection (str): The subsection to be used for the prompt.
    """
    request = f"Propose some plots for the following text: {subsection}"
    return request

def prompt_text_plots_subsection(
    industry: str, region: str, subsection: str
    ) -> str:
    """
    Provides a prompt for the given industry and region.
    Args:
        industry (str): The industry to be used for the prompt.
        region (str): The region to be used for the prompt.
        subsection (str): The subsection to be used for the prompt.
    """
    prompt_plot = f"""I have a text that discusses {subsection} for the {industry} in the {region}.
    Based on this text, suggest 2-3 complementary data visualizations that would enhance understanding of the content.
    For each proposed plot, please:
    The type of chart : one of "line_chart", "bar_chart", or "pie_chart"
    Describe the plot (e.g., chart showing market growth, chart comparing key drivers, ...).
    Explain in a natural way how should we interpret the plot and what insights we can get from it.
    Provide real estimated data (in table format) that I can use to generate the plot.
    """

    return prompt_plot
