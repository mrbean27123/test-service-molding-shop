from pydantic import BaseModel


def rebuild_schemas(schemas: list[type[BaseModel]]) -> None:
    for schema in schemas:
        try:
            schema.model_rebuild()
        except Exception as e:
            print(f"[Schema rebuild failed] {schema.__name__}: {e}")
