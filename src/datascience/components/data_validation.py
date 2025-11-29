import os
import urllib.request as request
import zipfile
from src.datascience import logger
import pandas as pd
from src.datascience.entity.config_entity import DataValidationConfig


class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config

    def validate_all_columns(self) -> bool:
        try:
            validation_status = None

            # 1) read csv
            df = pd.read_csv(self.config.unzip_data_dir)

            # 2) columns from file and from schema
            all_cols = list(df.columns)
            all_schema = list(self.config.all_schema.keys())

            # 3) check each column
            for col in all_cols:
                if col not in all_schema:
                    validation_status = False
                    with open(self.config.STATUS_FILE, "w") as f:
                        f.write(f"validation status: {validation_status}")
                    break
            else:
                # runs only if loop DID NOT break => all columns OK.
                validation_status = True
                with open(self.config.STATUS_FILE, "w") as f:
                    f.write(f"validation status: {validation_status}")

            return validation_status

        except Exception as e:
            raise e
