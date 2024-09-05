package co.crisi.wardrobe.wizard.api.entity;


import co.crisi.wardrobe.wizard.api.domain.IItem;
import co.crisi.wardrobe.wizard.api.domain.data.ItemCategory;
import co.crisi.wardrobe.wizard.api.domain.data.ItemType;
import jakarta.persistence.*;
import lombok.AllArgsConstructor;
import lombok.Getter;
import lombok.NoArgsConstructor;
import lombok.Setter;

@Entity
@Table(name = "item")
@Getter
@Setter
@AllArgsConstructor
@NoArgsConstructor
public class ItemJPAEntity implements IItem {

    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    private Long id;

    private String name;

    private String description;

    @Column(name = "image_url")
    private String imageUrl;

    private String color;

    private String size;

    private String brand;

    private String material;

    @Enumerated(EnumType.STRING)
    private ItemCategory category;

    @Enumerated(EnumType.STRING)
    private ItemType type;


}
