package co.crisi.wardrobe.wizard.api.domain;

import co.crisi.wardrobe.wizard.api.domain.data.ItemCategory;
import co.crisi.wardrobe.wizard.api.domain.data.ItemType;

public interface IItem extends IEntity<Long> {

    String getName();
    String getDescription();
    String getImageUrl();
    String getColor();
    String getSize();
    String getBrand();
    String getMaterial();
    ItemCategory getCategory();
    ItemType getType();

}
