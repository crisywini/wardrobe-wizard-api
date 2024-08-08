package co.crisi.wardrobe.wizard.api.exception.validator;

public class NullFieldException extends ValidationException {

    public NullFieldException(String errorMessage) {
        super(errorMessage);
    }
}
