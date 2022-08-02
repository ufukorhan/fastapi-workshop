
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware


from .routers import auth, post, user, vote

# instead of this i am using alembic
# models.Base.metadata.create_all(bind=engine) 

app = FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins, # A list of origins that should be permitted to make cross-origin requests.
    # E.g. ['https://example.org', 'https://www.example.org']. We can use ['*'] to allow any origin.
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)
app.include_router(vote.router)

@app.get("/")
def root():
    return {"message": "Main Page"}


