
from dataclasses import dataclass
from pathlib import Path


@dataclass(frozen=True)   #frozen is use for create immutable data class
class DataIngestionConfig: #forzen use for to avoid accidental modification and consistent 
    root_dir:Path
    Source_URL:str
    local_data_file:Path
    unzip_dir:Path
