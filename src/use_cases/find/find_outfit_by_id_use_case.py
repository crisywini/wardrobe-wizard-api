from src.ports.gateways.find.find_outfit_by_id_gateway import FindOutfitByIdGateway


class FindOutfitByIdUseCase:
    def __init__(self, gateway: FindOutfitByIdGateway):
        self.gateway = gateway

    def run(self, id:str):
        return self.gateway.run(id)
