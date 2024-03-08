from pathlib import Path

SRC_PATH = str(Path.cwd().joinpath(Path(__file__).parent.expanduser()))
DATA_PATH = str(Path(SRC_PATH).parent.joinpath('data'))