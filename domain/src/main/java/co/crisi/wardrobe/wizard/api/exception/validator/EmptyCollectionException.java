package co.crisi.wardrobe.wizard.api.exception.validator;

public class EmptyCollectionException extends ValidationException{

    public EmptyCollectionException(String errorMessage) {
        super(errorMessage);
    }
}
