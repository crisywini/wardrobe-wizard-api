package co.crisi.wardrobe.wizard.api.service;

import co.crisi.wardrobe.wizard.api.domain.IOutfit;
import co.crisi.wardrobe.wizard.api.port.api.IOutfitServicePort;

import java.util.List;

public class ItemServicePort implements IOutfitServicePort {

    
    @Override
    public IOutfit save(IOutfit entity) {
        return null;
    }

    @Override
    public IOutfit getById(Long aLong) {
        return null;
    }

    @Override
    public List<IOutfit> getAll() {
        return List.of();
    }

    @Override
    public IOutfit update(Long aLong, IOutfit newInfo) {
        return null;
    }

    @Override
    public void deleteById(Long aLong) {

    }
}
