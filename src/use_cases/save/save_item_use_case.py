from src.ports.gateways.save.save_item_gateway import SaveItemGateway
from src.domain.entities.item import Item

class SaveItemUseCase:
    def __init__(self, gateway: SaveItemGateway):
        self.gateway = gateway

    def run(self, item: Item):
        return self.gateway.run(item)

