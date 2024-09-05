package co.crisi.wardrobe.wizard.api.domain.validator;

public interface IValidator {

    <T extends Object> T validate(T object, String fieldName);

}
