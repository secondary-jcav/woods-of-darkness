from dataclasses import dataclass
from typing import Dict, Optional

@dataclass
class Choice:
    description: str
    next_scene: Optional[str]  # None = end

@dataclass
class Scene:
    id: str
    text: str
    choices: Dict[str, Choice]
