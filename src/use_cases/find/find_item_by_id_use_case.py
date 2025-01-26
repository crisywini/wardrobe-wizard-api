from src.ports.gateways.find.find_item_by_id_gateway import FindItemByIdGateway


class FindItemByIdUseCase:

    def __init__(self, gateway: FindItemByIdGateway):
        self.gateway = gateway

    def run(self, id: str):
        return self.gateway.run(id)