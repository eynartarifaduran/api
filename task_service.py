from app.models.task import Task

class TaskService:
    @staticmethod
    def create_task(title, description, status, created_at, assigned_to):
        # Implementar lógica para crear una nueva tarea aquí
        pass

    @staticmethod
    def update_task(task_id, status):
        # Implementar lógica para actualizar una tarea existente aquí
        pass

    @staticmethod
    def delete_task(task_id):
        # Implementar lógica para eliminar una tarea existente aquí
        pass

    @staticmethod
    def get_task(task_id):
        # Implementar lógica para obtener información de una tarea específica aquí
        pass

    @staticmethod
    def get_all_tasks():
        # Implementar lógica para obtener todas las tareas aquí
        pass
