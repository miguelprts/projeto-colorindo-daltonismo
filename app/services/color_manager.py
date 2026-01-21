from ..data.repository import ColorRepository
from ..core.interfaces import ITranslationService

class ColorManager:
    def __init__(self, repo: ColorRepository, translator: ITranslationService):
        self.repo = repo
        self.translator = translator

    def identify_by_hex(self, hex_code: str):
        row, dist = self.repo.find_nearest_by_hex(hex_code)
        name_pt = self.translator.translate(row['Name'], 'en', 'pt')
        return {
            "status": "success",
            "name_en": row['Name'],
            "name_pt_br": name_pt,
            "matched_hex": f"#{row['Hex (24 bit)']}", # Apenas UM #
            "distance": float(dist)
        }

    def identify_by_name(self, color_name: str):
        name_en_search = self.translator.translate(color_name, 'pt', 'en')
        row, similarity = self.repo.find_by_name_fuzzy(name_en_search)
        
        if similarity < 0.95:
            return {"status": "error", "message": "Cor não encontrada"}

        name_pt = self.translator.translate(row['Name'], 'en', 'pt')
        return {
            "status": "success",
            "name_en": row['Name'],
            "name_pt_br": name_pt,
            "matched_hex": f"#{row['Hex (24 bit)']}",
            "similarity": float(similarity) # Alterado de string para float
        }