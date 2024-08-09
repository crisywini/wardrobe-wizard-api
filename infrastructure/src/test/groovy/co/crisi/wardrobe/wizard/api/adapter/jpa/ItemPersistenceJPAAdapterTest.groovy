package co.crisi.wardrobe.wizard.api.adapter.jpa

import spock.lang.Specification

class ItemPersistenceJPAAdapterTest extends Specification {

    def "test"(){
       given:"Test"
        def a = 1

        when: "sum"
        def b = a+a
        then:
        b == 2
    }

}
