from pathlib import Path
import polars as pl
import LoadVideo as lv
from typing import cast

FRAME_INDEX_COL = "FrameIndex"
META_FEATURES =  ["EngagementRating","Condition", "TaskType"]

EXTR_FEATURE_SPECS = [
    {
        "key": "position",
        "filename": "features_position.csv",
        "columns": ["FrameIndex", "x", "y"],
    },
    {
        "key": "moeng_skin",
        "filename": "features_moeng_skin.csv",
        "columns": ["FrameIndex", "moeng_skin"],
    },
    {
        "key": "moeng_motion",
        "filename": "features_moeng_motion.csv",
        "columns": ["FrameIndex", "moeng_motion"],
    },
    {
        "key": "moeng_combined",
        "filename": "features_moeng_combined.csv",
        "columns": ["FrameIndex", "moeng_combined"],
    },  
]

# #########################################
# EXTRACTED FEATURES
def all_extracted_feature_specs() -> pl.DataFrame:
    return pl.DataFrame(EXTR_FEATURE_SPECS)

def list_extracted_feature_keynames() -> list[str]:
    return [spec["key"] for spec in EXTR_FEATURE_SPECS]

def list_extracted_feature_fnames() -> list[str]:
    return [spec["filename"] for spec in EXTR_FEATURE_SPECS]

def vid_extracted_feature_path(
    video_id: str,
    key: str,
    video_root: Path | str | None = None,
    require_path_exists: bool = True
) -> Path:
    filename = next(
        (spec["filename"] for spec in EXTR_FEATURE_SPECS if spec["key"] == key),
        None,
    )
    assert filename is not None, f"Unknown feature key: {key}. Expected one of: {[spec['key'] for spec in EXTR_FEATURE_SPECS]}"
    path = lv.get_video_dir(video_id, video_root=video_root, require_exist=True) / filename

    if require_path_exists:
        assert path.is_file(), f"Missing feature file: {path}"
    
    return path


def video_init_extracted_feature_df(video_id: str, data_root: Path | str | None = None) -> pl.DataFrame:
    data_root = lv.get_data_root(data_root)

    dfs = []
    for extracted_feat in list_extracted_feature_keynames():
        path = vid_extracted_feature_path(video_id, extracted_feat, require_path_exists=True)       
        dfs.append(pl.read_csv(path))

    assert dfs, f"No extracted feature files found for video_id={video_id}"
    df_features = dfs[0]
    for df in dfs[1:]:
        df_features = df_features.join(df, on=FRAME_INDEX_COL, how="inner")


    return df_features

# FINALIZED FEATURE DATA SET
def video_extracted_feature_df(video_id: str, data_root: Path | str | None = None) -> pl.DataFrame:
    df = video_init_extracted_feature_df(video_id,data_root)
    df = compute_speed_vector(df)
    return df

# #########################################
# VIDEO META DATA
def video_meta_features_df(video_id: str) -> pl.DataFrame:
    import metadata 
    vid_meta_df =  metadata.get_video_metadata(video_id,as_dict=False)
    vid_meta_df = vid_meta_df.select(META_FEATURES)
    return vid_meta_df



# #########################################
# DERIVE OTHER VARIABLES
def compute_speed_vector(df: pl.DataFrame) -> pl.DataFrame:
    assert "x" in df.columns, f"data frame must contain variable 'x' to commpute speed"
    assert "y" in df.columns, f"data frame must contain variable 'y' to commpute speed"

    dx = pl.col("x").diff()
    dy = pl.col("y").diff()
    df = df.with_columns(
        (dx.pow(2) + dy.pow(2)).sqrt().fill_null(0).alias("Speed"),
        (pl.arctan2(dy, dx)).degrees().fill_null(0).alias("Direction"),
    )

    return df

