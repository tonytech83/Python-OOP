from typing import List
from project.task import Task


class Section:
    def __init__(self, name: str):
        self.name = name
        self.tasks: List = []

    def add_task(self, new_task: Task) -> str:
        if not any(new_task.name == task.name for task in self.tasks):
            self.tasks.append(new_task)

            return f'Task Name: {new_task.name} - Due Date: {new_task.due_date} is added to the section'

        return f'Task is already in the section {self.name}'

    def complete_task(self, task_name: str):
        for task in self.tasks:
            if task.name == task_name:
                task.completed = True

                return f'Completed task {task_name}'

        return f'Could not find task with the name {task_name}'

    def clean_section(self):
        removed_tasks = 0

        for task in self.tasks:
            if task.completed:
                self.tasks.remove(task)
                removed_tasks += 1

        return f'Cleared {removed_tasks} tasks.'

    def view_section(self):
        result = f'Section {self.name}:\n'
        result += '\n'.join(task.details() for task in self.tasks)

        return result
