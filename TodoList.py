from typing import List

# Define a data structure for a task
def task(title: str, description: str = "", completed: bool = False) -> dict:
    """
    This function defines the structure of a task with its attributes.

    Args:
        title: The title of the task.
        description: (Optional) A description of the task.
        completed: Whether the task is completed or not.

    Returns:
        A dictionary representing the task.
    """
    return {
        "title": title,
        "description": description,
        "completed": completed,
    }

# Define a pure function to add a new task to a list
def add_task(tasks: List[dict], new_task: dict) -> List[dict]:
    """
    This function adds a new task to the list of tasks.

    Args:
        tasks: A list of dictionaries representing tasks.
        new_task: A dictionary representing the new task to add.

    Returns:
        A new list of tasks with the new task added.
    """
    return tasks + [new_task]  # Use list concatenation to avoid modifying the original list

# Define a higher-order function to filter tasks based on completion status
def filter_tasks(tasks: List[dict], completed: bool) -> List[dict]:
    """
    This function filters a list of tasks based on their completion status.

    Args:
        tasks: A list of dictionaries representing tasks.
        completed: A boolean value indicating whether to filter completed (True) or pending (False) tasks.

    Returns:
        A new list containing only tasks that match the completion status.
    """
    return [task for task in tasks if task["completed"] == completed]

# Define a function to mark a task as completed
def mark_completed(tasks: List[dict], title: str) -> List[dict]:
    """
    This function marks a task with the given title as completed.

    Args:
        tasks: A list of dictionaries representing tasks.
        title: The title of the task to mark as completed.

    Returns:
        A new list with the specified task marked as completed.
    """
    return [
        {**task, "completed": True} if task["title"] == title else task  # Update the specific task dictionary
        for task in tasks
    ]

# Example usage
tasks = []  # Empty list to store tasks

# Add some tasks
tasks = add_task(tasks, task("Buy groceries", "Milk, bread, eggs"))
tasks = add_task(tasks, task("Finish report", "Due tomorrow"))
tasks = add_task(tasks, task("Clean the house", "", True))

# Print all tasks
print("All tasks:")
for task in tasks:
    print(f"- {task['title']}" + (f" ({task['description']})" if task["description"] else ""))

# Print pending tasks
print("\nPending tasks:")
pending_tasks = filter_tasks(tasks, False)
for task in pending_tasks:
    print(f"- {task['title']}" + (f" ({task['description']})" if task["description"] else ""))

# Mark a task as completed
tasks = mark_completed(tasks, "Buy groceries")

# Print all tasks after marking one as completed
print("\nAll tasks after marking one completed:")
for task in tasks:
    completed_str = "[completed] " if task["completed"] else ""
    print(f"- {completed_str}{task['title']}" + (f" ({task['description']})" if task["description"] else ""))
