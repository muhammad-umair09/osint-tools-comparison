import json
import logging
import pandas as pd
import numpy as np
from app.config import DATA_FILE_PATH, WEIGHTS

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class OSINTEngine:
    def __init__(self):
        self.data_path = DATA_FILE_PATH
        self.raw_data = self._load_dataset()
        
    def _load_dataset(self):
        try:
            with open(self.data_path, 'r') as file:
                return json.load(file)
        except Exception as e:
            logging.error(f"Failed to load dataset from {self.data_path}: {str(e)}")
            return []

    def calculate_composite_score(self, tool):
        """Calculates a weighted normalization composite score between 1 and 10."""
        # Feature and Data source scores are calculated based on list lengths normalized to scale 1-10
        feature_score = min(len(tool.get("features", [])) * 2.5, 10.0)
        ds_score = min(len(tool.get("data_sources", [])) * 2.0, 10.0)
        
        score = (
            (feature_score * WEIGHTS["features"]) +
            (tool.get("ease_of_use", 5) * WEIGHTS["ease_of_use"]) +
            (tool.get("accuracy", 5) * WEIGHTS["accuracy"]) +
            (tool.get("performance", 5) * WEIGHTS["performance"]) +
            (tool.get("automation", 5) * WEIGHTS["automation"]) +
            (tool.get("reporting", 5) * WEIGHTS["reporting"]) +
            (ds_score * WEIGHTS["data_sources"])
        )
        return round(score, 2)

    def get_processed_dataframe(self):
        if not self.raw_data:
            return pd.DataFrame()
        
        processed_tools = []
        for tool in self.raw_data:
            tool_copy = tool.copy()
            tool_copy["composite_score"] = self.calculate_composite_score(tool)
            # Flatten lists to comma-separated strings for tabular presentation
            tool_copy["features"] = ", ".join(tool["features"])
            tool_copy["data_sources"] = ", ".join(tool["data_sources"])
            tool_copy["use_cases"] = ", ".join(tool["use_cases"])
            tool_copy["advantages"] = ", ".join(tool["advantages"])
            tool_copy["limitations"] = ", ".join(tool["limitations"])
            processed_tools.append(tool_copy)
            
        df = pd.DataFrame(processed_tools)
        return df.sort_values(by="composite_score", ascending=False)