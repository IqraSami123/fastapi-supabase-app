from fastapi import APIRouter, Request, Form, HTTPException
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from app.models.user_model import UserModel, UserAddressModel
from app.schemas.user_schema import UserCreate, UserUpdate, UserAddressCreate

router = APIRouter()
templates = Jinja2Templates(directory="app/templates")


@router.get("/")
def user_list(request: Request):
    users = UserModel.get_users()
    return templates.TemplateResponse("users_list.html", {"request": request, "users": users})


@router.get("/user/{user_id}")
def get_user(request: Request, user_id: int):
    user = UserModel.get_user(user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return templates.TemplateResponse("user_detail.html", {"request": request, "user": user})


@router.get("/add")
def show_add_user_form(request: Request):
    return templates.TemplateResponse("user_form.html", {"request": request})


@router.post("/add")
def create_user(
    request: Request,
    name: str = Form(...),
    email: str = Form(...),
    phone_no: str = Form(...),
    address_line1: str = Form(...),
    address_line2: str = Form(None),
    city: str = Form(...),
    state: str = Form(...),
):
    user = UserModel.create_user(UserCreate(name=name, email=email, phone_no=phone_no))
    UserAddressModel.create_address(user["id"], UserAddressCreate(
        address_line1=address_line1,
        address_line2=address_line2,
        city=city,
        state=state
    ))
    return RedirectResponse(url="/", status_code=302)


@router.get("/user/{user_id}/edit")
def edit_user_form(request: Request, user_id: int):
    user = UserModel.get_user(user_id)
    return templates.TemplateResponse("user_form.html", {"request": request, "user": user})


@router.post("/user/{user_id}/edit")
def update_user(
    request: Request,
    user_id: int,
    name: str = Form(None),
    email: str = Form(None),
    phone_no: str = Form(None),
):
    updated = UserModel.update_user(user_id, UserUpdate(name=name, email=email, phone_no=phone_no))
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return RedirectResponse(url="/", status_code=302)


@router.get("/user/{user_id}/delete")
def delete_user(user_id: int):
    UserModel.delete_user(user_id)
    return RedirectResponse(url="/", status_code=302)
