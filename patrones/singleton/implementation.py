from __future__ import annotations

from dataclasses import dataclass #crea automaticamente el __init__
from threading import Lock, RLock #para sincronización de hilos
from typing import List


@dataclass(frozen=True) # objeto (frozen lo hace inmutable)
class Book:
    title: str
    author: str


class Database:
    """
    Singleton perezoso (lazy) y seguro para hilos.
    - Única instancia: Database() siempre devuelve el mismo objeto.
    - Thread-safe: doble chequeo + Lock.
    - Estado compartido: lista de libros protegida con RLock.
    """

    _instance: "Database | None" = None # unica instancia global
    _lock: Lock = Lock()  # protege la creación de la instancia

    def __new__(cls) -> "Database": #creamos la instancia solo cuando alguien la llama
        # Lazy initialization con doble chequeo, evitando que dos hilos creen instancias simultaneamente
        if cls._instance is None:
            with cls._lock:
                if cls._instance is None:
                    cls._instance = super().__new__(cls)
        return cls._instance

    def __init__(self) -> None:
        # Evita re-inicializar si __init__ se llama múltiples veces
        if getattr(self, "_initialized", False):
            return
        self._data_lock: RLock = RLock()
        self._books: List[Book] = []
        self._initialized = True

    # --------- API "de bibliotecario" ----------
    def add_book(self, title: str, author: str) -> Book:
        if not title or not author:
            raise ValueError("title y author no pueden ser vacíos")
        book = Book(title=title.strip(), author=author.strip())
        with self._data_lock:
            self._books.append(book)
        return book

    def list_books(self) -> list[Book]:
        with self._data_lock:
            # Devuelve una copia, para no exponer ni permitir modificar el arreglo interno.
            return list(self._books)

    # --------- Utilidad para ejemplos/tests ----------
    @classmethod
    def _drop_instance_for_tests(cls) -> None:
        """Reinicia la instancia (solo para pruebas/demos)."""
        with cls._lock:
            cls._instance = None

    def __repr__(self) -> str:
        return f"<Database id={id(self)} books={len(self._books)}>"