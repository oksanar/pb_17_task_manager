from typing import List, Tuple

_DB = []


def add_task(title: str) -> None:
    _DB.append({"title": title, "completed": False})


def remove_task(index: int) -> None:
    _DB.pop(index - 1)


def mark_task_completed(index: int, completed: bool) -> None:
    _DB[index - 1]["completed"] = completed


def get_all_tasks() -> List[Tuple[int, str, bool]]:
    return [(i + 1, task["title"], task["completed"]) for i, task in enumerate(_DB)]
