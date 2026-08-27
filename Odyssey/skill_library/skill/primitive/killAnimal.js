async function killAnimal(bot, type = null) {
    const equipped = await equipSword(bot);
    if (!equipped) {
        return null;
    }
    // killMob owns target selection, combat, drop collection and the result.
    return await killMob(bot, type, 300);
}
