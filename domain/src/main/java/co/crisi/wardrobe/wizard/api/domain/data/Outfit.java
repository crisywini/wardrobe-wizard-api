package co.crisi.wardrobe.wizard.api.domain.data;

import co.crisi.wardrobe.wizard.api.domain.IItem;
import co.crisi.wardrobe.wizard.api.domain.IOutfit;
import co.crisi.wardrobe.wizard.api.domain.validator.decorator.NonNullValidatorDecorator;
import co.crisi.wardrobe.wizard.api.domain.validator.decorator.NotEmptyValidatorDecorator;
import co.crisi.wardrobe.wizard.api.domain.validator.decorator.Validator;

import java.util.List;

public record Outfit(Long id, List<IItem> items, Long score, String category) implements IOutfit {

    public Outfit(Long id, List<IItem> items, Long score, String category){
        var validator = new Validator();
        var nonNullValidator = new NonNullValidatorDecorator(validator);
        var notEmptyValidator = new NotEmptyValidatorDecorator(nonNullValidator);

        this.id = nonNullValidator.validate(id, "outfit id");
        this.items = notEmptyValidator.validate(items, "outfit items");
        this.score = nonNullValidator.validate(score, "outfit score");
        this.category = nonNullValidator.validate(category, "outfit category");
    }

    @Override
    public List<IItem> getItems() {
        return items;
    }

    @Override
    public Long getScore() {
        return score;
    }

    @Override
    public String getCategory() {
        return category;
    }

    @Override
    public Long getId() {
        return id;
    }
}
