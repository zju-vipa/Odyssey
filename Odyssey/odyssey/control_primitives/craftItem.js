async function craftItem(bot, name, count = 1) {
    // return if name is not string
    if (typeof name !== "string") {
        throw new Error("name for craftItem must be a string");
    }
    // return if count is not number
    if (typeof count !== "number") {
        throw new Error("count for craftItem must be a number");
    }
    const itemByName = mcData.itemsByName[name];
    if (!itemByName) {
        throw new Error(`No item named ${name}`);
    }
    const craftingTable = bot.findBlock({
        matching: mcData.blocksByName.crafting_table.id,
        maxDistance: 32,
    });
    const noCraftingTableList = [
        "crafting_table", 
        "melon_seeds", "pumpkin_seeds", "sugar", 
        "iron_nugget", "iron_trapdoor", "heavy_weighted_pressure_plate", "light_weighted_pressure_plate",
        "stick", "torch", "flint_and_steel", "lever",
        "oak_planks", "birch_planks", "spruce_planks", "jungle_planks", "acacia_planks", "dark_oak_planks", "mangrove_planks",
        "cut_sandstone"];
    if (noCraftingTableList.includes(name)) {
        const recipe = bot.recipesFor(itemByName.id, null, 1, null)[0];
        try {
            await bot.craft(recipe, count, null);
            bot.chat(`I did the recipe for ${name} ${count} times`);
            return;
        } catch (err) {
            bot.chat(`I cannot do the recipe for ${name} ${count} times`);
        }
    }
    if (!craftingTable) {
        bot.chat("Craft without a crafting table");
    } else {
        await bot.pathfinder.goto(
            new GoalLookAtBlock(craftingTable.position, bot.world)
        );
    }
    const recipe = bot.recipesFor(itemByName.id, null, 1, craftingTable)[0];
    if (recipe) {
        bot.chat(`I can make ${name}`);
        try {
            await bot.craft(recipe, count, craftingTable);
            bot.chat(`I did the recipe for ${name} ${count} times`);
        } catch (err) {
            bot.chat(`I cannot do the recipe for ${name} ${count} times`);
        }
    } else {
        failedCraftFeedback(bot, name, itemByName, craftingTable);
        _craftItemFailCount++;
        if (_craftItemFailCount > 10) {
            throw new Error(
                "craftItem failed too many times, check chat log to see what happened"
            );
        }
    }
}
