from src.ports.gateways.find.find_all_items_gateway import FindAllItemsGateway


class FindAllItemsUseCase:
    def __init__(self, gateway: FindAllItemsGateway):
        self.gateway = gateway

    def run(self):
        self.gateway.run()
