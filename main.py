from fastapi import FastAPI

app = FastAPI()


# path operation decorator with path 👇
@app.get("/")
# path operation function 👇
async def root():
    return {"message": "Hello World"}


# http://127.0.0.1:8000/blog?limit=13 takes the limit parameter value
@app.get("/blog")
async def blog(limit):
    return {"data":  f'{limit} blogs'} # f strings in python


## all definite paths needs to be abobe dynamic routes
@app.get("/blog/unpublished")
async def unpublished():
  return {"data" : "unpublished"}

@app.get("/blog/{id}")
async def blog(id: int):
    return {"message":  id}


@app.get("/blog/{id}/comments")
async def comment(id : int):
    # fetch comments of blogs with id
    return {"message": "comments for blog " + str(id)}



## /docs and /redoc for testing