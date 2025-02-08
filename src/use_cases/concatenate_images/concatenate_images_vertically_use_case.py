from PIL import Image


class ConcatenateImagesVerticallyUseCase:

    def run(self, image_paths, output_path):
        images = [Image.open(img) for img in image_paths]

        width = max(img.width for img in images)
        height = sum(img.height for img in images)

        new_image = Image.new("RGB", (width, height))

        y_offset = 0
        for img in images:
            new_image.paste(img, (0, y_offset))
            y_offset += img.height

        new_image.save(output_path)