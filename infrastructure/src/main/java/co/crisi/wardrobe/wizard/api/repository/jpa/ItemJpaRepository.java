package co.crisi.wardrobe.wizard.api.repository.jpa;


import co.crisi.wardrobe.wizard.api.entity.ItemJPAEntity;
import org.springframework.data.repository.CrudRepository;
import org.springframework.stereotype.Repository;

@Repository
public interface ItemJpaRepository extends CrudRepository<ItemJPAEntity, Long> {
}
