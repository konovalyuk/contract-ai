from typing import Optional
from llama_models.llama3.reference_impl.generation import Llama
from termcolor import cprint


def complete_text(
        ckpt_dir: str,
        temperature: float = 0.6,
        top_p: float = 0.9,
        max_seq_len: int = 512,
        max_batch_size: int = 4,
        max_gen_len: int = 64,
        model_parallel_size: Optional[int] = None,
):
    generator = Llama.build(
        ckpt_dir=ckpt_dir,
        max_seq_len=max_seq_len,
        max_batch_size=max_batch_size,
        model_parallel_size=model_parallel_size,
    )

    print("Enter text to completion (or write 'exit' to finish):")
    while True:
        prompt = input("Enter text: ")
        if prompt.lower() == "exit":
            print("Quit.")
            break

        result = generator.text_completion(
            prompt,
            temperature=temperature,
            top_p=top_p,
            max_gen_len=max_gen_len,
            logprobs=False,
        )

        cprint(f"{prompt}", end="")
        cprint(f"{result.generation}", color="yellow")
        print("\n==================================\n")
