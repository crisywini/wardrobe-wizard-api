package co.crisi.wardrobe.wizard.api.domain

import co.crisi.wardrobe.wizard.api.domain.data.Item
import co.crisi.wardrobe.wizard.api.domain.data.ItemCategory
import co.crisi.wardrobe.wizard.api.domain.data.ItemType
import co.crisi.wardrobe.wizard.api.exception.validator.NullFieldException
import spock.lang.Specification

class ItemSpec extends Specification {

    def "Should be able to create an item"() {
        given: "The fields needed to create an item"
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

        when: "Creates an item"
        def item = new Item(id, name, description, imageUrl, color, size, brand, material, category, type)

        then: "It should be able to create the item and all elements are correctly assign"

        verifyAll {
            item.id == id
            item.name == name
            item.description == description
            item.imageUrl == imageUrl
            item.color == color
            item.size == size
            item.brand == brand
            item.material == material
            item.category == category
            item.type == type
        }

    }


    def "Should failed when missing id"() {
        given: "The fields needed to create an item"
        def id = null
        def name = "Lycra"
        def description = "Black lycra full body"
        def imageUrl = "folder/image.png"
        def color = "Black"
        def size = "L"
        def brand = "Nike"
        def material = "lycra"
        def category = ItemCategory.GYM_WEAR
        def type = ItemType.CLOTHES

        when: "Creates an item"
        def item = new Item(id, name, description, imageUrl, color, size, brand, material, category, type)

        then: "It should throw an exception"

        def exception = thrown(NullFieldException)
        exception.message == "The item id should exists!"
    }

    def "Should failed when missing name"() {
        given: "The fields needed to create an item"
        def id = 0
        def name = null
        def description = "Black lycra full body"
        def imageUrl = "folder/image.png"
        def color = "Black"
        def size = "L"
        def brand = "Nike"
        def material = "lycra"
        def category = ItemCategory.GYM_WEAR
        def type = ItemType.CLOTHES

        when: "Creates an item"
        def item = new Item(id, name, description, imageUrl, color, size, brand, material, category, type)

        then: "It should throw an exception"

        def exception = thrown(NullFieldException)
        exception.message == "The item name should exists!"
    }

    def "Should failed when missing description"() {
        given: "The fields needed to create an item"
        def id = 0
        def name = "Lycra"
        def description = null
        def imageUrl = "folder/image.png"
        def color = "Black"
        def size = "L"
        def brand = "Nike"
        def material = "lycra"
        def category = ItemCategory.GYM_WEAR
        def type = ItemType.CLOTHES

        when: "Creates an item"
        def item = new Item(id, name, description, imageUrl, color, size, brand, material, category, type)

        then: "It should throw an exception"

        def exception = thrown(NullFieldException)
        exception.message == "The item description should exists!"
    }

    def "Should failed when missing imageUrl"() {
        given: "The fields needed to create an item"
        def id = 0
        def name = "Lycra"
        def description =  "Black lycra full body"
        def imageUrl = null
        def color = "Black"
        def size = "L"
        def brand = "Nike"
        def material = "lycra"
        def category = ItemCategory.GYM_WEAR
        def type = ItemType.CLOTHES

        when: "Creates an item"
        def item = new Item(id, name, description, imageUrl, color, size, brand, material, category, type)

        then: "It should throw an exception"

        def exception = thrown(NullFieldException)
        exception.message == "The item image url should exists!"
    }

    def "Should failed when missing color"() {
        given: "The fields needed to create an item"
        def id = 0
        def name = "Lycra"
        def description =  "Black lycra full body"
        def imageUrl = "folder/image.png"
        def color = null
        def size = "L"
        def brand = "Nike"
        def material = "lycra"
        def category = ItemCategory.GYM_WEAR
        def type = ItemType.CLOTHES

        when: "Creates an item"
        def item = new Item(id, name, description, imageUrl, color, size, brand, material, category, type)

        then: "It should throw an exception"

        def exception = thrown(NullFieldException)
        exception.message == "The item color should exists!"
    }

    def "Should failed when missing size"() {
        given: "The fields needed to create an item"
        def id = 0
        def name = "Lycra"
        def description =  "Black lycra full body"
        def imageUrl = "folder/image.png"
        def color = "Black"
        def size = null
        def brand = "Nike"
        def material = "lycra"
        def category = ItemCategory.GYM_WEAR
        def type = ItemType.CLOTHES

        when: "Creates an item"
        def item = new Item(id, name, description, imageUrl, color, size, brand, material, category, type)

        then: "It should throw an exception"

        def exception = thrown(NullFieldException)
        exception.message == "The item size should exists!"
    }

    def "Should failed when missing brand"() {
        given: "The fields needed to create an item"
        def id = 0
        def name = "Lycra"
        def description =  "Black lycra full body"
        def imageUrl = "folder/image.png"
        def color = "Black"
        def size = "L"
        def brand = null
        def material = "lycra"
        def category = ItemCategory.GYM_WEAR
        def type = ItemType.CLOTHES

        when: "Creates an item"
        def item = new Item(id, name, description, imageUrl, color, size, brand, material, category, type)

        then: "It should throw an exception"

        def exception = thrown(NullFieldException)
        exception.message == "The item brand should exists!"
    }

    def "Should failed when missing material"() {
        given: "The fields needed to create an item"
        def id = 0
        def name = "Lycra"
        def description =  "Black lycra full body"
        def imageUrl = "folder/image.png"
        def color = "Black"
        def size = "L"
        def brand = "Nike"
        def material = null
        def category = ItemCategory.GYM_WEAR
        def type = ItemType.CLOTHES

        when: "Creates an item"
        def item = new Item(id, name, description, imageUrl, color, size, brand, material, category, type)

        then: "It should throw an exception"

        def exception = thrown(NullFieldException)
        exception.message == "The item material should exists!"
    }

    def "Should failed when missing category"() {
        given: "The fields needed to create an item"
        def id = 0
        def name = "Lycra"
        def description =  "Black lycra full body"
        def imageUrl = "folder/image.png"
        def color = "Black"
        def size = "L"
        def brand = "Nike"
        def material = "lycra"
        def category = null
        def type = ItemType.CLOTHES

        when: "Creates an item"
        def item = new Item(id, name, description, imageUrl, color, size, brand, material, category, type)

        then: "It should throw an exception"

        def exception = thrown(NullFieldException)
        exception.message == "The item category should exists!"
    }

    def "Should failed when missing type"() {
        given: "The fields needed to create an item"
        def id = 0
        def name = "Lycra"
        def description =  "Black lycra full body"
        def imageUrl = "folder/image.png"
        def color = "Black"
        def size = "L"
        def brand = "Nike"
        def material = "lycra"
        def category = ItemCategory.GYM_WEAR
        def type = null

        when: "Creates an item"
        def item = new Item(id, name, description, imageUrl, color, size, brand, material, category, type)

        then: "It should throw an exception"

        def exception = thrown(NullFieldException)
        exception.message == "The item type should exists!"
    }

}
