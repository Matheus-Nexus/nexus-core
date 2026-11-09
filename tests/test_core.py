from src.nexus.core import NexusCore
from src.nexus.task import Task

def test_run_task():
    core = NexusCore()
    task = Task(task_id="123")
    result = core.run_task(task)
    assert "123" in result
