## Data values
### ID
Java Edition:

| Name                    | Identifier             | Form | Item tags | Translation key                       |
|-------------------------|------------------------|------|-----------|---------------------------------------|
| Bucket of Tropical Fish | `tropical_fish_bucket` | Item | None      | `item.minecraft.tropical_fish_bucket` |

Bedrock Edition:

| Name                    | Identifier             | Alias ID     | Numeric ID | Form | Translation key                                             |
|-------------------------|------------------------|--------------|------------|------|-------------------------------------------------------------|
| Bucket of Tropical Fish | `tropical_fish_bucket` | `bucket / 4` | `366`      | Item | `item.bucketTropical.name`<br/>`item.bucketCustomFish.name` |

### Item data
Java Edition:

Main article: Item format
- tag: The item'stagtag.

- 
	- BucketVariantTag: Thevariant dataof the tropical fish in the bucket. Applies only to Bucket of Tropical Fish.
	- EntityTag: Stores entity data that is applied to the aquatic mob when it is poured out. If this data includes a tropical fish variant, it overrides the one provided inBucketVariantTag.
		- Seeentity format.

Normal buckets of fish use only the BucketVariantTag tag to store the variant of any tropical fish that is picked up, and the item's display name to store the fish's custom name.

Bedrock Edition:

SeeBedrock Edition level format/Item format.

