from difflib import SequenceMatcher
import pandas as pd
from ..core.interfaces import IColorMath

class ColorRepository:
    def __init__(self, csv_path: str, math_service: IColorMath):
        self.df = pd.read_csv(csv_path)
        self.math = math_service
        self._normalize_data()

    def _normalize_data(self):
        # Garante que o HEX não tenha # extra e esteja limpo
        self.df['Hex (24 bit)'] = self.df['Hex (24 bit)'].astype(str).str.replace('#', '').str.strip().str.upper()
        self.df['Name_Lower'] = self.df['Name'].str.lower().str.strip()

    def find_nearest_by_hex(self, target_hex: str):
        clean_hex = target_hex.replace('#', '').upper()
        target_rgb = self.math.hex_to_rgb(clean_hex)
        target_hsl = self.math.rgb_to_hsl(*target_rgb)
        
        def get_dist(row_hex):
            try:
                rgb = self.math.hex_to_rgb(row_hex)
                return self.math.calculate_distance(target_hsl, self.math.rgb_to_hsl(*rgb))
            except: return 999
            
        distances = self.df['Hex (24 bit)'].apply(get_dist)
        idx = distances.idxmin()
        return self.df.loc[idx], distances[idx]

    def find_by_name_fuzzy(self, search_name: str):
        search_name = search_name.lower().strip()
        
        def get_similarity(row_name):
            # SequenceMatcher dá um score de 0 a 1
            return SequenceMatcher(None, search_name, row_name).ratio()
        
        similarities = self.df['Name_Lower'].apply(get_similarity)
        idx = similarities.idxmax()
        return self.df.loc[idx], similarities[idx]