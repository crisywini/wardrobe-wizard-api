from PIL import Image, ExifTags


class ConcatenateImagesVerticallyUseCase:

    def run(self, image_paths, output_path):
        #images = [Image.open(img) for img in image_paths]

        images = []

        for img_path in image_paths:
            img = Image.open(img_path)
            try:
                exif = img._getexif()
                if exif:
                    for tag, value in exif.items():
                        tag_name = ExifTags.TAGS.get(tag)
                        if tag_name == "Orientation":
                            if value == 3:
                                img = img.rotate(180, expand=True)
                            elif value == 6:
                                img = img.rotate(270, expand=True)
                            elif value == 8:
                                img = img.rotate(90, expand=True)
            except AttributeError:
                pass

            images.append(img)

        width = max(img.width for img in images)
        height = sum(img.height for img in images)

        new_image = Image.new("RGB", (width, height))

        y_offset = 0
        for img in images:
            new_image.paste(img, (0, y_offset))
            y_offset += img.height

        new_image.save(output_path)