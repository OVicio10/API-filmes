from fastapi import FastAPI


app = FastAPI()

#tora raiz
@app.get("/")
def raiz():
    return {"Ola" : "mundo"}
