# Local Fine-tuning on Mac (QLoRA with MLX)

Code hacked from here: https://github.com/ml-explore/mlx-examples/tree/main/lora

### How to Setup

1. Clone repo and navigate to this folder
2. Create Python env
```
python -m venv mlx-env
```
3. Activate env (bash/zsh)
```
source mlx-env/bin/activate
```
4. Install requirements
```
pip install -r requirements.txt
```
Note: MLX has the following requirements. More info [here](https://ml-explore.github.io/mlx/build/html/install.html).
- Using an M series chip (Apple silicon)
- Using a native Python >= 3.8
- macOS >= 13.5 (MacOS 14 recommended)
