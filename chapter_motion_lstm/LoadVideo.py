# Load Video Functions
import os
from pathlib import Path
from dotenv import load_dotenv
import numpy as np
import polars as pl
import cv2
import metadata as md

load_dotenv()

def get_data_root(video_root: Path | str | None = None) -> Path:
    if video_root is None:
        env_root = os.getenv("VIDEO_PATH") or os.getenv("DATA_ROOT")
        assert env_root, "Set VIDEO_PATH or DATA_ROOT to the dataset root folder."
        root = Path(env_root)
    else:
        root = Path(video_root)

    assert root.is_dir(), f"Dataset root not found: {root}"
    return root

def list_video_ids(video_root: Path | str | None = None) -> list[str]:
    root = get_data_root(video_root)
    return sorted(
        [
            p.name
            for p in root.iterdir()
            if p.is_dir() and not p.name.startswith(".")
        ]
    )

def get_video_dir(video_id: str, video_root: Path | str | None = None, require_exist=False) -> Path:
    vid_dir = get_data_root(video_root) / video_id
    if require_exist:
        assert Path.exists(vid_dir), f"Video directory does not exist /n {vid_dir}"

    return vid_dir

def ensure_video_dir(video_dir: Path) -> Path:
    video_dir.mkdir(parents=True, exist_ok=True)
    return video_dir

def scale_to_int(scale: float | int) -> int:
    value = float(scale)
    assert value > 0, f"scale must be positive, got {scale}"
    if value < 1:
        scale_int = int(round(value * 100))
    else:
        scale_int = int(round(value))
    assert 1 <= scale_int <= 99, f"scale must map to 1-99, got {scale_int}"
    return scale_int

def standardized_filename(norm_mode: str, target_fps: int, scale: float) -> str:
    scale_int = scale_to_int(scale)
    return f"{md.STANDARDIZED_PREFIX}-{norm_mode}_fps{target_fps}_s{scale_int}.mp4"

def get_video_file(
    video_id: str,
    kind: str = "standardized",
    video_root: Path | str | None = None,
    require_exists: bool = True,
) -> Path:
    video_dir = get_video_dir(video_id, video_root=video_root)

    if kind == "manual":
        path = video_dir / md.MANUALEDIT_VID_FILENAME
    elif kind == "standardized":
        path = video_dir / md.STANDARDIZED_FILENAME
    else:
        raise ValueError(f"Unknown kind: {kind}. Use 'manual' or 'standardized'.")

    if require_exists:
        assert path.is_file(), f"Missing {kind} video: {path}"
    return path

def get_log_path(
    video_id: str,
    filename: str,
    video_root: Path | str | None = None,
) -> Path:
    return get_video_dir(video_id, video_root=video_root) / filename

# ============================================================================
# Video Loaders

def get_np_video_array(
    fn_full,
    verbose: bool = False,
    plot_eg_frame: bool = False,
) -> np.ndarray:

    cap = cv2.VideoCapture(str(fn_full))
    assert cap.isOpened(), IOError(f"Could not open video file: {fn_full}")

    frames = []
    if verbose:
        print(f"Reading frames from: {fn_full}")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frames.append(frame)

    video_np_array = np.array(frames)

    if verbose:
        print(f"\nSuccessfully read {len(frames)} frames.")
        print(f"Shape + DType of the video array: {video_np_array.shape},{video_np_array.dtype}")
        print(f"Shape + DType of the video array: {video_np_array.shape},{video_np_array.dtype}")

    if plot_eg_frame:
        import matplotlib.pyplot as plt
        rgb = cv2.cvtColor(video_np_array[0], cv2.COLOR_BGR2RGB)
        plt.imshow(rgb)
        plt.title("First Frame (Color)")
        plt.axis("off")
        plt.show()

    cap.release()
    cv2.destroyAllWindows()
    return video_np_array

