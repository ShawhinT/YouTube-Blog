# MLX Fine-tuning

# Code authored by: Shaw Talebi
# Video link: coming soon!
# Blog link: coming soon!

# Source: https://github.com/ml-explore/mlx-examples/tree/main/lora

import subprocess

def run_command_with_live_output(command: list[str]) -> None:
    """
    Courtesy of ChatGPT:
    Runs a command and prints its output line by line as it executes.

    Args:
        command (List[str]): The command and its arguments to be executed.

    Returns:
        None
    """
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    # Print the output line by line
    while True:
        output = process.stdout.readline()
        if output == '' and process.poll() is not None:
            break
        if output:
            print(output.strip())
        
    # Print the error output, if any
    err_output = process.stderr.read()
    if err_output:
        print(err_output)


# prompt format
intstructions_string = f"""ShawGPT, functioning as a virtual data science consultant on YouTube, communicates in clear, accessible language, escalating to technical depth upon request. \
It reacts to feedback aptly and ends responses with its signature '–ShawGPT'. \
ShawGPT will tailor the length of its responses to match the viewer's comment, providing concise acknowledgments to brief expressions of gratitude or feedback, \
thus keeping the interaction natural and engaging.

Please respond to the following comment.
"""

prompt_builder = lambda comment: f'''<s>[INST] {intstructions_string} \n{comment} \n[/INST]\n'''


# run inference with quantized model
model_path = "mlx-community/Mistral-7B-v0.2-4bit"
max_tokens = "50"
prompt = prompt_builder("Great content, thank you!")

# define and run command
command = ['python', 'lora.py', '--model', model_path, '--max-tokens', max_tokens, '--prompt', prompt]
run_command_with_live_output(command)


# fine-tune with LoRA
num_iters = "400"
steps_per_eval = "100"

# define and run command
command = ['python', 'lora.py', '--model', model_path, '--train', '--iters', num_iters, '--steps-per-eval', steps_per_eval, '--test']
run_command_with_live_output(command)