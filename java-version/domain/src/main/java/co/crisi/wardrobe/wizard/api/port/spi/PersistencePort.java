package co.crisi.wardrobe.wizard.api.port.spi;

import java.util.List;
import java.util.Optional;

public interface PersistencePort <T, ID>{

    T save(T entity);

    Optional<T> findById(ID id);

    List<T> findAll();

    void deleteById(ID id);

    boolean existsById(ID id);


}
