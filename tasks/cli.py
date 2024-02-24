from .export import save_to_file
from .storage import add_task, get_all_tasks, mark_task_completed, remove_task


def handle_action():
    user_input = input(
        "What action do you want to take?\n"
        "1 - add task\n"
        "2 - remove task\n"
        "3 - mark as done\n"
        "4 - show all tasks\n"
    )

    match user_input:
        case "1":
            title = input("Enter title: ")
            add_task(title)
        case "2":
            print(get_all_tasks())
            index = int(input("Choose task index to remove: "))
            remove_task(index)
        case "3":
            print(get_all_tasks())
            index = int(input("Choose task index to mark as done: "))
            mark_task_completed(index, True)
        case "4":
            print(get_all_tasks())
        case _:
            print("Try again")


def handle_interrupt():
    user_input1 = input('\nDo you want to exit (y/n)?\n')
    if user_input1 == "y":
        user_input2 = input('\nExport tasks to file (y/n)?\n')
        if user_input2 == "y":
            save_to_file(get_all_tasks(), "export")
            print('Tasks exported to file out/export.xlsx')
    return True
