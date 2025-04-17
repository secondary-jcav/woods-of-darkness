import yaml
from pathlib import Path
import glob
import os
from typing import Dict

from models.entities import Scene, Choice


def load_scenes_from_yaml(path: str) -> Dict[str, Scene]:
    with open(path) as f:
        raw = yaml.safe_load(f)

    scenes: Dict[str, Scene] = {}
    for scene_id, data in raw.items():
        choices = {
            key: Choice(desc["description"], desc.get("next_scene"))
            for key, desc in data["choices"].items()
        }
        scenes[scene_id] = Scene(scene_id, data["text"], choices)
    return scenes


def load_all_chapters(dir_path: str) -> Dict[str, Scene]:
    scenes: Dict[str, Scene] = {}
    for path in sorted(glob.glob(os.path.join(dir_path, '*.yaml'))):
        ep = Path(path).stem       # e.g. "episode1"
        raw = yaml.safe_load(open(path))
        for scene_id, data in raw.items():
            # prefix IDs to avoid collisions:
            full_id = f"{ep}.{scene_id}"
            choices = {
                key: Choice(c["description"],
                            # prefix next_scene if present
                            (f"{ep}.{c['next_scene']}" if c.get("next_scene") else None))
                for key, c in data["choices"].items()
            }
            scenes[full_id] = Scene(full_id, data["text"], choices)
    return scenes
