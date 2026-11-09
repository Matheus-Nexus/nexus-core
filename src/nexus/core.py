from .bank import NexusBank
from .task import Task

class NexusCore:
    def __init__(self):
        self.bank = NexusBank()

    def run_task(self, task: Task):
        return f"Task {task.task_id} executed"
