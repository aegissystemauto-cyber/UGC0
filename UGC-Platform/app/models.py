from sqlalchemy import Column, Integer, String, Text, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base

class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True) # Ví dụ: Code, Thơ, Ảnh...
    
    # Liên kết: Một danh mục có nhiều bài đăng
    posts = relationship("Post", back_populates="category")

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    content = Column(Text)
    # Lưu link nếu là bài đăng dạng link, hoặc code, hoặc thơ
    post_type = Column(String) # "code", "poem", "image", "link"
    
    category_id = Column(Integer, ForeignKey("categories.id"))
    
    # Liên kết ngược lại với danh mục
    category = relationship("Category", back_populates="posts")
