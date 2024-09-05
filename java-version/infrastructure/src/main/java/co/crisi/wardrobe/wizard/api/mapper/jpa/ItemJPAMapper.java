package co.crisi.wardrobe.wizard.api.mapper.jpa;

import co.crisi.wardrobe.wizard.api.domain.IItem;
import co.crisi.wardrobe.wizard.api.entity.ItemJPAEntity;
import org.mapstruct.Mapper;

@Mapper
public interface ItemJPAMapper {
    ItemJPAEntity map(IItem item);
}
