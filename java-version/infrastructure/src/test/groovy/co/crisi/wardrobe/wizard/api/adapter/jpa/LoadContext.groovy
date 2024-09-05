package co.crisi.wardrobe.wizard.api.adapter.jpa

import co.crisi.wardrobe.wizard.api.repository.jpa.ItemJpaRepository
import org.springframework.beans.factory.annotation.Autowired
import org.springframework.boot.test.context.SpringBootTest
import spock.lang.Specification
import co.crisi.wardrobe.wizard.api.WardrobeWizardApiApplication


@SpringBootTest(classes = WardrobeWizardApiApplication)
class LoadContext extends Specification {

    @Autowired
    private ItemJpaRepository itemJpaRepository

    def "context loads"() {
        expect:
        itemJpaRepository != null
    }


}
