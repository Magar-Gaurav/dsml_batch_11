from fastapi import FastAPI # type: ignore
from Calculator import Calculator

app = FastAPI()

@app.post("/items/{num1}/{num2}")
def read_item(num1: int, num2: int, q: str | None = None):
    op = None if q is None else q.strip()
    calc_obj = Calculator(num1, num2, op)
    result = calc_obj.perform_calculation()
    return {"num1": num1, "num2": num2, "q": q, "result": result}
