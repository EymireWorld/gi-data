def parse(obj) -> dict:
    result = {}

    for column in obj.__table__.columns:
        result[column.name] = getattr(obj, column.name)

    return result
