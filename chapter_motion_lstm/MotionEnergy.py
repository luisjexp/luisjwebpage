# Motion Energy Calculation Script
import cv2
import numpy as np
import polars as pl


def moeng_framepairs(frame1: np.ndarray, frame2: np.ndarray, force_gray: bool = False) -> float:
    if force_gray:
        if frame1.ndim == 3:
            frame1 = cv2.cvtColor(frame1, cv2.COLOR_BGR2GRAY)
        if frame2.ndim == 3:
            frame2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2GRAY)

    if frame1.shape != frame2.shape:
        raise ValueError(f"Frame shape mismatch: {frame1.shape} vs {frame2.shape}")

    diff_frame = cv2.absdiff(frame1, frame2)
    return float(np.sum(diff_frame))


def moeng_video(video_np_array: np.ndarray, force_gray: bool = False) -> pl.DataFrame:
    video_np_array = np.asarray(video_np_array)
    if video_np_array.ndim not in (3, 4):
        raise ValueError(f"Expected video array with 3 or 4 dims, got {video_np_array.ndim}")

    if video_np_array.shape[0] < 2:
        return pl.DataFrame({
            "FrameIndex": pl.Series([], dtype=pl.Int32),
            "MotionEnergy": pl.Series([], dtype=pl.Float64),
        })

    rows = []
    for i in range(1, video_np_array.shape[0]):
        frame1 = video_np_array[i - 1]
        frame2 = video_np_array[i]
        energy = moeng_framepairs(frame1, frame2, force_gray=force_gray)
        rows.append({"FrameIndex": i, "MotionEnergy": energy})

    return pl.DataFrame(rows).with_columns(
        pl.col("FrameIndex").cast(pl.Int32)
    )

