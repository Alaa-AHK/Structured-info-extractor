from typing import Optional
from pydantic import BaseModel, Field

class PersonInfo(BaseModel):
    # We use Field descriptions to help the LLM understand what to look for
    name: Optional[str] = Field(description="The full name of the person", default=None)
    email: Optional[str] = Field(description="The email address found in the text", default=None)
    Age: Optional[int] = Field(description="The age of the person as an integer", default=None)
    Faculty: Optional[str] = Field(description="The university faculty or department", default=None)