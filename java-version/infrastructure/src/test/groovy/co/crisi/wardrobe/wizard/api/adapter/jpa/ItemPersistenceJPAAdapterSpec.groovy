package co.crisi.wardrobe.wizard.api.adapter.jpa

import co.crisi.wardrobe.wizard.api.domain.IItem
import co.crisi.wardrobe.wizard.api.domain.data.Item
import co.crisi.wardrobe.wizard.api.domain.data.ItemCategory
import co.crisi.wardrobe.wizard.api.domain.data.ItemType
import co.crisi.wardrobe.wizard.api.repository.jpa.ItemJpaRepository
import org.junit.Ignore
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.boot.test.autoconfigure.orm.jpa.DataJpaTest
import org.springframework.boot.test.context.SpringBootTest
import org.springframework.test.context.DynamicPropertyRegistry
import org.springframework.test.context.DynamicPropertySource
import org.testcontainers.containers.PostgreSQLContainer
import spock.lang.Shared
import spock.lang.Specification


@SpringBootTest
class ItemPersistenceJPAAdapterSpec extends Specification {

    @Shared
    static container = new PostgreSQLContainer<>("pgvector/pgvector:pg16")

    @DynamicPropertySource
    static void registerPgProperties(DynamicPropertyRegistry registry) {
        container
                .withDatabaseName("wizard-api")
                .withUsername("postgresql")
                .withPassword("1234")
                .start()

        registry.add("spring.datasource.url", container::getJdbcUrl)
        registry.add("spring.datasource.username", container::getUsername)
        registry.add("spring.datasource.password", container::getPassword)
    }

    def setupSpec() {
        container
                .withDatabaseName("wizard-api")
                .withUsername("postgresql")
                .withPassword("1234")
                .start()
    }

    @Autowired(required = true)
    private ItemJpaRepository itemJpaRepository

    def itemPersistenceJPAAdapter = new ItemPersistenceJPAAdapter(itemJpaRepository)


    def cleanup() {
        itemJpaRepository.deleteAll()
    }

    def "when context is loaded then all expected beans are created"() {
        expect: "the itemJpaRepository is created"
        itemJpaRepository
    }

    @Ignore
    def "test save and find by id"() {
        given: "an item to save"
        IItem item = getRandomItem()

        when: "saving the item"
        def savedItem = itemPersistenceJPAAdapter.save(item)

        then: "the item is successfully saved and can be retrieved by ID"
        def foundItem = itemPersistenceJPAAdapter.findById(savedItem.getId())
        foundItem.isPresent()
        foundItem.get().name == "Lycra"
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

}
