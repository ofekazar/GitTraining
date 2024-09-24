import os
import platform
import subprocess
import shlex
from collections import deque
from rich.live import Live
from rich.console import Console
from rich.panel import Panel
from rich.layout import Layout
from rich.text import Text


LOG_COMMAND = "git log --graph --pretty=short --all"
COMMAND_HISTORY = 12
DIR_PATH = os.path.dirname(os.path.realpath(__file__))
DEMO_PATH = f"{DIR_PATH}\..\git_demo"


def get_git_log(path):
    """
    :path (str): A path to a git repository.
    :returns (str): The stdout of the git log command in the given path.
    """
    result = subprocess.run(
        shlex.split(LOG_COMMAND),
        capture_output=True,
        text=True,
        cwd=path
    )
    return result.stdout if result.returncode == 0 else ""


def make_layout(left_text, log_graph, commands, last_result):
    layout = Layout()
    left_layout = Layout()

    text_layout = Layout(Panel(Text(f"{left_text}\n\nPress Enter To Continue ->"), title="Command Overview", border_style="bold blue",), name="text_layout")
    command_history_layout = Layout(Panel(Text("\n".join(commands) + f"\n\n{last_result}"), title="Previous Commands", border_style="bold blue"), name="command_history_layout")
    git_graph_layout = Layout(Panel(log_graph, title="Git Log Graph", border_style="bold blue"), name="git_graph_layout")

    left_layout.split_column(
        text_layout,
        git_graph_layout,
    )
    layout.split_row(
        left_layout,
        command_history_layout
    )
    return layout


def recreate_demo_folder():
    """
    Make sure the demo folder is empty.
    """
    if os.path.exists(DEMO_PATH):
        system = platform.system()
        if system == "Windows":
            subprocess.run(f'rmdir /S /Q "{DEMO_PATH}"', capture_output=True, shell=True)
        else: # Linux / Mac
            subprocess.run(f'rm -rf "{DEMO_PATH}"', capture_output=True, shell=True)

    os.makedirs(DEMO_PATH)


def run_command_demo(command):
    result = subprocess.run(shlex.split(command), capture_output=True, text=True, cwd=DEMO_PATH)
    output = result.stdout if result.returncode == 0 else result.stderr

    if isinstance(command, list):
        command = " ".join(command)
    return f">>> {command}", output


def command_sequence():
    yield f"First, before this demo started, I created an empty folder in '{DEMO_PATH}'. " \
           "You can open it and look at the changes done to it as we go. This demo is meant to show you how to add and commit changes.\n" \
           "We will now run the command 'git init' to start a new git project in that folder."
    yield run_command_demo("git init")
    yield "This command creates a new hidden folder in our project called .git. " \
          "You might be able to see the folder if your windows explorer is configured to show hidden files. " \
          "This folder contains all the tracking data for git and git is operated within it for this given project.\n\n" \
         f"You might have already noticed it, the pane on the right will show the commands history."

    filename = "hello.txt"
    text = "Hello World!"
    yield f"We will now create a new file in the folder called {filename} and add the text '{text}' to it."

    with open(f"{DEMO_PATH}/{filename}", "w") as f:
        f.write(f"{text}\n")

    yield "The file is now created. We can see that git detects the change using the command 'git status'. " \
          "This commands lets us see the current status of our local git repository."
    yield run_command_demo("git status")
    yield "We can see the a new Untracked file called hello.txt. We can add it and stage it for the next commit using the command 'git add'"
    yield run_command_demo(f"git add {filename}")
    yield "Now the file is staged for the next commit. Let's see it by running 'git status' again"
    yield run_command_demo("git status")
    yield "Git marked the file as a new file and is staged for the next commit. " \
          "All that's left to do now is commit our changes. We will use the command 'git commit -m 'commit message''.\n" \
          "The commit message is a short description of our commit."
    yield run_command_demo("git commit -m 'Added the file hello.txt'")
    yield "We commited our first commit! We can now see it on the right pane of our program. The right side of this software " \
          "shows all the commit we created in a nice graph. The command that is used to show it is\n\n" \
          "git log --graph --pretty=short --all"

    filename2 = "file2.txt"
    text2 = "Hello World 2"
    yield f"A commit holds a set of changes from the stage of the repository in the previous commit. Before the first commit the state of the repository is empty. In our case, the first commit contains the new file {filename} with the text {text} inside it."
    yield f"We can create a commit with more then on file changed. We will add the text {text2} to our file and create a new file called {filename2}"

    with open(f"{DEMO_PATH}/{filename}", "a") as f:
        f.write(text2)
    open(f"{DEMO_PATH}/{filename2}", "w")

    yield "The files are now created, lets run 'git status' to see the changes."
    yield run_command_demo("git status")
    yield f"We can see the {filename} is under the tracked items list (Changes that are not staged for commit:) and {filename2} is under the untracked files list.\n" \
           "Tracked files are files that we previously commited to this repository and we are now changing their content.\n" \
           "Untracked files are new files in the repository that we can choose to add for commit."
    yield "We will add both files"
    yield run_command_demo(f"git add {filename} {filename2}")
    yield "Now both files are added and both are tracked by git. We will run 'git status' one last time."
    yield run_command_demo("git status")
    yield "And now commit the changes."
    yield run_command_demo("git commit -m 'Change hello.txt content and add new file file2.txt'")
    yield f"We can see the new commit was added to the list of commits. The list below is generated using the command: '{LOG_COMMAND}'"
    yield "Thank you for going through this demo. This was meant to show you how git is used in your own terminal. " \
          "There was a lot of commands and information missing from this so you should now continue with: https://learngitbranching.js.org/"


def main():
    recreate_demo_folder()

    console = Console()
    text = Text("Welcome to 'git in 30' local demo.", justify="left")
    commands = deque()
    last_result = ""
    with Live(make_layout(text, get_git_log(DEMO_PATH), commands, last_result), refresh_per_second=1, console=console) as live:
        try:
            for output in command_sequence():
                if isinstance(output, tuple):
                    commands.append(output[0])
                    if len(commands) > COMMAND_HISTORY:
                        commands.popleft()

                    last_result = output[1]
                    output = "\n\n".join(output)
                new_layout = make_layout(output, get_git_log(DEMO_PATH), commands, last_result)

                input("")
                live.update(new_layout)
        except KeyboardInterrupt:
            print("Stopped by the user")


if __name__ == "__main__":
    main()
