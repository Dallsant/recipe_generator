from typing import List, Optional
from pydantic import BaseModel
from enum import Enum
from odmantic import EmbeddedModel, Model, Field
from datetime import datetime


class SupportedLanguages(str, Enum):
    spanish = "Spanish"
    english = "English"
    french = "French"


class RecipeGenerationPrompValue(str, Enum):
    example_params = "[[EXAMPLE_PARAMETERS]]"
    params = "[[PARAMETERS]]"


class RecipeGenerationParams(BaseModel):
    # Only use ingredients that appear on the ingredients list
    strict_mode: Optional[bool] = False

    # Language the openai output is going to be written in
    output_language: Optional[str] = SupportedLanguages.english

    # List of ingredients
    ingredients: List[str]

    # Used to tell the model to be more explicit
    detailed_directions: bool = False

    # Amount of dishes to generate
    amount_of_dishes: int = 3


class Recipe(Model):
    name: str
    user_id: Optional[str] = None
    description: Optional[str] = None
    ingredients: List[str] = []
    directions: List[str] = []
    created_at: datetime = Field(default_factory=datetime.utcnow)
    updated_at: datetime = Field(default_factory=datetime.utcnow)
    deleted: bool = False

    class Config:
        collection = "recipes"
        parse_doc_with_default_factories = True
