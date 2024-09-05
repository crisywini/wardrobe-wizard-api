package co.crisi.wardrobe.wizard.api.service;

import co.crisi.wardrobe.wizard.api.domain.IItem;
import co.crisi.wardrobe.wizard.api.exception.business.BusinessException;
import co.crisi.wardrobe.wizard.api.exception.business.ItemNotFoundException;
import co.crisi.wardrobe.wizard.api.port.api.IItemServicePort;
import co.crisi.wardrobe.wizard.api.port.spi.IItemPersistencePort;
import lombok.RequiredArgsConstructor;

import java.util.List;

@RequiredArgsConstructor
public class ItemServicePort implements IItemServicePort {

    private final IItemPersistencePort persistencePort;


    @Override
    public IItem save(IItem entity) {
        return persistencePort.save(entity);
    }

    @Override
    public IItem getById(Long id) {

        return persistencePort.findById(id)
                .orElseThrow(() -> new ItemNotFoundException(String.format("The item with id %s was not found!", id)));
    }

    @Override
    public List<IItem> getAll() {
        return persistencePort.findAll();
    }

    @Override
    public IItem update(Long id, IItem newInfo) {

        if(!persistencePort.existsById(id)){
            throw new ItemNotFoundException(String.format("The item with id %s was not found!", id));
        }
        if(!id.equals(newInfo.getId())){
            throw new BusinessException("The item id and the new item id are different");
        }

        return save(newInfo);
    }

    @Override
    public void deleteById(Long id) {
        if(!persistencePort.existsById(id)){
            throw new ItemNotFoundException(String.format("The item with id %s was not found!", id));
        }
        persistencePort.deleteById(id);
    }
}
