from fastapi import FastAPI

app = FastAPI()
@app.get('/')

def root():
    return  {'data':{'name':'vaish'}}

@app.get('/about')
def about():
    return{'data':{'about my page'}}