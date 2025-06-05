from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import requests

app = FastAPI()

# Mount static folder for favicon
app.mount("/static", StaticFiles(directory="static"), name="static")

# Load environment variables
load_dotenv()
api_key = os.getenv("WEATHER_API_KEY")

# Crop Yield Model
class CropYield(BaseModel):
    crop_type: str
    yield_amount: float
    harvest_date: str

# Input Usage Model
class InputUsage(BaseModel):
    crop_id: int
    input_type: str
    quantity: float
    usage_date: str

# Temporary storage
crops = []
inputs = []

@app.get("/")
def read_root():
    return {"message": "Welcome to Kalvin Fathers Farm System"}

@app.post("/crops/")
def add_crop(crop: CropYield):
    crops.append(crop)
    return {"message": "Crop yield added successfully", "data": crop}

@app.get("/crops/")
def get_crops():
    return {"crops": crops}

@app.post("/inputs/")
def add_input(input: InputUsage):
    inputs.append(input)
    return {"message": "Input usage added successfully", "data": input}

@app.get("/inputs/")
def get_inputs():
    return {"inputs": inputs}

@app.get("/weather/")
def get_weather():
    city = "Wa,gh"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    data = response.json()
    if response.status_code == 200:
        rainfall = data.get("rain", {}).get("1h", 0)
        return {
            "temperature": data["main"]["temp"],
            "rainfall": rainfall,
            "advice": "Irrigate lightly" if rainfall < 2 else "No irrigation needed"
        }
    return {"error": "Failed to fetch weather data"}