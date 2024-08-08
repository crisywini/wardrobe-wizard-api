package co.crisi.wardrobe.wizard.api.domain.validator.decorator;

import co.crisi.wardrobe.wizard.api.domain.validator.IValidator;
import co.crisi.wardrobe.wizard.api.exception.validator.EmptyCollectionException;
import lombok.AllArgsConstructor;

import java.util.List;
import java.util.Optional;


@AllArgsConstructor
public class ValidatorDecorator implements IValidator {

    protected IValidator objectValidator;

    @Override
    public <T> T validate(T object, String fieldName) {
        var validate = this.objectValidator.validate(object, fieldName);
        var errorMessage = "The %s, should not be empty!";

        if (validate instanceof List<?> validatedList) {
            return (T) Optional.ofNullable(validatedList)
                    .filter(l -> !l.isEmpty())
                    .orElseThrow(() -> new EmptyCollectionException(String.format(errorMessage, fieldName)));

        } else {
            throw new IllegalArgumentException("The validation result is not a List.");
        }

    }
}
