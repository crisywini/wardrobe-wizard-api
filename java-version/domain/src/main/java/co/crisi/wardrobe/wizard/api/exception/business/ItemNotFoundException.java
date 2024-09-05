package co.crisi.wardrobe.wizard.api.exception.business;

public class ItemNotFoundException extends BusinessException{
    public ItemNotFoundException(String errorMessage) {
        super(errorMessage);
    }
}
