from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from app.api.dependencies import get_db
from app.crud.user import create_user, get_user_by_username, get_users
from app.schemas.user import UserCreate, UserResponse

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)


@router.post(
    "/",
    response_model=UserResponse,
    status_code=status.HTTP_201_CREATED,
)
def create_user_endpoint(
    user_data: UserCreate,
    db: Session = Depends(get_db),  # noqa: B008
):
    existing_user = get_user_by_username(
        db,
        user_data.username,
    )

    if existing_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Username already exists",
        )

    return create_user(
        db,
        user_data,
    )
    
@router.get(
    "/",
    response_model=list[UserResponse],
)
def get_users_endpoint(
    db: Session = Depends(get_db),  # noqa: B008
):
    return get_users(db)