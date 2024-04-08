from todo_app.data.item import item


class ViewModel:
    def __init__(self, items):
        self._items = items
 
    @property
    def items(self):
        return self._items

    @property
    def Todo_items(self):
        return []
    
    @property
    def doing_items(self):
        return []

    @property
    def done_items(self) -> list[item]:
        output =[]

        for item in self._items:
            if item.status == "Done":
                output.append(item)

        return output