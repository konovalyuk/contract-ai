# from src.utils import greet
import fire

from text_completion import complete_text
from chat_completion import chat


def main():
    fire.Fire(chat)


if __name__ == "__main__":
    # print(greet("AI Project"))
    main()
