from concurrent.futures import ThreadPoolExecutor
from .implementation import Database


def main() -> None:
    # Mismas referencias aunque "instanciemos" varias veces
    db1 = Database()
    db2 = Database()
    print("db1 is db2:", db1 is db2)
    print("id(db1), id(db2):", id(db1), id(db2))

    # Operaciones de "bibliotecario"
    db1.add_book("Clean Architecture", "Robert C. Martin")
    db2.add_book("Design Patterns", "GoF")
    db2.add_book("Prueba", "Abril Freytes")

    for b in db1.list_books():
        print(f"- {b.title} — {b.author}")

    # Demostración multi-hilo: todas las tareas ven la MISMA instancia, se corren 32 tareas en paralelo
    def grab_id() -> int:
        return id(Database())

    with ThreadPoolExecutor(max_workers=8) as ex:
        ids = set(ex.map(lambda _: grab_id(), range(32)))

    print("IDs únicos vistos desde 32 tareas:", ids)
    print("¿Una sola instancia?", len(ids) == 1)


if __name__ == "__main__":
    main()
