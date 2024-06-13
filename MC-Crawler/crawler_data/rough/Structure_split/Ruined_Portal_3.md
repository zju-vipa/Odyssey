## Data values
### ID
Java Edition:

| Structure type | Identifier      |
|----------------|-----------------|
| Ruined Portal  | `ruined_portal` |

| Structure              | Identifier               |
|------------------------|--------------------------|
| Ruined Portal          | `ruined_portal`          |
| Desert Ruined Portal   | `ruined_portal_desert`   |
| Jungle Ruined Portal   | `ruined_portal_jungle`   |
| Mountain Ruined Portal | `ruined_portal_mountain` |
| Nether Ruined Portal   | `ruined_portal_nether`   |
| Ocean Ruined Portal    | `ruined_portal_ocean`    |
| Swamp Ruined Portal    | `ruined_portal_swamp`    |

Bedrock Edition:

| Structure     | Identifier      | Alias ID       | Translation key         |
|---------------|-----------------|----------------|-------------------------|
| Ruined Portal | `ruined_portal` | `ruinedportal` | `feature.ruined_portal` |

### Config
Java Edition:

- Structure configuration
	- type:minecraft:ruined_portal
	- 
	- Fields common to all structures
	- setups: (Cannot be empty) A list of ruined portal setups to randomly choose one from it.
		- weight: The weight this ruined portal setup is chosen.
		- placement: Eitheron_land_surface,partly_buried,on_ocean_floor,in_mountain,underground,in_nether. Determines how the ruined portal is placed.
		- air_pocket_probability: The probability that the ruined portal generates an air pocket around it. Value between 0.0 and 1.0 (inclusive).
		- mossiness: Determines how mossy the ruined portal is, as an argument forminecraft:block_ageprocessor. Value between 0.0 and 1.0 (inclusive).
		- overgrown: Determines whether or not jungle leaves generate.
		- vines: Determines whether or not vines generate on the ruined portal.
		- can_be_cold: Determines whether or not lava and magma can be replaced with netherrack.
		- replace_with_blackstone: Determines whether or not stone bricks in the ruined portal are replaced with their blackstone equivalents.


