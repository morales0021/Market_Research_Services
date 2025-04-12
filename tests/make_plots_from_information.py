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
import json
import pdb

api_key  = "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"

client = OpenAI(
    # This is the default and can be omitted
    api_key=api_key,
)

model = "gpt-4o-mini"
data = 'The market research services industry in the United States has experienced significant growth, with revenues reaching approximately $36.6 billion in 2025, reflecting a compound annual growth rate (CAGR) of 3.9% over the past five years. ([ibisworld.com](https://www.ibisworld.com/united-states/industry/market-research/1442/?utm_source=openai)) This expansion is primarily driven by several key factors. First, the increasing reliance on data-driven decision-making across various sectors has heightened the demand for comprehensive market insights. Companies are investing more in research and development (R&D) to develop new products and services that align with evolving consumer preferences, thereby boosting the need for market research services. ([ibisworld.com](https://www.ibisworld.com/united-states/industry/market-research/1442/?utm_source=openai)) Second, technological advancements, particularly in artificial intelligence (AI) and machine learning, have revolutionized data collection and analysis processes. These innovations enable market research firms to provide faster, more accurate insights, enhancing their value proposition to clients. ([ai-smarties.com](https://ai-smarties.com/en/market/market-research-agency-companies-in-united-states-2024?utm_source=openai)) Third, the shift towards digital platforms has facilitated the growth of online and mobile quantitative research, allowing for more efficient and cost-effective data gathering methods. ([research.aimultiple.com](https://research.aimultiple.com/market-research-stats/?utm_source=openai))\n\nHowever, the industry faces several challenges that could impact its growth trajectory. The emergence of self-service platforms and do-it-yourself (DIY) tools has made market research more accessible to businesses, potentially reducing the demand for traditional market research services. This trend pressures established firms to adapt by offering more specialized and value-added services to maintain their competitive edge. ([ibisworld.com](https://www.ibisworld.com/united-states/industry/market-research/1442/?utm_source=openai)) Additionally, the rapid pace of technological change requires market research companies to continually invest in new tools and methodologies to stay relevant, which can be resource-intensive. Moreover, the increasing reliance on quantitative data, facilitated by widespread internet use, may overshadow qualitative insights, potentially leading to a more superficial understanding of consumer behavior. ([ibisworld.com](https://www.ibisworld.com/united-states/industry/market-research/1442/?utm_source=openai)) Furthermore, economic uncertainties and fluctuations in corporate profits can influence R&D spending, thereby affecting the demand for market research services. During periods of economic downturn, companies may reduce their research budgets, impacting the overall industry revenue. ([ibisworld.com](https://www.ibisworld.com/united-states/industry/market-research/1442/?utm_source=openai))\n\n\n## Recent Developments in the U.S. Market Research Industry:\n- [US market research industry up 14.3% | News | Research Live](https://www.research-live.com/article/news/us-market-research-industry-up-143/id/5116623?utm_source=openai) '
industry = "market research services"
region = "United States"
subsection = "key growth drivers and challenges"

sys_prompt_plots = prompt_text_plots_subsection(
    industry=industry,
    region=region,
    subsection=subsection
)
user_prompt_plots = prompt_user_make_plots(subsection=subsection)

data = get_online_natural_completion(
    prompt=sys_prompt_plots,
    user_prompt=user_prompt_plots,
    client=client,
    model=model
)

print(data.output_text)

with open("text_plots_2.json", "w") as f:
    info = {"text": data.output_text}
    f.write(json.dumps(info, indent=4))

plots_json = get_offline_json_completion(
    prompt=PROMPT_CREATE_JSON_PLOTS,
    user_prompt=data.output_text,
    format_json=Charts,
    client=client,
    model=model
)

print(plots_json)

with open("plots.json", "w") as f:
    info = plots_json.to_dict()
    f.write(json.dumps(info, indent=4))