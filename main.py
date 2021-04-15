from fastapi import FastAPI

app = FastAPI()
app.counter = 0

@app.get("/")
def root():
    return {"message": "Hello world!"}

@app.get('/method')
def getRequest():
    return {"method": "GET"}
    

@app.get("/hello/{name}")
def hello_name_view(name: str):
    return f"Hello {name}"

@app.get('/counter')
def counter():
    app.counter += 1
    return str(app.counter)
