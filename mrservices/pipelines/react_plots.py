from openai import OpenAI
from mrservices.completions.completions import (
    get_online_natural_completion,
    get_offline_json_completion
)
from mrservices.prompts.plots import (
    PROMPT_CREATE_JSON_PLOTS,
    prompt_user_make_plots,
    prompt_text_plots_subsection
)
from mrservices.formats.charts import Charts
from mrservices.react.chart_formatting import (
    nivo_bar_chart,
    nivo_pie_chart,
    nivo_line_chart
)

class GetReactPlots:

    def __init__(self, api_key, model="gpt-4o-mini"):
        self.client = OpenAI(
            # This is the default and can be omitted
            api_key=api_key,
        )
        self.model = model
        self.plots_json_raw = None
        self.data_raw = None

    def get_react_plots(self, industry, region, subsection, core_data):
        """
        Get the react plots for a specific subsection of the industry and region.
        """
        str_subsection_plots = self._get_text(
            industry=industry,
            region=region,
            subsection=subsection,
            core_data=core_data
        )

        plots_json_raw = self._format_text(str_subsection_plots)
        plots_json = plots_json_raw['choices'][0]['message']['parsed']['charts']

        react_plots = []

        for plot in plots_json:
            if plot['type_chart'] == 'bar_chart':
                react_plot = nivo_bar_chart(plot)
                react_plot['type_chart'] = 'bar_chart'
            elif plot['type_chart'] == 'pie_chart':
                react_plot = nivo_pie_chart(plot)
                react_plot['type_chart'] = 'pie_chart'
            elif plot['type_chart'] == 'line_chart':
                react_plot = nivo_line_chart(plot)
                react_plot['type_chart'] = 'line_chart'
            else:
                raise ValueError(f"Unknown chart type: {plot['type_chart']}")

            react_plots.append(react_plot)

        return react_plots

    def _get_text(self, industry, region, subsection, core_data):

        sys_prompt_plots = prompt_text_plots_subsection(
            industry=industry,
            region=region,
            subsection=subsection
        )
    
        user_prompt_plots = prompt_user_make_plots(subsection=core_data)

        self.data_raw = get_online_natural_completion(
            prompt=sys_prompt_plots,
            user_prompt=user_prompt_plots,
            client=self.client,
            model=self.model
        )

        return self.data_raw
    
    def _format_text(self, text):
        """
        Format the text into a JSON object
        that contains the content and references.
        """
        self.plots_json_raw = get_offline_json_completion(
            prompt=PROMPT_CREATE_JSON_PLOTS,
            user_prompt=text,
            format_json=Charts,
            client=self.client,
            model=self.model
        )

        return self.plots_json_raw.to_dict()