from src.ports.gateways.find.find_all_items_by_category_gateway import FindAllItemsByCategoryGateway


class FindAllItemsByCategoryUseCase:
    def __init__(self, gateway: FindAllItemsByCategoryGateway):
        self.gateway = gateway

    def run(self, category: str):
        return self.gateway.run(category)