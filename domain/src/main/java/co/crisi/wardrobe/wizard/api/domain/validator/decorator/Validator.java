package co.crisi.wardrobe.wizard.api.domain.validator.decorator;

import co.crisi.wardrobe.wizard.api.domain.validator.IValidator;

public class Validator implements IValidator {

    @Override
    public <T> T validate(T object, String fieldName) {
        return object;
    }
}
