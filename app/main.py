import asyncio

from app.core.model import LocalLLM
from app.core.executor import BitChordExecutor


MODEL_PATH = "models/LFM2-VL-1.6B-Q4_0.gguf"
MMPROJ_PATH = "models/mmproj-LFM2-VL-1.6B-Q8_0.gguf"


async def main():
    print("=" * 60)
    print("BITCHORD - LOCAL AI ORCHESTRATION")
    print("=" * 60)

    print("\nLoading local LFM2-VL model...")

    llm = LocalLLM(
        model_path=MODEL_PATH,
        mmproj_path=MMPROJ_PATH,
        context_size=2048,
    )

    print("Model loaded successfully.")

    executor = BitChordExecutor(llm)

    user_input = input("\nEnter your request: ")

    state = await executor.run(user_input)

    print("\n" + "=" * 60)
    print("BITCHORD RESPONSE")
    print("=" * 60)

    print(f"Route selected: {state.route}")
    print(f"Execution graph: {state.execution_graph}")
    print(f"Completed steps: {state.completed_steps}")
    print(f"Step timestamps: {state.step_timestamps}")
    print("\nFinal response:")
    print(state.final_response)


if __name__ == "__main__":
    asyncio.run(main())
