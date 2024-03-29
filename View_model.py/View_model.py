from todo_app.data.item import item


class ViewModel:
    def __init__(self, items):
        self._items = items
 
    @property
    def items(self):
        return self._items