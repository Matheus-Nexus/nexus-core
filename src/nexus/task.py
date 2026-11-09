from dataclasses import dataclass, field
from typing import Dict, Any

@dataclass
class Task:
    task_id: str
    payload: Dict[str, Any] = field(default_factory=dict)
