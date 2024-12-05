import io
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, StreamingResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
import matplotlib.pyplot as plt
import random

import numpy as np

app = FastAPI()

templates = Jinja2Templates(directory="templates")

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/test.html", response_class=HTMLResponse)
async def test(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "message": "Welcome to FastAPI!"})


# Endpoint to generate a plot
@app.get("/plot")
async def get_plot():
    # Simulate smoke sensor data
    # x = np.linspace(0,2*np.pi)
    # y = np.sin(x)

    x = []
    y = []
    with open("data.txt", "r") as file:
        lines = file.readlines()
        for line in lines:
            l = line.split(",")
            x.append(float(l[0]))
            y.append(float(l[1]))

    # Create a plot
    plt.figure(figsize=(10, 6))
    plt.plot(x, y, marker="o", label="Smoke Level")
    plt.title("Smoke Sensor Readings")
    plt.xlabel("Time (s)")
    plt.ylabel("Smoke Level")
    plt.legend()
    plt.grid()

    # Save the plot to a BytesIO object
    buf = io.BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)
    plt.close()

    return StreamingResponse(buf, media_type="image/png")


# Endpoint to generate a plot
@app.get("/new_point/{index}/{value}")
async def new_point(index,value):
    # Simulate smoke sensor data
    # x = np.linspace(0,2*np.pi)
    # y = np.sin(x)

    with open("data.txt", "a") as file:
        file.write(f"\n{index},{value}")

    return "ok"