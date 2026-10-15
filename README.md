# BitChord – Offline AI Orchestration

BitChord is a Python-based local AI orchestration framework powered by the LFM2-VL 1.6B language model. It routes user requests to specialized agents and executes conditional workflows using a shared state.

## Features

- Local LFM2-VL 1.6B model inference
- CPU-only execution using `llama-cpp-python`
- No external AI API dependency for inference
- Dynamic keyword-based task routing
- Specialized Coder, Researcher, and Summarizer agents
- Conditional execution graphs
- Shared state and execution timestamps
- Automated tests using `pytest`

## Architecture

```text
User Request
     |
     v
Task Router
     |
     +------> Coder Agent --------+
     |                            |
     +------> Researcher Agent ---+--> Summarizer Agent
     |                            |
     +------> Summarizer Agent ---+
                                  |
                                  v
                            Final Response
```

## Technology Stack

- **Language:** Python
- **Local inference:** LFM2-VL 1.6B GGUF
- **Inference engine:** llama-cpp-python
- **Testing:** pytest, pytest-asyncio

## Project Structure

```text
BitChord/
├── app/
│   ├── agents/
│   │   ├── coder.py
│   │   ├── researcher.py
│   │   └── summarizer.py
│   ├── core/
│   │   ├── executor.py
│   │   ├── model.py
│   │   ├── router.py
│   │   └── state.py
│   └── main.py
├── models/
│   └── .gitkeep
├── tests/
│   ├── test_router.py
│   ├── test_state.py
│   └── test_executor.py
├── .gitignore
├── pytest.ini
├── requirements.txt
└── README.md
```

## Prerequisites

- Python 3.13 or a compatible Python version
- A Windows, Linux, or macOS environment supported by `llama-cpp-python`
- Sufficient RAM for the quantized model

## Installation

Clone the repository and enter the project directory:

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd BitChord
```

Create and activate a virtual environment.

**Windows PowerShell:**

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Model Setup

Download the required model files from the official [LiquidAI/LFM2-VL-1.6B-GGUF repository](https://huggingface.co/LiquidAI/LFM2-VL-1.6B-GGUF) and place them in the `models/` directory.

Expected filenames:

```text
models/
├── LFM2-VL-1.6B-Q4_0.gguf
└── mmproj-LFM2-VL-1.6B-Q8_0.gguf
```

The model files are excluded from GitHub because of their large size.

## Run the Application

From the repository root:

```bash
python -m app.main
```

Enter a request when prompted. BitChord selects a route, executes its workflow, and displays the final response.

## Run Tests

```bash
pytest -q
```

The routing, shared-state, and conditional execution graph tests can run without loading the AI model.

## Current Limitations

- Task routing uses keyword-based rules.
- Local inference speed and memory requirements depend on the computer.
- The model files must be downloaded separately.
- Async agent methods currently call synchronous model inference, so model calls are not truly concurrent.

## License

No license has been added yet. A license can be selected and added separately.
