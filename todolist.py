import datetime

class ToDoItem:
    def __init__(self,td,dd):
        self.todo = td
        self.due_date = dd
        self.finished = False

todo1 =ToDoItem("DO HW",datetime.date.today())
print(todo1.todo)
print(todo1.due_date)
print(todo1.finished)
