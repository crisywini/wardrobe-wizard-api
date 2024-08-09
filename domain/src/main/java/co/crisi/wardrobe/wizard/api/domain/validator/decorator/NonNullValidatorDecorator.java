package co.crisi.wardrobe.wizard.api.domain.validator.decorator;

import co.crisi.wardrobe.wizard.api.exception.validator.NullFieldException;
import co.crisi.wardrobe.wizard.api.domain.validator.IValidator;

import java.util.Optional;

public class NonNullValidatorDecorator extends ValidatorDecorator{

    public NonNullValidatorDecorator(IValidator objectValidator){
        super(objectValidator);
    }

    @Override
    public <T> T validate(T object, String fieldName) {
        var validate = this.objectValidator.validate(object, fieldName);
        var errorMessage = "The %s should exists!";
        return Optional.ofNullable(validate)
                .orElseThrow(() -> new NullFieldException(String
                        .format(errorMessage, fieldName)));
    }

}
