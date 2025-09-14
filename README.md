# 📚 Final diseño de sistemas - Abril  Freytes

Implementación de **patrones de diseño** en Python, sin Lombock y tests:

- **Singleton** — una sola instancia, lazy & thread-safe
- **Factory Method** — creación polimórfica por jerarquías de creadores
- **Abstract Factory** — familias de objetos compatibles (UI + Envío)
- **Builder** — construcción declarativa de objetos inmutables con validación
- **Prototype** — clonación (deep/shallow) con overrides

## 🧱 Estructura del proyecto
    patrones/
    ├─ singleton/
    │ ├─ init.py
    │ ├─ implementation.py
    │ └─ example.py
    ├─ factory_method/
    │ ├─ init.py
    │ ├─ implementation.py
    │ └─ example.py
    ├─ abstract_factory/
    │ ├─ init.py
    │ ├─ implementation.py
    │ └─ example.py
    ├─ builder/
    │ ├─ init.py
    │ ├─ implementation.py
    │ └─ example.py
    ├─ prototype/
    ├─ init.py
    ├─ implementation.py
    └─ example.py
    
    tests/
    ├─ conftest.py
    ├─ test_singleton.py
    ├─ test_factory_method.py
    ├─ test_abstract_factory.py
    ├─ test_builder.py
    └─ test_prototype.py
    
    presentaciones/
    ├─ Abstract Factory.pdf
    ├─ Builder.pdf
    ├─ Factory.pdf
    ├─ Prototype.pdf
    └─ Singleton.pdf


    requirements.txt
    README.md

