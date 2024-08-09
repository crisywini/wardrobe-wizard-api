package co.crisi.wardrobe.wizard.api.service;

import co.crisi.wardrobe.wizard.api.domain.IOutfit;
import co.crisi.wardrobe.wizard.api.exception.business.BusinessException;
import co.crisi.wardrobe.wizard.api.exception.business.OutfitNotFoundException;
import co.crisi.wardrobe.wizard.api.exception.business.RepeatedOutfitException;
import co.crisi.wardrobe.wizard.api.port.api.IOutfitServicePort;
import co.crisi.wardrobe.wizard.api.port.spi.IOutfitPersistencePort;
import lombok.RequiredArgsConstructor;

import java.util.List;
import java.util.Objects;


@RequiredArgsConstructor
public class OutfitServicePort implements IOutfitServicePort {

    private final IOutfitPersistencePort persistencePort;

    @Override
    public IOutfit save(IOutfit entity) {
        if (Objects.nonNull(entity.getId()) && persistencePort.existsById(entity.getId())) {
            throw new RepeatedOutfitException(String.format("The outfit with id %d already exists!", entity.getId()));
        }
        return persistencePort.save(entity);
    }

    @Override
    public IOutfit getById(Long id) {
        return persistencePort.findById(id)
                .orElseThrow(() -> new OutfitNotFoundException(String.format("The outfit with id %s, was not found!", id)));
    }

    @Override
    public List<IOutfit> getAll() {
        return persistencePort.findAll();
    }

    @Override
    public IOutfit update(Long id, IOutfit newInfo) {

        if(!persistencePort.existsById(id)){
            throw new OutfitNotFoundException(String.format("The outfit with id %s, was not found!", id));
        }

        if(!id.equals(newInfo.getId())){
            throw new BusinessException("The outfit id an the new outfit id are different!");
        }

        return save(newInfo);
    }

    @Override
    public void deleteById(Long id) {
        if(!persistencePort.existsById(id)){
            throw new OutfitNotFoundException(String.format("The outfit with id %s, was not found!", id));
        }
        persistencePort.deleteById(id);
    }
}
