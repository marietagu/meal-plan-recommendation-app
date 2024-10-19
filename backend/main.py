from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel,conlist
from typing import List, Optional
import pandas as pd
import os
from model import recommend,output_recommended_recipes
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Get the directory of the current file
current_dir = os.path.dirname(os.path.abspath(__file__))
dataset_path = os.path.join(current_dir, 'Data', 'dataset.csv')

# Load the dataset
try:
    dataset = pd.read_csv(dataset_path)
    print(f"Dataset loaded successfully from {dataset_path}")
except Exception as e:
    print(f"Error loading dataset: {str(e)}")
    dataset = None

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)

@app.on_event("startup")
async def startup_event():
    port = os.environ.get("PORT", 8000)
    logger.info(f"Starting server on port {port}")
    logger.info(f"Current directory: {current_dir}")
    logger.info(f"Dataset path: {dataset_path}")
    if dataset is not None:
        logger.info("Dataset loaded successfully")
    else:
        logger.error("Failed to load dataset")

class params(BaseModel):
    n_neighbors:int=5
    return_distance:bool=False

class PredictionIn(BaseModel):
    nutrition_input:conlist(float, min_items=9, max_items=9)
    ingredients: List[str] = []
    params:Optional[params]


class Recipe(BaseModel):
    Name: str
    CookTime: str
    PrepTime: str
    TotalTime: str
    RecipeIngredientParts: List[str]
    Calories: float
    FatContent: float
    SaturatedFatContent: float
    CholesterolContent: float
    SodiumContent: float
    CarbohydrateContent: float
    FiberContent: float
    SugarContent: float
    ProteinContent: float
    RecipeInstructions: List[str]

class PredictionOut(BaseModel):
    output: Optional[List[Recipe]] = None


@app.get("/")
def home():
    return {"health_check": "OK"}


@app.get("/health")
def health_check():
    if dataset is not None:
        return {"status": "OK", "dataset": "loaded"}
    else:
        return {"status": "Error", "dataset": "not loaded"}


@app.post("/predict/", response_model=PredictionOut)
def update_item(prediction_input: PredictionIn):
    if dataset is None:
        return {"output": None, "error": "Dataset not loaded"}
