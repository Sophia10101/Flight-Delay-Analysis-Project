from pydantic import BaseSettings
from typing import Optional

class Settings(BaseSettings):
   
    API_V1_STR: str = "/api/v1"
    PROJECT_NAME: str = "Flight Delay Prediction API"
    
 
    FLIGHTAWARE_API_KEY: Optional[str] = None
    CHECKWX_API_KEY: Optional[str] = None
    AVIATION_STACK_API_KEY: Optional[str] = None
    
    class Config:
        env_file = ".env"
        case_sensitive = True

settings = Settings() 