package co.crisi.wardrobe.wizard.api.exception.business;

public class OutfitNotFoundException extends BusinessException{
    public OutfitNotFoundException(String errorMessage) {
        super(errorMessage);
    }
}
