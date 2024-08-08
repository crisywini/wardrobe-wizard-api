package co.crisi.wardrobe.wizard.api.domain;

import java.util.List;

public interface IOutfit extends IEntity<Long> {

    List<IItem> getItems();

    Long getScore();

    String getCategory();
}
