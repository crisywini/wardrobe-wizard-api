package co.crisi.wardrobe.wizard.api.domain.validator.decorator;

import co.crisi.wardrobe.wizard.api.domain.validator.IValidator;
import lombok.AllArgsConstructor;



@AllArgsConstructor
public class ValidatorDecorator implements IValidator {

    protected IValidator objectValidator;

    @Override
    public <T> T validate(T object, String fieldName) {
        return objectValidator.validate(object, fieldName);
    }
}
