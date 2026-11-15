from typing import Annotated

from fastapi import Depends, Query


def get_pagination(
    skip: Annotated[int, Query(ge=0)] = 0,
    limit: Annotated[int, Query(ge=1, le=10)] = 5,
) -> dict:
    return {"skip": skip, "limit": limit}


Pagination = Annotated[dict, Depends(get_pagination)]