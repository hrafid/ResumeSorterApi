import os
from fastapi import FastAPI, File, UploadFile
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from script import *  # Ensure you have the necessary functions imported
from model import *   # Ensure you have the model loading logic here

# Load the model and other components
model, tokenizer, device, reverse_label_map = load_model()

app = FastAPI()

# CORS Middleware (if you plan to use the API from a frontend)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve the HTML page
@app.get("/", response_class=HTMLResponse)
async def read_root():
    with open("index.html") as f:
        return HTMLResponse(content=f.read())

# Predict resume category
@app.post("/predict-resume/")
async def predict_resume(file: UploadFile = File(...)):
    try:
        # Read the file's content
        contents = await file.read()

        # Process the resume content (in-memory processing)
        category = process_resumes(contents, model, tokenizer, device, reverse_label_map)

        # Return the prediction
        return {'prediction': str(category), 'category': category}

    except Exception as e:
        return {"error": str(e)}

    finally:
        # Clean up uploaded file (if saved temporarily)
        if os.path.exists(file.filename):
            os.remove(file.filename)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=int(os.getenv("PORT", 8080)))

