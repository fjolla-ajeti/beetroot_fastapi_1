from fastapi import FastAPI

app= FastAPI()

@app.get('/')
async def hello_everyone():
    return{'message': 'hello to everyone'}


@app.get('/beetroot/names/{emp_name}')
async def say_hello(emp_name):
    return {'greetings':f'hello{emp_name}'}