#  file: main.py
from deta import Deta  # Import Deta
from fastapi import FastAPI

# Initialize with a Project Key unless detabase is within a micro-- then automatic
# deta = Deta("project key")
deta = Deta()
# This how to connect to or create a database.
db = deta.Base("pins")

# You can create as many db's as you want without additional charges.
# books = deta.Base("books")


class PinsIn(BaseModel):
    ts: str
    src: str
    A0: int = None
    A1: int = None
    D2: int = None
    D3: int = None


class Pins(PinsIn):
    id: int


app = FastAPI()


@app.get("/")
def read_root():
    return {"Testing": "NoSQL_Pins"}


@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id}


@app.post("/pins", response_model=Pins)
async def create_pins(pns: PinsIn):
    rspns = db.put({pns.ts, pns.src, pns.D2, pns.D3, pns.A0., pns.A1})
    return rspns
