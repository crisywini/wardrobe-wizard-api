package co.crisi.wardrobe.wizard.api.service

import co.crisi.wardrobe.wizard.api.domain.data.Item
import co.crisi.wardrobe.wizard.api.domain.data.ItemCategory
import co.crisi.wardrobe.wizard.api.domain.data.ItemType
import co.crisi.wardrobe.wizard.api.port.spi.IItemPersistencePort
import spock.lang.Specification

class ItemServicePortSpec extends Specification {

    def final persistencePort = Mock(IItemPersistencePort)

    def itemServicePort = new ItemServicePort(persistencePort)

    def "Should be able to save an item"(){
        given: "An Item entity"
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
        def item = new Item(id, name, description, imageUrl, color, size, brand, material, category, type)

        persistencePort.save(item) >> item

        when: "Calling service port"
        def entitySaved = itemServicePort.save(item)

        then: "The item saved is the same sended to saved"
        entitySaved.equals(item)
    }

    def "Should be able to find an entity"(){
        given: "An id of existing item"
        def id = 1L
        def item = getItem()
        persistencePort.findById(id) >> Optional.of(item)

        when: "Calling the get by id service port"
        def entity = itemServicePort.getById(id)

        then: "Should return the entity unwrapped"
        entity.equals(item)
    }

    private def getItem(){
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

    def "Should return all the elements found"(){
        given:"Config for persistence port"
        def items = List.of(getItem(), getItem())
        persistencePort.findAll() >> items

        when: "Call find all method"
        def entities = itemServicePort.getAll()

        then: "The entities should be the same as the items"
        verifyAll {
            items.size() == entities.size()
            items[0].equals(entities[0])
            items[1].equals(entities[1])
        }
    }

    def "Should be able to update an item"(){
        given: "An id of existing item"
        def id = 1L
        and: "A new entity with something changed"
        def newInfo = getItemForUpdate()
        persistencePort.existsById(id) >> true
        persistencePort.save(newInfo) >> newInfo

        when: "Updating an item"
        def updatedEntity = itemServicePort.update(id, newInfo)

        then: "Should be the same entity updated"
        updatedEntity.equals(newInfo)

    }

    private def getItemForUpdate(){
        def id = 1L
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

    def "Should be able to delete and existing by id"(){
        given: "An id of existing item"
        def id = 1L
        persistencePort.existsById(id) >> true

        when: "Delete an existing item"
        itemServicePort.deleteById(id)

        then: "The persistence port should be called"
        1 * persistencePort.deleteById(id)
    }

}
