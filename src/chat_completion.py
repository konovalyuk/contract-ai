from typing import Optional

from llama_models.llama3.api.datatypes import UserMessage, CompletionMessage, SystemMessage
from llama_models.llama3.reference_impl.generation import Llama

MAX_DIALOG_LENGTH = 256  # Token limit

def truncate_dialog(dialog, max_length):
    total_tokens = 0
    truncated_dialog = []
    for message in reversed(dialog):
        message_tokens = len(message.content.split())
        if total_tokens + message_tokens <= max_length:
            truncated_dialog.insert(0, message)
            total_tokens += message_tokens
        else:
            break
    return truncated_dialog


def chat(
        ckpt_dir: str,
        temperature: float = 0.6,
        top_p: float = 0.9,
        max_seq_len: int = 512,
        max_batch_size: int = 4,
        max_gen_len: Optional[int] = None,
        model_parallel_size: Optional[int] = None,
):
    generator = Llama.build(
        ckpt_dir=ckpt_dir,
        max_seq_len=max_seq_len,
        max_batch_size=max_batch_size,
        model_parallel_size=model_parallel_size,
    )

    dialog = []
    print("Start a chat. Type 'exit' to quit.")

    while True:
        user_input = input("You: ")
        if user_input.strip().lower() == "exit":
            print("Exiting chat. Goodbye!")
            break

        # Add user message to dialog
        dialog.append(UserMessage(role="user", content=user_input))

        dialog = truncate_dialog(dialog, MAX_DIALOG_LENGTH)
        # Generate assistant response
        result = generator.chat_completion(
            dialog,
            max_gen_len=max_gen_len,
            temperature=temperature,
            top_p=top_p,
        )

        # Get assistant message
        assistant_message = result.generation
        dialog.append(assistant_message)

        # Print messages
        print(f"Assistant: {assistant_message.content}")
        print("\n==================================\n")
