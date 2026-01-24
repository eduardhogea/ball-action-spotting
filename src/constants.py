from pathlib import Path
import os

work_dir = Path(os.environ.get("BALL_ACTION_WORKDIR", "/workdir"))
if not work_dir.exists():
    work_dir = Path(__file__).resolve().parents[1]
data_dir = work_dir / "data"
configs_dir = work_dir / "configs"
soccernet_dir = data_dir / "soccernet"
