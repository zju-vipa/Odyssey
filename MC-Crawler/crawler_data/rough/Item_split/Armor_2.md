### Dyeing leather armor
Main article: Dye § Dyeing armor
Leather armor can be dyed by combining it with dye(s) through crafting‌[JE  only] or by using it on a cauldron containing dyed water.‌[BE  only] Using leather armor on a cauldron containing ordinary water removes any dye from it.

Default color HEX code for leather armor is  #A06540.

An interactive widget is being loaded. If this does not work for you, please reload the page or check if JavaScript is enabled.
### Armor trims
A display of all sixteen armor trims and ten colors on netherite armor.
Main article: Smithing § Trimming
Armor can be given trims using an armor trim smithing template, a trim material and any armor piece. Trimmed armor has different patterns and different colors depending on the template and material used.

### Smelting ingredient
| Name        | Ingredients                                         | Smelting recipe |
|-------------|-----------------------------------------------------|-----------------|
| Iron Nugget | Anyiron armoror<br/>Anychainmail armor+<br/>Anyfuel | 0.1             |
| Gold Nugget | Anygolden armor+<br/>Anyfuel                        | 0.1             |

## Mechanics
Whenever a piece of armor absorbs damage for the player, the armor itself is damaged, reducing its durability. After taking enough damage, the armor piece is completely destroyed.

Note that if the damage is absorbed not by the armor itself, but by a protection enchantment of the armor, the armor is not damaged. Enchantments can also reduce the damage that armor normally does not reduce.

### Damage types
The following types of damage are reduced by armor and, consequently, damage the armor itself:

- Direct (melee) attacks frommobsandplayers. This includes theStrengthand theWeaknesseffects and damage-increasing enchantments.
- Getting hit with anarrow, ashulker bulletor a throwntrident. This includes extra damage from enchantments (except shulker bullets).
- Getting hit with afireballfrom aghastorblaze, or afire charge.
- Laser beam of aguardianor anelder guardian.
- Damage fromThornsenchantment, or spikes ofguardiansandelder guardians.
- Touching a damaging block (fire,lava,magma block,cactusorsweet berry bush).
	- This excludes netherite armor which is not damaged by fire-related sources.
- Touching apufferfish.
- Explosions.
- Fireworkswith at least afirework starin the recipe.
- Lightning.
- Getting hit with a fallinganvil.
- Getting hit with asnowballfrom aplayer‌[upcoming: JE Combat Tests]orsnow golem.[more information needed]
- Getting hit with aneggfrom aplayer‌[upcoming: JE Combat Tests][more information needed]

The following types of damage are not reduced by armor and have no effect on the armor itself:

