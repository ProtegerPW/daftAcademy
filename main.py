from fastapi import FastAPI

app = FastAPI()
app.counter = 0

@app.get("/")
def root():
    return {"message": "Hello world!"}

@app.get('/method')
def getRequest():
    return {"method": "GET"}

@app.put('/method')
def putRequest():
    return {"method": "PUT"}

@app.options('/method')
def optionsRequest():
    return {"method": "OPTIONS"}

@app.delete('/method')
def deleteRequest():
    return {"method": "DELETE"}

@app.post('/method')
def postRequest():
    return {"method": "POST"}
    

@app.get("/hello/{name}")
def hello_name_view(name: str):
    return f"Hello {name}"

@app.get('/counter')
def counter():
    app.counter += 1
    return str(app.counter)
