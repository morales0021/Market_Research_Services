from openai import OpenAI
from mrservices.completions.completions import (
    get_online_natural_completion,
    get_offline_json_completion
    )
from mrservices.prompts.plots import PROMPT_REFERENCES
from mrservices.prompts.plots import prompt_industry_region_subsection
from mrservices.formats.text_content import TextContentRefs

industry = "hydrogen industry"
region = "Mexico"
subsection = "key growth drivers and challenges"

prompt_key_growth_drivers = prompt_industry_region_subsection(
    industry=industry,
    region=region,
    subsection=subsection,
    n_words=400
)
#api_key from jose
api_key  = "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"

client = OpenAI(
    # This is the default and can be omitted
    api_key=api_key,
)

model = "gpt-4o-mini"
data = get_online_natural_completion(
    prompt=prompt_key_growth_drivers,
    user_prompt="",
    client=client,
    model=model
)

print(data.output_text)

info = get_offline_json_completion(
    prompt=PROMPT_REFERENCES,
    user_prompt=data.output_text,
    format_json=TextContentRefs,
    client=client,
    model=model
)

print(info)