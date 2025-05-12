from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from mrservices.pipelines.subsection import GetSubsection
from mrservices.pipelines.react_plots import GetReactPlots


api_key = ""
sub_text = GetSubsection(api_key)
sub_plots = GetReactPlots(api_key)


class Subsection(BaseModel):
    industry: str
    region: str
    subsection: str
    n_words: int

app = FastAPI()





@app.post("/subsection")
def get_sub_txt_plots(data: Subsection):
    sub_json = sub_text.get_subsection(
        data.industry,
        data.region,
        data.subsection,
        data.n_words
        )

    react_plots = sub_plots.get_react_plots(
        data.industry,
        data.region,
        data.subsection,
        sub_json['content']
        )
    
    return {
        "content": sub_json["content"],
        "plots": react_plots
        }