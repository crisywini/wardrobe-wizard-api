from src.ports.gateways.save.save_outfit_gateway import SaveOutfitGateway
from src.domain.entities.outfit import Outfit

class SaveOutfitUseCase:
    def __init__(self, gateway: SaveOutfitGateway):
        self.gateway = gateway

    def run(self, outfit: Outfit):
        return self.gateway.run(outfit)