#### Expanded default settings

This file contains the same settings used to produce a default world, but with all of the presets expanded to their default values. Note that there is a bug that makes it impossible to create the ender dragon fight without using the dimension type preset minecraft:the_end, as the flag that creates the fight is hardcoded and not accessible through JSON. However, it is otherwise identical to the default world.

Collapsed JSON content
{
  "bonus_chest": false,
  "dimensions": {
    "minecraft:overworld": {
      "type": {
		"logical_height": 256,
		"infiniburn": "minecraft:infiniburn_overworld",
		"effects": "minecraft:overworld",
		"ambient_light": 0.0,
		"respawn_anchor_works": false,
		"has_raids": true,
		"min_y": 0,
		"height": 256,
		"natural": true,
		"coordinate_scale": 1.0,
		"piglin_safe": false,
		"bed_works": true,
		"has_skylight": true,
		"has_ceiling": false,
		"ultrawarm": false
      },
      "generator": {
        "biome_source": {
          "seed": 0,
          "large_biomes": false,
          "type": "minecraft:vanilla_layered"
        },
        "seed": 0,
        "settings": {
		  "noise_caves_enabled": false,
		  "deepslate_enabled": false,
		  "ore_veins_enabled": false,
		  "noodle_caves_enabled": false,
		  "min_surface_level": 0,
		  "disable_mob_generation": false,
		  "aquifers_enabled": false,
		  "default_fluid": {
			"Properties": {
			  "level": "0"
			},
			"Name": "minecraft:water"
		  },
		  "bedrock_roof_position": -2147483648,
		  "bedrock_floor_position": 0,
		  "sea_level": 63,
		  "structures": {
			"stronghold": {
			  "distance": 32,
			  "spread": 3,
			  "count": 128
			},
			"structures": {
			  "minecraft:pillager_outpost": {
				"spacing": 32,
				"separation": 8,
				"salt": 165745296
			  },
			  "minecraft:village": {
				"spacing": 32,
				"separation": 8,
				"salt": 10387312
			  },
			  "minecraft:fortress": {
				"spacing": 27,
				"separation": 4,
				"salt": 30084232
			  },
			  "minecraft:desert_pyramid": {
				"spacing": 32,
				"separation": 8,
				"salt": 14357617
			  },
			  "minecraft:bastion_remnant": {
				"spacing": 27,
				"separation": 4,
				"salt": 30084232
			  },
			  "minecraft:stronghold": {
				"spacing": 1,
				"separation": 0,
				"salt": 0
			  },
			  "minecraft:monument": {
				"spacing": 32,
				"separation": 5,
				"salt": 10387313
			  },
			  "minecraft:swamp_hut": {
				"spacing": 32,
				"separation": 8,
				"salt": 14357620
			  },
			  "minecraft:endcity": {
				"spacing": 20,
				"separation": 11,
				"salt": 10387313
			  },
			  "minecraft:mineshaft": {
				"spacing": 1,
				"separation": 0,
				"salt": 0
			  },
			  "minecraft:igloo": {
				"spacing": 32,
				"separation": 8,
				"salt": 14357618
			  },
			  "minecraft:mansion": {
				"spacing": 80,
				"separation": 20,
				"salt": 10387319
			  },
			  "minecraft:buried_treasure": {
				"spacing": 1,
				"separation": 0,
				"salt": 0
			  },
			  "minecraft:ocean_ruin": {
				"spacing": 20,
				"separation": 8,
				"salt": 14357621
			  },
			  "minecraft:jungle_pyramid": {
				"spacing": 32,
				"separation": 8,
				"salt": 14357619
			  },
			  "minecraft:ruined_portal": {
				"spacing": 40,
				"separation": 15,
				"salt": 34222645
			  },
			  "minecraft:shipwreck": {
				"spacing": 24,
				"separation": 4,
				"salt": 165745295
			  },
			  "minecraft:nether_fossil": {
				"spacing": 2,
				"separation": 1,
				"salt": 14357921
			  }
			}
		  },
		  "noise": {
			"simplex_surface_noise": true,
			"random_density_offset": true,
			"size_vertical": 2,
			"density_factor": 1.0,
			"density_offset": -0.46875,
			"top_slide": {
			  "target": -10,
			  "size": 3,
			  "offset": 0
			},
			"bottom_slide": {
			  "target": 15,
			  "size": 3,
			  "offset": 0
			},
			"size_horizontal": 1,
			"min_y": 0,
			"height": 256,
			"sampling": {
			  "xz_scale": 0.9999999814507745,
			  "y_scale": 0.9999999814507745,
			  "xz_factor": 80.0,
			  "y_factor": 160.0
			}
		  },
		  "default_block": {
			"Name": "minecraft:stone"
		  }
		},
        "type": "minecraft:noise"
      }
    },
    "minecraft:the_nether": {
      "type": {
		"logical_height": 128,
		"infiniburn": "minecraft:infiniburn_nether",
		"effects": "minecraft:the_nether",
		"ambient_light": 0.1,
		"respawn_anchor_works": true,
		"has_raids": false,
		"min_y": 0,
		"height": 256,
		"natural": false,
		"coordinate_scale": 8.0,
		"piglin_safe": true,
		"bed_works": false,
		"fixed_time": 18000,
		"has_skylight": false,
		"has_ceiling": true,
		"ultrawarm": true
	  },
	  "generator": {
		"biome_source": {
		  "humidity_noise": {
			"firstOctave": -7,
			"amplitudes": [
			  1.0,
			  1.0
			]
		  },
		  "altitude_noise": {
			"firstOctave": -7,
			"amplitudes": [
			  1.0,
			  1.0
			]
		  },
		  "weirdness_noise": {
			"firstOctave": -7,
			"amplitudes": [
			  1.0,
			  1.0
			]
		  },
		  "seed": 0,
		  "biomes": [
			{
			  "parameters": {
				"altitude": 0.0,
				"weirdness": 0.0,
				"offset": 0.0,
				"temperature": 0.0,
				"humidity": 0.0
			  },
			  "biome": "minecraft:nether_wastes"
			},
			{
			  "parameters": {
				"altitude": 0.0,
				"weirdness": 0.0,
				"offset": 0.0,
				"temperature": 0.0,
				"humidity": -0.5
			  },
			  "biome": "minecraft:soul_sand_valley"
			},
			{
			  "parameters": {
				"altitude": 0.0,
				"weirdness": 0.0,
				"offset": 0.0,
				"temperature": 0.4,
				"humidity": 0.0
			  },
			  "biome": "minecraft:crimson_forest"
			},
			{
			  "parameters": {
				"altitude": 0.0,
				"weirdness": 0.0,
				"offset": 0.375,
				"temperature": 0.0,
				"humidity": 0.5
			  },
			  "biome": "minecraft:warped_forest"
			},
			{
			  "parameters": {
				"altitude": 0.0,
				"weirdness": 0.0,
				"offset": 0.175,
				"temperature": -0.5,
				"humidity": 0.0
			  },
			  "biome": "minecraft:basalt_deltas"
			}
		  ],
		  "temperature_noise": {
			"firstOctave": -7,
			"amplitudes": [
			  1.0,
			  1.0
			]
		  },
		  "type": "minecraft:multi_noise"
		},
        "seed": 0,
        "settings": {
		  "noise_caves_enabled": false,
		  "deepslate_enabled": false,
		  "ore_veins_enabled": false,
		  "noodle_caves_enabled": false,
		  "min_surface_level": 0,
		  "disable_mob_generation": false,
		  "aquifers_enabled": false,
		  "bedrock_roof_position": 0,
		  "bedrock_floor_position": 0,
		  "sea_level": 32,
		  "structures": {
			"structures": {
			  "minecraft:pillager_outpost": {
				"spacing": 32,
				"separation": 8,
				"salt": 165745296
			  },
			  "minecraft:village": {
				"spacing": 32,
				"separation": 8,
				"salt": 10387312
			  },
			  "minecraft:fortress": {
				"spacing": 27,
				"separation": 4,
				"salt": 30084232
			  },
			  "minecraft:desert_pyramid": {
				"spacing": 32,
				"separation": 8,
				"salt": 14357617
			  },
			  "minecraft:bastion_remnant": {
				"spacing": 27,
				"separation": 4,
				"salt": 30084232
			  },
			  "minecraft:stronghold": {
				"spacing": 1,
				"separation": 0,
				"salt": 0
			  },
			  "minecraft:monument": {
				"spacing": 32,
				"separation": 5,
				"salt": 10387313
			  },
			  "minecraft:swamp_hut": {
				"spacing": 32,
				"separation": 8,
				"salt": 14357620
			  },
			  "minecraft:endcity": {
				"spacing": 20,
				"separation": 11,
				"salt": 10387313
			  },
			  "minecraft:mineshaft": {
				"spacing": 1,
				"separation": 0,
				"salt": 0
			  },
			  "minecraft:igloo": {
				"spacing": 32,
				"separation": 8,
				"salt": 14357618
			  },
			  "minecraft:mansion": {
				"spacing": 80,
				"separation": 20,
				"salt": 10387319
			  },
			  "minecraft:buried_treasure": {
				"spacing": 1,
				"separation": 0,
				"salt": 0
			  },
			  "minecraft:ocean_ruin": {
				"spacing": 20,
				"separation": 8,
				"salt": 14357621
			  },
			  "minecraft:jungle_pyramid": {
				"spacing": 32,
				"separation": 8,
				"salt": 14357619
			  },
			  "minecraft:ruined_portal": {
				"spacing": 25,
				"separation": 10,
				"salt": 34222645
			  },
			  "minecraft:shipwreck": {
				"spacing": 24,
				"separation": 4,
				"salt": 165745295
			  },
			  "minecraft:nether_fossil": {
				"spacing": 2,
				"separation": 1,
				"salt": 14357921
			  }
			}
		  },
		  "noise": {
			"density_factor": 0.0,
			"density_offset": 0.019921875,
			"simplex_surface_noise": false,
			"bottom_slide": {
			  "target": 320,
			  "size": 4,
			  "offset": -1
			},
			"size_horizontal": 1,
			"size_vertical": 2,
			"height": 128,
			"sampling": {
			  "xz_scale": 1.0,
			  "y_scale": 3.0,
			  "xz_factor": 80.0,
			  "y_factor": 60.0
			},
			"top_slide": {
			  "target": 120,
			  "size": 3,
			  "offset": 0
			}
		  },
		  "default_block": {
			"Name": "minecraft:netherrack"
		  },
		  "default_fluid": {
			"Properties": {
			  "level": "0"
			},
			"Name": "minecraft:lava"
		  }
		},
        "type": "minecraft:noise"
      }
    },
    "minecraft:the_end": {
	  "type": {
		"logical_height": 256,
		"infiniburn": "minecraft:infiniburn_end",
		"effects": "minecraft:the_end",
		"ambient_light": 0.0,
		"respawn_anchor_works": false,
		"has_raids": true,
		"min_y": 0,
		"height": 256,
		"natural": false,
		"coordinate_scale": 1.0,
		"piglin_safe": false,
		"bed_works": false,
		"fixed_time": 6000,
		"has_skylight": false,
		"has_ceiling": false,
		"ultrawarm": false
	  },
      "generator": {
        "biome_source": {
          "seed": 0,
          "type": "minecraft:the_end"
        },
        "seed": 0,
        "settings": {
		  "noise_caves_enabled": false,
		  "deepslate_enabled": false,
		  "ore_veins_enabled": false,
		  "noodle_caves_enabled": false,
		  "min_surface_level": 0,
		  "disable_mob_generation": true,
		  "aquifers_enabled": false,
		  "bedrock_roof_position": -2147483648,
		  "bedrock_floor_position": -2147483648,
		  "sea_level": 0,
		  "structures": {
			"structures": {
			  "minecraft:pillager_outpost": {
				"spacing": 32,
				"separation": 8,
				"salt": 165745296
			  },
			  "minecraft:village": {
				"spacing": 32,
				"separation": 8,
				"salt": 10387312
			  },
			  "minecraft:fortress": {
				"spacing": 27,
				"separation": 4,
				"salt": 30084232
			  },
			  "minecraft:desert_pyramid": {
				"spacing": 32,
				"separation": 8,
				"salt": 14357617
			  },
			  "minecraft:bastion_remnant": {
				"spacing": 27,
				"separation": 4,
				"salt": 30084232
			  },
			  "minecraft:stronghold": {
				"spacing": 1,
				"separation": 0,
				"salt": 0
			  },
			  "minecraft:monument": {
				"spacing": 32,
				"separation": 5,
				"salt": 10387313
			  },
			  "minecraft:swamp_hut": {
				"spacing": 32,
				"separation": 8,
				"salt": 14357620
			  },
			  "minecraft:endcity": {
				"spacing": 20,
				"separation": 11,
				"salt": 10387313
			  },
			  "minecraft:mineshaft": {
				"spacing": 1,
				"separation": 0,
				"salt": 0
			  },
			  "minecraft:igloo": {
				"spacing": 32,
				"separation": 8,
				"salt": 14357618
			  },
			  "minecraft:mansion": {
				"spacing": 80,
				"separation": 20,
				"salt": 10387319
			  },
			  "minecraft:buried_treasure": {
				"spacing": 1,
				"separation": 0,
				"salt": 0
			  },
			  "minecraft:ocean_ruin": {
				"spacing": 20,
				"separation": 8,
				"salt": 14357621
			  },
			  "minecraft:jungle_pyramid": {
				"spacing": 32,
				"separation": 8,
				"salt": 14357619
			  },
			  "minecraft:ruined_portal": {
				"spacing": 40,
				"separation": 15,
				"salt": 34222645
			  },
			  "minecraft:shipwreck": {
				"spacing": 24,
				"separation": 4,
				"salt": 165745295
			  },
			  "minecraft:nether_fossil": {
				"spacing": 2,
				"separation": 1,
				"salt": 14357921
			  }
			}
		  },
		  "noise": {
			"island_noise_override": true,
			"density_factor": 0.0,
			"density_offset": 0.0,
			"simplex_surface_noise": true,
			"bottom_slide": {
			  "target": -30,
			  "size": 7,
			  "offset": 1
			},
			"size_horizontal": 2,
			"size_vertical": 1,
			"height": 128,
			"sampling": {
			  "xz_scale": 2.0,
			  "y_scale": 1.0,
			  "xz_factor": 80.0,
			  "y_factor": 160.0
			},
			"top_slide": {
			  "target": -3000,
			  "size": 64,
			  "offset": -46
			}
		  },
		  "default_block": {
			"Name": "minecraft:end_stone"
		  },
		  "default_fluid": {
			"Name": "minecraft:air"
		  }
		},
        "type": "minecraft:noise"
      }
    }
  },
  "seed": 0,
  "generate_features": true
}