- Ranged sonic attacks fromwardens.
- Fall damage (includingender pearls, butProtectionandFeather Fallingenchantments reduce it).
- Ongoing damage from being onfire.
- Suffocatinginside a block or due toentity cramming(also includes theworld border)‌[JE  only].
- Drowningin water (partially forturtle shells).
- Starvation.
- Colliding with a block while flying withelytra.
- 
- Magic (Evokerfangs,status effectsandinstant damagefrom apotion of HarmingorDragon's Breath) (butProtectiondoes reduce magical damage.)
- Falling into thevoidor/kill.
- Being inside of apowder snowblock.
	- This excludes if the player or mob wears any piece of leather armor.

### Defense points



The armor bar as shown in game


Armor defense points are controlled by an attribute, generic.armor. The player's current protection level is represented visually by the armor bar. The armor meter is affected by the particular pieces that are worn as well as the tier of the armor. The following table shows the number of defense points added by default by each individual piece of armor, as well as the total points added by a full set of armor for each material. 

| Material     | Full set   | Helmet / Cap | Chestplate / Tunic | Leggings / Pants | Boots |
|--------------|------------|--------------|--------------------|------------------|-------|
| Turtle Shell | 2 ()       | 2 ()         | N/A                | N/A              | N/A   |
| Leather      | 7 ()       | 1 ()         | 3 ()               | 2 ()             | 1 ()  |
| Golden       | 11 (× 5.5) | 2 ()         | 5 ()               | 3 ()             | 1 ()  |
| Chainmail    | 12 (× 6)   | 2 ()         | 5 ()               | 4 ()             | 1 ()  |
| Iron         | 15 (× 7.5) | 2 ()         | 6 ()               | 5 ()             | 2 ()  |
| Diamond      | 20 (× 10)  | 3 ()         | 8 ()               | 6 ()             | 3 ()  |
| Netherite    | 20 (× 10)  | 3 ()         | 8 ()               | 6 ()             | 3 ()  |

Different combinations of armor provide different levels of defense.

### Armor toughness
Armor can further protect the player through a second attribute, generic.armor_toughness. Normally, armor nullifies a lesser portion of damage from attacks that deal greater damage.[2] Armor toughness resists this effect, mitigating the power of strong attacks.[3] By default, only diamond and netherite armor provide toughness, with each piece granting +2 toughness for diamond and +3 for netherite.

| Material     | Full set | Helmet / Cap | Chestplate / Tunic | Leggings / Pants | Boots |
|--------------|----------|--------------|--------------------|------------------|-------|
| Turtle Shell | 0 ()     | 0 ()         | N/A                | N/A              | N/A   |
| Leather      | 0 ()     | 0 ()         | 0 ()               | 0 ()             | 0 ()  |
| Golden       | 0 ()     | 0 ()         | 0 ()               | 0 ()             | 0 ()  |
| Chainmail    | 0 ()     | 0 ()         | 0 ()               | 0 ()             | 0 ()  |
| Iron         | 0 ()     | 0 ()         | 0 ()               | 0 ()             | 0 ()  |
| Diamond      | 8 ()     | 2 ()         | 2 ()               | 2 ()             | 2 ()  |
| Netherite    | 12 (× 6) | 3 ()         | 3 ()               | 3 ()             | 3 ()  |

Different combinations of armor provide different levels of armor toughness.

Armor toughness system includes a new formula for calculating damage:

totalDamage=damage×(1−max(defensePoints5,defensePoints−4×damagetoughness+8)25)
### Damage protection
See also: Armor/Old

Damage taken depends on the number of defense points, the toughness of the armor worn and the strength of the attack. 

damage=weapondamage×(1−min⁡(20,max⁡(defensepoints5,defensepoints−4×weapondamagetoughness+8))25)
(Note: the min and max operators mean that only the minimum or maximum output of the two expressions that follow them (separated by commas) is used. for example, "y = min (2x, 16)" means that "y" is equal to the smallest value out of "2x" and "16", while the largest is ignored.)

Broken down, this means that each armor point gives 4% maximum damage reduction against an incoming attack. Without toughness, this max damage reduction is lessened by 2 percentage points for each hit point of the incoming attack. 2 defense points are worth 8% protection, so the total protection that can be achieved with armor is 80%. Diamond and netherite armors protect the player from up to 80% of damage, iron provides up to 60% damage reduction and leather provides up to 28%.

One piece of diamond armor (granting +2 toughness) decreases the defense reduction value for each attack hit point to 1.6%. Two diamond pieces decrease it to 4⁄3% (about 1.3333%), three decrease it to 8⁄7% (about 1.1428%), and four decrease it to 1%. Netherite armor decreases this even further. One piece of netherite armor reduce the defense reduction value for every hit point to 16⁄11 (about 1.4545%), two decrease it to 8⁄7 (about 1.1428%), three decrease to 16⁄17 (about 0.9412%) and four decrease it to 0.8%. The exact formula for the defense reduction in percent is:

defensereductioninpercent=16×damagetoughness+8
Simply put, as toughness increases, the amount of defense reduction done by high-damaging attacks is diminished, and as toughness approaches a high value (through commands), the defense reduction caused by high-damaging attacks becomes negligible. The final damage reduction value of the armor is capped at a minimum of 0.8% damage reduction per armor point, and to a maximum of 80% total. If armor is cheated in so that the min cap is larger than the max cap, the min cap is ignored. An illustration of the armor reduction is given below.

 

In tabular form (with a toughness of 0), damages are:

| Armor | Attack damage |      |      |      |      |      |      |      |      |       |       |       |       |       |       |       |       |       |       |       |
|-------|---------------|------|------|------|------|------|------|------|------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|-------|
|       | 1             | 2    | 3    | 4    | 5    | 6    | 7    | 8    | 9    | 10    | 11    | 12    | 13    | 14    | 15    | 16    | 17    | 18    | 19    | 20    |
| 0     | 1.00          | 2.00 | 3.00 | 4.00 | 5.00 | 6.00 | 7.00 | 8.00 | 9.00 | 10.00 | 11.00 | 12.00 | 13.00 | 14.00 | 15.00 | 16.00 | 17.00 | 18.00 | 19.00 | 20.00 |
| 1     | 0.98          | 1.98 | 2.98 | 3.97 | 4.96 | 5.95 | 6.94 | 7.94 | 8.93 | 9.92  | 10.91 | 11.90 | 12.90 | 13.89 | 14.88 | 15.87 | 16.86 | 17.86 | 18.85 | 19.84 |
| 2     | 0.94          | 1.92 | 2.94 | 3.94 | 4.92 | 5.90 | 6.89 | 7.87 | 8.86 | 9.84  | 10.82 | 11.81 | 12.79 | 13.78 | 14.76 | 15.74 | 16.73 | 17.71 | 18.70 | 19.68 |
| 3     | 0.90          | 1.84 | 2.82 | 3.84 | 4.88 | 5.86 | 6.83 | 7.81 | 8.78 | 9.76  | 10.74 | 11.71 | 12.69 | 13.66 | 14.64 | 15.62 | 16.59 | 17.57 | 18.54 | 19.52 |
| 4     | 0.86          | 1.76 | 2.70 | 3.68 | 4.70 | 5.76 | 6.78 | 7.74 | 8.71 | 9.68  | 10.65 | 11.62 | 12.58 | 13.55 | 14.52 | 15.49 | 16.46 | 17.42 | 18.39 | 19.36 |
| 5     | 0.82          | 1.68 | 2.58 | 3.52 | 4.50 | 5.52 | 6.58 | 7.68 | 8.64 | 9.60  | 10.56 | 11.52 | 12.48 | 13.44 | 14.40 | 15.36 | 16.32 | 17.28 | 18.24 | 19.20 |
| 6     | 0.78          | 1.60 | 2.46 | 3.36 | 4.30 | 5.28 | 6.30 | 7.36 | 8.46 | 9.52  | 10.47 | 11.42 | 12.38 | 13.33 | 14.28 | 15.23 | 16.18 | 17.14 | 18.09 | 19.04 |
| 7     | 0.74          | 1.52 | 2.34 | 3.20 | 4.10 | 5.04 | 6.02 | 7.04 | 8.10 | 9.20  | 10.34 | 11.33 | 12.27 | 13.22 | 14.16 | 15.10 | 16.05 | 16.99 | 17.94 | 18.88 |
| 8     | 0.70          | 1.44 | 2.22 | 3.04 | 3.90 | 4.80 | 5.74 | 6.72 | 7.74 | 8.80  | 9.90  | 11.04 | 12.17 | 13.10 | 14.04 | 14.98 | 15.91 | 16.85 | 17.78 | 18.72 |
| 9     | 0.66          | 1.36 | 2.10 | 2.88 | 3.70 | 4.56 | 5.46 | 6.40 | 7.38 | 8.40  | 9.46  | 10.56 | 11.70 | 12.88 | 13.92 | 14.85 | 15.78 | 16.70 | 17.63 | 18.56 |
| 10    | 0.62          | 1.28 | 1.98 | 2.72 | 3.50 | 4.32 | 5.18 | 6.08 | 7.02 | 8.00  | 9.02  | 10.08 | 11.18 | 12.32 | 13.50 | 14.72 | 15.64 | 16.56 | 17.48 | 18.40 |
| 11    | 0.58          | 1.20 | 1.86 | 2.56 | 3.30 | 4.08 | 4.90 | 5.76 | 6.66 | 7.60  | 8.58  | 9.60  | 10.66 | 11.76 | 12.90 | 14.08 | 15.30 | 16.42 | 17.33 | 18.24 |
| 12    | 0.54          | 1.12 | 1.74 | 2.40 | 3.10 | 3.84 | 4.62 | 5.44 | 6.30 | 7.20  | 8.14  | 9.12  | 10.14 | 11.20 | 12.30 | 13.44 | 14.62 | 15.84 | 17.10 | 18.08 |
| 13    | 0.50          | 1.04 | 1.62 | 2.24 | 2.90 | 3.60 | 4.34 | 5.12 | 5.94 | 6.80  | 7.70  | 8.64  | 9.62  | 10.64 | 11.70 | 12.80 | 13.94 | 15.12 | 16.34 | 17.60 |
| 14    | 0.46          | 0.96 | 1.50 | 2.08 | 2.70 | 3.36 | 4.06 | 4.80 | 5.58 | 6.40  | 7.26  | 8.16  | 9.10  | 10.08 | 11.10 | 12.16 | 13.26 | 14.40 | 15.58 | 16.80 |
| 15    | 0.42          | 0.88 | 1.38 | 1.92 | 2.50 | 3.12 | 3.78 | 4.48 | 5.22 | 6.00  | 6.82  | 7.68  | 8.58  | 9.52  | 10.50 | 11.52 | 12.58 | 13.68 | 14.82 | 16.00 |
| 16    | 0.38          | 0.80 | 1.26 | 1.76 | 2.30 | 2.88 | 3.50 | 4.16 | 4.86 | 5.60  | 6.38  | 7.20  | 8.06  | 8.96  | 9.90  | 10.88 | 11.90 | 12.96 | 14.06 | 15.20 |
| 17    | 0.34          | 0.72 | 1.14 | 1.60 | 2.10 | 2.64 | 3.22 | 3.84 | 4.50 | 5.20  | 5.94  | 6.72  | 7.54  | 8.40  | 9.30  | 10.24 | 11.22 | 12.24 | 13.30 | 14.40 |
| 18    | 0.30          | 0.64 | 1.02 | 1.44 | 1.90 | 2.40 | 2.94 | 3.52 | 4.14 | 4.80  | 5.50  | 6.24  | 7.02  | 7.84  | 8.70  | 9.60  | 10.54 | 11.52 | 12.54 | 13.60 |
| 19    | 0.26          | 0.56 | 0.90 | 1.28 | 1.70 | 2.16 | 2.66 | 3.20 | 3.78 | 4.40  | 5.06  | 5.76  | 6.50  | 7.28  | 8.10  | 8.96  | 9.86  | 10.80 | 11.78 | 12.80 |
| 20    | 0.22          | 0.48 | 0.78 | 1.12 | 1.50 | 1.92 | 2.38 | 2.88 | 3.42 | 4.00  | 4.62  | 5.28  | 5.98  | 6.72  | 7.50  | 8.32  | 9.18  | 10.08 | 11.02 | 12.00 |

Note that these damage values are lower if a player wears pieces of diamond armor or has toughness added to the armor through commands. Without using cheats, armor values of 16 and above are impossible to obtain without at least one piece of diamond or netherite armor.

