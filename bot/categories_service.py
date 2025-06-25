import json
from typing import Dict, List
from config import settings

class CategoryService:
    def __init__(self):
        self.categories: Dict[str, List[str]] = {}
        self.load_categories()

    def load_categories(self):
        try:
            with open(settings.CATEGORIES_FILE, 'r', encoding='utf-8') as f:
                self.categories = json.load(f)
        except Exception as e:
            raise Exception(f"Failed to load categories: {e}")

    def get_all_categories(self) -> List[str]:
        return list(self.categories.keys())

    def get_subcategories(self, category: str) -> List[str]:
        return self.categories.get(category, [])

category_service = CategoryService()
