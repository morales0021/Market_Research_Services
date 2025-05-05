from mrservices.pipelines.subsection import GetSubsection
from mrservices.pipelines.react_plots import GetReactPlots
import json


api_key  = "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"
sub = GetSubsection(api_key)
sub_plots = GetReactPlots(api_key)

industry = 'hydrogen market'
region = "france"
subsection = "Market size (current and projected growth in the next 5 years)"
sub_json = sub.get_subsection(industry, region, subsection, 400)

# print(subsection_json['content'])

react_plots = sub_plots.get_react_plots(
    industry,
    region,
    subsection,
    sub_json['content']
    )

# print(sub_plots.data_raw.output_text)
# print(react_plots)

data = {
    "content": sub_json["content"],
    "plots": react_plots
    }


with open("subsection_ms.json", "w") as f:
    f.write(json.dumps(data, indent=4))