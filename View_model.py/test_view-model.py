
from todo_app.data.item import item
from todo_app.data.view_model import viewmodel


def test_done_items_property_only_shows_done_items_and_nothing_else():
    # ARRANGE
    items = [
        item(1,"started Todo", "To Do"),
        item(2, "In progress Todo" , "Doing"),
        item(3, "Finished Todo", "Done")
    ]
    view_model = viewmodel(items)

    # ACT
    returned_items = view_model.done_items

    # ASSERT
    assert len (returned_items) == 1
    returned_single_item = returned_items[0]
    assert returned_singe_item.status == done