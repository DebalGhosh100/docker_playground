from sqlalchemy import except_
from db.engine import engine, Base, get_session

from db.models.employee import Employee
from db.models.department import Department


from fastapi import (
    APIRouter,
    Depends,
    Header,
    HTTPException,
    Query,
    Response,
    status as HTTPStatus,
    Request
)

from sqlalchemy.orm import Session, session

local_router = APIRouter(tags=["Build Models"])


@local_router.get(
    "/build_models",
    status_code=HTTPStatus.HTTP_201_CREATED
)
def create_tables(
    db_session: Session = Depends(get_session)
):
    try:
        Base.metadata.create_all(
            bind=engine
        )
    except Exception as error:
        print(error)
