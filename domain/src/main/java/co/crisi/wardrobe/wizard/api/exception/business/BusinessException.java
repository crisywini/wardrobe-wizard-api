package co.crisi.wardrobe.wizard.api.exception.business;

public class BusinessException extends RuntimeException {
    public BusinessException(String errorMessage) {
        super(errorMessage);
    }
}
