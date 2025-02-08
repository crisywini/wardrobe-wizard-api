from src.adapters.controller.config.constants import URL_IMAGE_DEFAULT_FE_PATH
from src.ports.gateways.save.save_outfit_gateway import SaveOutfitGateway
from src.domain.entities.outfit import Outfit
from src.use_cases.concatenate_images.concatenate_images_vertically_use_case import ConcatenateImagesVerticallyUseCase


class SaveOutfitUseCase:
    def __init__(self, gateway: SaveOutfitGateway):
        self.gateway = gateway
        self.concatenate_images_vertically_use_case = ConcatenateImagesVerticallyUseCase()

    def run(self, outfit: Outfit):
        shirt = list(filter(lambda i: i["category"] == 'shirts', outfit.items))[0]
        pants = list(filter(lambda i: i["category"] == 'pants', outfit.items))[0]
        shoes = list(filter(lambda i: i["category"] == 'shoes', outfit.items))[0]
        print(shirt)
        print(pants)
        print(shoes)
        file_name = outfit.name + ".png"
        self.concatenate_images_vertically_use_case.run([shirt["image_url"], pants["image_url"], shoes["image_url"]],
                                                        f"{URL_IMAGE_DEFAULT_FE_PATH}/{file_name}")
        outfit.default_image_url = f"{URL_IMAGE_DEFAULT_FE_PATH}/{file_name}"

        return self.gateway.run(outfit)
