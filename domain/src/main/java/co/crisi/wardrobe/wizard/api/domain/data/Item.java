package co.crisi.wardrobe.wizard.api.domain.data;

import co.crisi.wardrobe.wizard.api.domain.IItem;
import co.crisi.wardrobe.wizard.api.domain.validator.decorator.NonNullValidatorDecorator;
import co.crisi.wardrobe.wizard.api.domain.validator.decorator.Validator;

public record Item(Long id, String name, String description, String imageUrl,
                   String color, String size, String brand, String material,
                   ItemCategory category, ItemType type) implements IItem {


    public Item(Long id, String name, String description, String imageUrl,
                String color, String size, String brand, String material,
                ItemCategory category, ItemType type) {

        var validator = new Validator();
        var nonNullValidator = new NonNullValidatorDecorator(validator);

        this.id = nonNullValidator.validate(id, "item id");
        this.name = nonNullValidator.validate(name, "item name");
        this.description = nonNullValidator.validate(description, "item description");
        this.imageUrl = nonNullValidator.validate(imageUrl, "item image url");
        this.color = nonNullValidator.validate(color, "item color");
        this.size = nonNullValidator.validate(size, "item size");
        this.brand = nonNullValidator.validate(brand, "item brand");
        this.material = nonNullValidator.validate(material, "item material");
        this.category = nonNullValidator.validate(category, "item category");
        this.type = nonNullValidator.validate(type, "item type");

    }

    @Override
    public String getName() {
        return name;
    }

    @Override
    public String getDescription() {
        return description;
    }

    @Override
    public String getImageUrl() {
        return imageUrl;
    }

    @Override
    public String getColor() {
        return color;
    }

    @Override
    public String getSize() {
        return size;
    }

    @Override
    public String getBrand() {
        return brand;
    }

    @Override
    public String getMaterial() {
        return material;
    }

    @Override
    public ItemCategory getCategory() {
        return category;
    }

    @Override
    public ItemType getType() {
        return type;
    }

    @Override
    public Long getId() {
        return id;
    }
}
