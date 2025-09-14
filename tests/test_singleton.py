from concurrent.futures import ThreadPoolExecutor
from patrones.singleton.implementation import Database, Book


def setup_function() -> None:
    # Aislamos el estado entre tests
    Database._drop_instance_for_tests()


def test_singleton_identity():
    a = Database()
    b = Database()
    assert a is b


def test_thread_safety_single_instance():
    def get_obj_id() -> int:
        return id(Database())

    with ThreadPoolExecutor(max_workers=16) as ex:
        ids = set(ex.map(lambda _: get_obj_id(), range(64)))

    assert len(ids) == 1, f"Se esperaban 1 id único, hubo {len(ids)}"


def test_add_and_list_books():
    db = Database()
    db.add_book("Refactoring", "Martin Fowler")
    db.add_book("Clean Code", "Robert C. Martin")

    books = db.list_books()
    assert books == [
        Book("Refactoring", "Martin Fowler"),
        Book("Clean Code", "Robert C. Martin"),
    ]