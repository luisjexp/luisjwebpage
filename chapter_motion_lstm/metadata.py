from pathlib import Path
import polars as pl
import LoadVideo as lv

METADF_FILENAME = "metadata.csv"
MANUALEDIT_VID_FILENAME = "manedit.mp4"
STANDARDIZED_FILENAME = "standardized.mp4"
STANDARDIZED_PREFIX = "std"
STANDARDIZED_COLUMN_NAME = "standardized_file"
VIDEO_ID_COLUMN = "video_id"
EDITED_COLUMN_NAME = "edited_file"
REQUIRED_METADATA_COLUMNS = [
    VIDEO_ID_COLUMN,
    EDITED_COLUMN_NAME,
    STANDARDIZED_COLUMN_NAME,
    "ParticipantID",
    "SessionID",
    "PromptID",
    "Trial",
    "Condition",
    "EngagementRating",
    "Notes",
]


def get_metadf_path(
    video_root: Path | str | None = None,
    metadata_fname: str = METADF_FILENAME,
) -> Path:
    return lv.get_data_root(video_root) / metadata_fname


def load_metadf(
    video_root: Path | str | None = None,
    metadata_fname: str = METADF_FILENAME,
) -> pl.DataFrame:
    path = get_metadf_path(video_root=video_root, metadata_fname=metadata_fname)
    assert path.is_file(), f"Metadata file not found: {path}"

    meta_df = pl.read_csv(path)
    for req_col in REQUIRED_METADATA_COLUMNS:
        assert req_col in meta_df.columns, f"Cannot load meta dataframe due to missing column: {req_col}"

    return meta_df 


def print_metadata_info(
        metadata_fname: str = METADF_FILENAME,
        data_root: Path | str | None = None
) -> None:
    root = lv.get_data_root(data_root)
    md = load_metadf(video_root=root, metadata_fname=metadata_fname)
    print(f"Metadata path: {Path(root) / metadata_fname}")
    print(f"Rows: {md.height} | Cols: {len(md.columns)}")
    print("Columns:", md.columns)


def get_video_metadata(
        video_id:str,
        metadata_fname: str = METADF_FILENAME,
        data_root: Path | str | None = None,
        as_dict = False
) -> pl.DataFrame :
    root = lv.get_data_root(data_root)
    
    md = load_metadf(video_root=root, metadata_fname=metadata_fname)
    row = md.filter(pl.col(VIDEO_ID_COLUMN) == video_id)
    
    assert row.height > 0, f"Meta data for video '{video_id}' not found"

    return row




