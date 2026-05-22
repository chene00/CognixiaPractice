# Simple Bank App

## Setup Instructions

Clone the repo. Navigate to the root of this project. bankapp
```bash
# Create/Activate virutal enviroment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

```bash
# Running the FastAPI server
uvicorn main:app --reload
```

Test