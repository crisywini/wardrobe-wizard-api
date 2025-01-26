from src.ports.gateways.find.find_all_outfits_by_category_gateway import FindAllOutfitsByCategoryGateway


class FindAllOutfitsByCategoryUseCase:
    def __init__(self, gateway: FindAllOutfitsByCategoryGateway):
        self.gateway = gateway

    def run(self, category: str):
        return self.gateway.run(category)