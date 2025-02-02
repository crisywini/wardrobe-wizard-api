from src.ports.gateways.find.find_all_outfits_gateway import FindAllOutfitsGateway


class FindAllOutfitCategoriesUseCase:
    def __init__(self, gateway: FindAllOutfitsGateway):
        self.gateway = gateway

    def run(self) -> set:
        outfits = self.gateway.run()
        return set(map(lambda outfit: outfit.category, outfits))
