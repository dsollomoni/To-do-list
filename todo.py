from abc import ABC, abstractmethod

class ITaskManager(ABC):
    @abstractmethod
    def addTask(self, title: str, description: str):
        pass
    
    @abstractmethod
    def markCompleted(self, task_id: int):
        pass
    
    @abstractmethod
    def listTasks(self, status: str = "all"):
        pass

class Task:
    task_counter = 1
    
    def __init__(self, title: str, description: str):
        self.taskID = Task.task_counter
        Task.task_counter += 1
        self.title = title
        self.description = description
        self.status = "Pending"
    
    def markCompleted(self):
        self.status = "Completed"
    
    def __str__(self):
        return f"[{self.taskID}] {self.title} - {self.description} [Status: {self.status}]"

class TaskManager(ITaskManager):
    def __init__(self):
        self.tasks = []
    
    def addTask(self, title: str, description: str):
        self.tasks.append(Task(title, description))
    
    def markCompleted(self, taskID: int):
        for task in self.tasks:
            if task.taskID == taskID:
                task.markCompleted()
                return
        print("Task ID not found. Please enter a valid task ID.")
    
    def listTasks(self, status: str = "all"):
        if status == "Completed":
            return [task for task in self.tasks if task.status == "Completed"]
        elif status == "Pending":
            return [task for task in self.tasks if task.status == "Pending"]
        return self.tasks

class TaskPrinter:
    @staticmethod
    def displayTasks(tasks):
        if not tasks:
            print("No tasks found.")
        for task in tasks:
            print(task)

# User interaction
def main():
    manager = TaskManager()
    while True:
        print("\nTo-Do List Manager")
        print("1. Add Task")
        print("2. Mark Task as Completed")
        print("3. View Tasks")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            manager.addTask(title, description)
            print("Task added successfully!")
        
        elif choice == "2":
            print("\nSelect a task to mark as completed:")
            TaskPrinter.displayTasks(manager.listTasks("Pending"))
            try:
                taskID = int(input("Enter the task ID: "))
                manager.markCompleted(taskID)
                print("Task marked as completed!")
            except ValueError:
                print("Invalid input. Please enter a valid task ID.")
        
        elif choice == "3":
            print("\nView tasks by status:")
            print("1. All Tasks")
            print("2. Completed Tasks")
            print("3. Pending Tasks")
            status_choice = input("Enter your choice: ")
            
            status = "all"
            if status_choice == "2":
                status = "Completed"
            elif status_choice == "3":
                status = "Pending"
            
            print("\nTasks:")
            TaskPrinter.displayTasks(manager.listTasks(status))
        
        elif choice == "4":
            print("Exiting... Have a great day!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()