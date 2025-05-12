from typing import Union

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from mrservices.pipelines.subsection import GetSubsection
from mrservices.pipelines.react_plots import GetReactPlots

api_key  = "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"
sub_text = GetSubsection(api_key)
sub_plots = GetReactPlots(api_key)


class Subsection(BaseModel):
    industry: str
    region: str
    subsection: str
    n_words: int

app = FastAPI()


# Add this block immediately after app creation
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://192.168.1.48:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# class Item(BaseModel):
#     name: str
#     price: float
#     is_offer: Union[bool, None] = None



# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}


# @app.put("/items/{item_id}")
# def update_item(item_id: int, item: Item):
#     return {"item_name": item.name, "item_id": item_id}


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