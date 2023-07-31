from colorama import Fore, Style


def print_colored(agent, text, speaker):
    if speaker == 'agent':
        agent_colors = {
            "Julie:": Fore.YELLOW,
        }
        color = agent_colors.get(agent, "")
        print(color + f"{agent} {text}" + Style.RESET_ALL, end="")
    elif speaker == 'intro':
        agent_colors = {
            "": Fore.GREEN,
        }
        color = agent_colors.get(agent, "")
        print(color + f"{agent} {text}" + Style.RESET_ALL, end="")
    else:
        agent_colors = {
            "You:": Fore.RED,
        }
        color = agent_colors.get(agent, "")
        print(color + f"{agent} {text}" + Style.RESET_ALL, end="")


def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()
