from src.ports.gateways.find.find_all_outfits_gateway import FindAllOutfitsGateway


class FindAllOutfitsUseCase:
    def __init__(self, gateway: FindAllOutfitsGateway):
        self.gateway = gateway

    def run(self):
        return self.gateway.run()