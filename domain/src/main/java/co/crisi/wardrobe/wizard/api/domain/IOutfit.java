package co.crisi.wardrobe.wizard.api.domain;

import co.crisi.wardrobe.wizard.api.domain.data.OutfitCategory;

import java.util.List;

public interface IOutfit extends IEntity<Long> {

    List<IItem> getItems();

    Long getScore();

    OutfitCategory getCategory();
}
