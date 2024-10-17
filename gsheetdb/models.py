from pydantic import BaseModel, ValidationError, create_model
from typing import Any, Dict

class GenericModel(BaseModel):
    """A generic model that can accommodate any data structure."""
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'GenericModel':
        return cls(**data)

def create_dynamic_model(fields: Dict[str, Any]) -> BaseModel:
    """Create a dynamic Pydantic model based on provided field definitions."""
    return create_model('DynamicModel', **fields)
