package co.crisi.wardrobe.wizard.api.exception.validator;

public class ValidationException extends RuntimeException{


    public ValidationException(String errorMessage){
        super(errorMessage);
    }
}
