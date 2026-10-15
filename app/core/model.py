from pathlib import Path
import os

from llama_cpp import Llama
from llama_cpp.llama_chat_format import MTMDChatHandler


class LocalLLM:
    """
    Local LFM2-VL 1.6B model for BitChord.

    Features:
    - Local GGUF inference
    - CPU-only execution
    - Multimodal support through MTMD
    - No external AI API
    """

    def __init__(
        self,
        model_path: str,
        mmproj_path: str,
        context_size: int = 4096,
    ):
        self.model_path = Path(model_path)
        self.mmproj_path = Path(mmproj_path)

        if not self.model_path.exists():
            raise FileNotFoundError(
                f"Model file not found: {self.model_path}"
            )

        if not self.mmproj_path.exists():
            raise FileNotFoundError(
                f"MMProj file not found: {self.mmproj_path}"
            )

        # Multimodal projector for LFM2-VL.
        # use_gpu=False keeps the entire project CPU-only.
        self.chat_handler = MTMDChatHandler(
            clip_model_path=str(self.mmproj_path),
            verbose=False,
            use_gpu=False,
        )

        # Local CPU inference.
        self.llm = Llama(
            model_path=str(self.model_path),
            chat_handler=self.chat_handler,
            n_ctx=context_size,
            n_gpu_layers=0,
            n_threads=max(1, (os.cpu_count() or 4) - 2),
            verbose=False,
        )

    def generate(
        self,
        prompt: str,
        max_tokens: int = 256,
        temperature: float = 0.2,
    ) -> str:
        """
        Generate a text response using the local LFM2-VL model.
        """

        response = self.llm.create_chat_completion(
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            max_tokens=max_tokens,
            temperature=temperature,
        )

        content = response["choices"][0]["message"].get("content", "")

        print("\n[DEBUG MODEL OUTPUT]")
        print(repr(content))

        return content
