package co.crisi.wardrobe.wizard.api.domain.data

import co.crisi.wardrobe.wizard.api.exception.validator.EmptyCollectionException
import co.crisi.wardrobe.wizard.api.exception.validator.NullFieldException
import spock.lang.Specification

class OutfitSpec extends Specification {

    def "Should be able to create an outfit"() {
        given: "Required fields"
        def id = 0
        def items = List.of(getRandomItem())
        def score = 5
        def category = OutfitCategory.CASUAL

        when: "Creates an outfit"

        def outfit = new Outfit(id, items, score, category)

        then: "Should create with issues"

        verifyAll {
            outfit.id == id
            outfit.items == items
            outfit.score == score
            outfit.category == category
        }
    }

    private def getRandomItem() {
        def id = 0
        def name = "Lycra"
        def description = "Black lycra full body"
        def imageUrl = "folder/image.png"
        def color = "Black"
        def size = "L"
        def brand = "Nike"
        def material = "lycra"
        def category = ItemCategory.GYM_WEAR
        def type = ItemType.CLOTHES
        return new Item(id, name, description, imageUrl, color, size, brand, material, category, type)
    }

    def "Should failed when missing id"() {
        given: "Required fields"
        def id = null
        def items = List.of(getRandomItem())
        def score = 5
        def category = OutfitCategory.CASUAL

        when: "Creates an outfit"
        def outfit = new Outfit(id, items, score, category)

        then: "Should throw an exception"
        def exception = thrown(NullFieldException)
        exception.message == "The outfit id should exists!"
    }

    def "Should failed when missing items"() {
        given: "Required fields"
        def id = 0
        def items = null
        def score = 5
        def category = OutfitCategory.CASUAL

        when: "Creates an outfit"
        def outfit = new Outfit(id, items, score, category)

        then: "Should throw an exception"
        def exception = thrown(NullFieldException)
        exception.message == "The outfit items should exists!"
    }

    def "Should failed when empty items"() {
        given: "Required fields"
        def id = 0
        def items = List.of()
        def score = 5
        def category = OutfitCategory.CASUAL

        when: "Creates an outfit"
        def outfit = new Outfit(id, items, score, category)

        then: "Should throw an exception"
        def exception = thrown(EmptyCollectionException)
        exception.message == "The outfit items should not be empty!"
    }

    def "Should failed when missing score"() {
        given: "Required fields"
        def id = 0
        def items = List.of(getRandomItem())
        def score = null
        def category = OutfitCategory.CASUAL

        when: "Creates an outfit"
        def outfit = new Outfit(id, items, score, category)

        then: "Should throw an exception"
        def exception = thrown(NullFieldException)
        exception.message == "The outfit score should exists!"
    }

    def "Should failed when missing category"() {
        given: "Required fields"
        def id = 0
        def items = List.of(getRandomItem())
        def score = 5
        def category = null

        when: "Creates an outfit"
        def outfit = new Outfit(id, items, score, category)

        then: "Should throw an exception"
        def exception = thrown(NullFieldException)
        exception.message == "The outfit category should exists!"
    }

}
