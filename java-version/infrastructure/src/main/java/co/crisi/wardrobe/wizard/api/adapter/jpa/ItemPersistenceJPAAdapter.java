package co.crisi.wardrobe.wizard.api.adapter.jpa;

import co.crisi.wardrobe.wizard.api.domain.IItem;
import co.crisi.wardrobe.wizard.api.mapper.jpa.ItemJPAMapper;
import co.crisi.wardrobe.wizard.api.port.spi.IItemPersistencePort;
import co.crisi.wardrobe.wizard.api.repository.jpa.ItemJpaRepository;
import lombok.RequiredArgsConstructor;
import org.mapstruct.factory.Mappers;
import org.springframework.stereotype.Repository;

import java.util.ArrayList;
import java.util.Collection;
import java.util.List;
import java.util.Optional;

@Repository
@RequiredArgsConstructor
public class ItemPersistenceJPAAdapter implements IItemPersistencePort {

    private final ItemJpaRepository repository;

    private final ItemJPAMapper mapper = Mappers.getMapper(ItemJPAMapper.class);

    @Override
    public IItem save(IItem entity) {
        return repository.save(mapper.map(entity));
    }

    @Override
    public Optional<IItem> findById(Long id) {
        var entity = repository.findById(id).orElse(null);
        return Optional.ofNullable(entity);
    }

    @Override
    public List<IItem> findAll() {
        return List.copyOf(new ArrayList<>((Collection<? extends IItem>) repository.findAll()));
    }

    @Override
    public void deleteById(Long id) {
        repository.deleteById(id);
    }

    @Override
    public boolean existsById(Long id) {
        return repository.existsById(id);
    }
}
