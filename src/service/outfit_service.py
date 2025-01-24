from domain.outfit import Outfit


class OutfitService:
    
    def __init__(self, repository):
        self.repository = repository
        
    def save(self, outfit):
        return str(self.repository.insert_outfit(outfit))
    
    def get_all(self):
        return self.repository.find_all_outfits()