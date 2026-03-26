#TO DO List Application

tasks = []
next_id = 1   # Counter to give each task a unique ID




def add_task():
    """Ask the user for a title and category, then add a new task."""
    global next_id  

    title = input("Enter task title: ").strip()
    if not title:
        print("   Title cannot be empty.\n")
        return

    print("  Suggested categories: Work | Personal | Shopping | Health | Other")
    category = input("  Enter category (default: General): ").strip() or "General"

    # Build the task dictionary and append it to the list
    task = {
        "id":        next_id,
        "title":     title,
        "category":  category,
        "completed": False        # Every new task starts as pending
    }
    tasks.append(task)
    print(f"   Task #{next_id} added.\n")
    next_id += 1  


def view_tasks(filter_category=None):
    """
    Display tasks in two groups: Pending and Completed.
    Pass a category string to show only tasks in that category.
    """
  
    visible = tasks
    if filter_category:
        visible = [t for t in tasks if t["category"].lower() == filter_category.lower()]
        if not visible:
            print(f"  No tasks found in category '{filter_category}'.\n")
            return

    # Split into pending and completed using list comprehensions
    pending   = [t for t in visible if not t["completed"]]
    completed = [t for t in visible if t["completed"]]

    print("\n~~~~~~~~~~~~~~~~~ PENDING TASKS ~~~~~~~~~~~~~~~~~~~~~~")
    if pending:
        for t in pending:
            print(f"  [{t['id']}] {t['title']}  ({t['category']})")
    else:
        print("  (none)")

    print("\n~~~~~~~~~~~~~~~ COMPLETED TASKS ~~~~~~~~~~~~~~~~~~")
    if completed:
        for t in completed:
            print(f"  [{t['id']}] ✓ {t['title']}  ({t['category']})")
    else:
        print("  (none)")
    print()


def mark_completed():
    """Find a task by ID and flip its completed flag to True."""
    view_tasks()
    try:
        task_id = int(input("Enter task ID to mark as completed: "))
    except ValueError:
        print("  ❌ Please enter a valid number.\n")
        return

    for task in tasks:
        if task["id"] == task_id:
            if task["completed"]:
                print("  Task is already completed.\n")
            else:
                task["completed"] = True
                print(f"   Task #{task_id} marked as completed.\n")
            return

    print(f"   No task with ID {task_id}.\n")


def remove_task():
    """Delete a task entirely from the list by its ID."""
    view_tasks()
    try:
        task_id = int(input("Enter task ID to remove: "))
    except ValueError:
        print("   Please enter a valid number.\n")
        return

    original_length = len(tasks)

    # Rebuild the list keeping every task EXCEPT the chosen one
    # tasks[:] modifies the list in-place so the global list is updated
    tasks[:] = [t for t in tasks if t["id"] != task_id]

    if len(tasks) < original_length:
        print(f"   Task #{task_id} removed.\n")
    else:
        print(f"   No task with ID {task_id}.\n")


def filter_tasks():
    """Show available categories then display tasks for the chosen one."""
    if not tasks:
        print("  No tasks yet.\n")
        return

#  sorted() for neat display
    categories = sorted({t["category"] for t in tasks})
    print("  Available categories:", ", ".join(categories))

    chosen = input("  Filter by category: ").strip()
    view_tasks(filter_category=chosen)


def print_menu():
    print(" _______________________________")
    print("||       TO DO LIST       ||")
    print(" _______________________________")
    print("||  1. Add task                 ||")
    print("||  2. View all tasks           ||")
    print("||  3. Mark task as completed   ||")
    print("||  4. Remove task              ||")
    print("||  5. Filter by category       ||")
    print("||  6. Quit                     ||")
    print(" _______________________________")


def main():

    print("\n  Welcome to the To Do List Application!\n")

    while True:
        print_menu()
        choice = input("Choose an option (1-6): ").strip()

        if   choice == "1": add_task()
        elif choice == "2": view_tasks()
        elif choice == "3": mark_completed()
        elif choice == "4": remove_task()
        elif choice == "5": filter_tasks()
        elif choice == "6":
            print("\n  Goodbye! have a nice day.\n")
            break
        else:
            print(" Invalid option. Please enter from 1-6.\n")


if __name__ == "__main__":
    main()