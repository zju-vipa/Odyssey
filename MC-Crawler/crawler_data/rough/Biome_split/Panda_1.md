### Breeding
The panda is the only animal to have extra breeding conditions. In Java Edition, pandas enter love mode when fed with bamboo, but breed only if there is at least one bamboo block (not including shoots) within a 7×7×3 area; otherwise the pandas briefly shake their heads and do not breed until that requirement is met. If only one panda is close to a bamboo block, the other panda shakes its head, but a baby is born.

In Bedrock Edition, there must be at least 8 bamboo blocks within a five-block radius of each panda in order for them to enter love mode. If a panda is fed without a sufficient amount of bamboo nearby, it sits and eats the bamboo instead of entering love mode.

Once pandas successfully breed, they produce a panda cub that remains neutral toward that player.

## Genetics
Each panda has two hidden values called "genes" or "alleles", as found in genetics. Pandas have a main gene and a hidden gene, each assigned to a particular trait. Normal, aggressive, lazy, worried, and playful personalities are dominant traits, while weak and brown personalities are recessive traits. If the main gene is a dominant gene, then it presents as the personality regardless of the hidden gene. If the main gene is recessive and the hidden gene is not the same trait, then a normal personality results. As recessive traits, weak and brown personalities occur if both the main and hidden genes of a panda are weak or brown, respectively. The hidden gene is relevant only for determining the panda's personality if the main gene is recessive.

When two pandas breed, each one passes one of their genes to their children, who then randomly mix both obtained genes as their respective main and hidden genes. There is also a 1⁄32 chance for each gene of the baby to mutate into another gene. Normal, weak, and brown traits more commonly result from mutations than other traits do. These probabilities also apply to naturally spawned pandas for their main and hidden genes.

| Mutated Gene | Probability    |
|--------------|----------------|
| Normal       | $\frac{5}{16}$ |
| Aggressive   | $\frac{1}{16}$ |
| Lazy         | $\frac{1}{16}$ |
| Worried      | $\frac{1}{16}$ |
| Playful      | $\frac{1}{16}$ |
| Weak         | $\frac{5}{16}$ |
| Brown        | $\frac{1}{8}$  |

| Panda Personality |            | Hidden Gene |            |            |            |            |            |            |
|-------------------|------------|-------------|------------|------------|------------|------------|------------|------------|
|                   |            | Normal      | Aggressive | Lazy       | Worried    | Playful    | Weak       | Brown      |
| Main Gene         | Normal     | Normal      | Normal     | Normal     | Normal     | Normal     | Normal     | Normal     |
|                   | Aggressive | Aggressive  | Aggressive | Aggressive | Aggressive | Aggressive | Aggressive | Aggressive |
|                   | Lazy       | Lazy        | Lazy       | Lazy       | Lazy       | Lazy       | Lazy       | Lazy       |
|                   | Worried    | Worried     | Worried    | Worried    | Worried    | Worried    | Worried    | Worried    |
|                   | Playful    | Playful     | Playful    | Playful    | Playful    | Playful    | Playful    | Playful    |
|                   | Weak       | Normal      | Normal     | Normal     | Normal     | Normal     | Weak       | Normal     |
|                   | Brown      | Normal      | Normal     | Normal     | Normal     | Normal     | Normal     | Brown      |

The only way to directly observe the hidden gene of a panda (if they are not weak or brown, in which case the genes are certain) is to use the command :/data get entity @e[type=minecraft:panda,limit=1] HiddenGene‌[Java Edition  only]or using third-party NBT editors.
## Data values
### ID
Java Edition:

| Name  | Identifier | Translation key          |
|-------|------------|--------------------------|
| Panda | `panda`    | `entity.minecraft.panda` |

Bedrock Edition:

| Name  | Identifier | Numeric ID | Translation key     |
|-------|------------|------------|---------------------|
| Panda | `panda`    | `113`      | `entity.panda.name` |

### Entity data
Panda have entity data associated with them that contains various properties.

Java Edition:

Main article: Entity format
- Entity data
	- 
	- Additional fields for mobs that can breed
	- 
	- Tags common to all entities
	- 
	- Tags common to all mobs
	- HiddenGene: The secondary gene this panda has, that can transfer to the child.
	- MainGene: The primary gene this panda has, that determines the behavior and appearance of the panda and that can transfer to the child.


Genes
Main article: Panda/DV[edit]

Bedrock Edition:

SeeBedrock Edition level format/Entity format.

