from src.ports.gateways.delete.delete_all_outfits_gateway import DeleteAllOutfitsGateway


class DeleteAllOutfitsUseCase:

    def __init__(self, gateway: DeleteAllOutfitsGateway):
        self.gateway = gateway

    def run(self):
        return self.gateway.run()