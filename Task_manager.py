#Задача: Создай класс `Task`, который позволяет управлять задачами
#(делами). У задачи должны быть атрибуты: описание задачи, срок выполнения
#и статус (выполнено/не выполнено). Реализуй функцию для добавления задач,
#отметки выполненных задач и вывода списка текущих (не выполненных) задач.

from datetime import datetime

class Task:
    def __init__(self, description, due_date):
        self.description = description  # Описание задачи
        self.due_date = due_date  # Срок выполнения
        self.status = False  # Статус задачи (False - не выполнено, True - выполнено)

    def mark_as_done(self):
        """Отметить задачу как выполненную"""
        self.status = True

    def __str__(self):
        """Строковое представление задачи"""
        status = "Выполнено" if self.status else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.due_date.strftime('%Y-%m-%d')}, Статус: {status}"


class TaskManager:
    def __init__(self):
        self.tasks = []  # Список задач

    def add_task(self, description, due_date):
        """Добавить новую задачу"""
        new_task = Task(description, due_date)
        self.tasks.append(new_task)

    def mark_task_as_done(self, task_index):
        """Отметить задачу как выполненную по индексу"""
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].mark_as_done()

    def get_current_tasks(self):
        """Вывести список не выполненных задач"""
        return [task for task in self.tasks if not task.status]

    def check_overdue_tasks(self):
        """Проверить просроченные задачи и запросить статус"""
        today = datetime.today()
        for task in self.tasks:
            if task.due_date < today and not task.status:
                # Если задача просрочена и ещё не выполнена
                print(f"\nЗадача просрочена: {task.description}, срок был {task.due_date.strftime('%Y-%m-%d')}")
                # Запрашиваем у пользователя, выполнена ли задача
                user_input = input("Задача выполнена? (да/нет): ").strip().lower()
                if user_input == "да":
                    # Вместо того чтобы напрямую вызывать task.mark_as_done(), вызовем метод через индекс
                    task_index = self.tasks.index(task)  # Получаем индекс текущей задачи
                    self.mark_task_as_done(task_index)  # Вызываем mark_task_as_done по индексу
                    print(f"Задача '{task.description}' отмечена как выполненная.\n")
                else:
                    print(f"Задача '{task.description}' остаётся не выполненной.\n")


# Пример использования
task_manager = TaskManager()

# Запрашиваем у пользователя описание задачи и дату выполнения
while True:
    description = input("Введите описание задачи (или 'exit' для выхода): ")
    if description.lower() == 'exit':
        break

    # Запрос даты и проверка её правильности
    while True:
        due_date_input = input("Введите срок выполнения задачи (в формате YYYY-MM-DD): ")
        try:
            due_date = datetime.strptime(due_date_input, "%Y-%m-%d")  # Преобразуем строку в дату
            break  # Если дата введена правильно, выходим из цикла
        except ValueError:
            print("Неверный формат даты. Пожалуйста, введите дату в формате YYYY-MM-DD.")

    # Добавляем задачу
    task_manager.add_task(description, due_date)
    print("Задача добавлена!\n")

# Проверяем просроченные задачи и задаём вопросы пользователю
task_manager.check_overdue_tasks()

# Выводим все задачи
print("\nВсе задачи:")
for task in task_manager.tasks:
    print(task)