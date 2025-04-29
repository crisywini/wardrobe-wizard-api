from delete_interface import DeleteById
from src.ports.gateways.delete.delete_item_by_id_gateway import DeleteItemByIdGateway

class DeleteItemById(DeleteById):
    
    
    def __init__(self, item_gateway: DeleteItemByIdGateway):
        self.item_gateway = item_gateway
        
