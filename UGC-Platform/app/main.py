from fastapi import FastAPI, Request, Depends
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from . import models, database

# Tạo bảng dữ liệu
models.Base.metadata.create_all(bind=database.engine)

app = FastAPI(title="Đế chế UGC của Wy")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request, db: Session = Depends(database.get_db)):
    # Lấy thử danh sách danh mục (hiện tại chắc chắn đang rỗng)
    categories = db.query(models.Category).all()
    
    return templates.TemplateResponse(
        request=request, 
        name="index.html", 
        context={
            "message": "Hệ thống Database đã sẵn sàng khai hỏa!",
            "categories": categories
        }
    )
