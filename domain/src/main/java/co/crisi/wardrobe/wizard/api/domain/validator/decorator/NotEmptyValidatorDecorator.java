package co.crisi.wardrobe.wizard.api.domain.validator.decorator;

import co.crisi.wardrobe.wizard.api.domain.validator.IValidator;

public class NotEmptyValidatorDecorator extends ValidatorDecorator {

    public NotEmptyValidatorDecorator(IValidator validator){
        super(validator);
    }

    @Override
    public <T> T validate(T object, String fieldName) {
        return null;
    }
}
