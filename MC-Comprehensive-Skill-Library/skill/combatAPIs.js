async function killMob(bot, mobName, timeout = 300) {
    // return if mobName is not string
    if (typeof mobName !== "string") {
        throw new Error(`mobName for killMob must be a string`);
    }
    // return if timeout is not number
    if (typeof timeout !== "number") {
        throw new Error(`timeout for killMob must be a number`);
    }

    const weaponsForShooting = [
        "bow",
        "crossbow",
        "snowball",
        "ender_pearl",
        "egg",
        "splash_potion",
        "trident",
    ];
    const mainHandItem = bot.inventory.slots[bot.getEquipmentDestSlot("hand")];

    const entity = bot.nearestEntity(
        (entity) =>
            entity.name === mobName &&
            // kill mob distance should be slightly bigger than explore distance
            entity.position.distanceTo(bot.entity.position) < 48
    );
    if (!entity) {
        bot.chat(`No ${mobName} nearby, please explore first`);
        _killMobFailCount++;
        if (_killMobFailCount > 10) {
            throw new Error(
                `killMob failed too many times, make sure you explore before calling killMob`
            );
        }
        return;
    }

    let droppedItem;
    if (mainHandItem && weaponsForShooting.includes(mainHandItem.name)) {
        bot.hawkEye.autoAttack(entity, mainHandItem.name);
        droppedItem = await waitForMobShot(bot, entity, timeout);
    } else {
        await bot.pvp.attack(entity);
        droppedItem = await waitForMobRemoved(bot, entity, timeout);
    }
    if (droppedItem) {
        await bot.collectBlock.collect(droppedItem, { ignoreNoPath: true });
    }
    bot.save(`${mobName}_killed`);
}

function waitForMobRemoved(bot, entity, timeout = 300) {
    return new Promise((resolve, reject) => {
        let success = false;
        let droppedItem = null;
        // Set up timeout
        const timeoutId = setTimeout(() => {
            success = false;
            bot.pvp.stop();
        }, timeout * 1000);

        // Function to handle entityRemoved event
        function onEntityGone(e) {
            if (e === entity) {
                success = true;
                clearTimeout(timeoutId);
                bot.chat(`Killed ${entity.name}!`);
                bot.pvp.stop();
            }
        }

        function onItemDrop(item) {
            if (entity.position.distanceTo(item.position) <= 1) {
                droppedItem = item;
            }
        }

        function onStoppedAttacking() {
            clearTimeout(timeoutId);
            bot.removeListener("entityGone", onEntityGone);
            bot.removeListener("stoppedAttacking", onStoppedAttacking);
            bot.removeListener("itemDrop", onItemDrop);
            if (!success) reject(new Error(`Failed to kill ${entity.name}.`));
            else resolve(droppedItem);
        }

        // Listen for entityRemoved event
        bot.on("entityGone", onEntityGone);
        bot.on("stoppedAttacking", onStoppedAttacking);
        bot.on("itemDrop", onItemDrop);
    });
}


function waitForMobShot(bot, entity, timeout = 300) {
    return new Promise((resolve, reject) => {
        let success = false;
        let droppedItem = null;
        // Set up timeout
        const timeoutId = setTimeout(() => {
            success = false;
            bot.hawkEye.stop();
        }, timeout * 1000);

        // Function to handle entityRemoved event
        function onEntityGone(e) {
            if (e === entity) {
                success = true;
                clearTimeout(timeoutId);
                bot.chat(`Shot ${entity.name}!`);
                bot.hawkEye.stop();
            }
        }

        function onItemDrop(item) {
            if (entity.position.distanceTo(item.position) <= 1) {
                droppedItem = item;
            }
        }

        function onAutoShotStopped() {
            clearTimeout(timeoutId);
            bot.removeListener("entityGone", onEntityGone);
            bot.removeListener("auto_shot_stopped", onAutoShotStopped);
            bot.removeListener("itemDrop", onItemDrop);
            if (!success) reject(new Error(`Failed to shoot ${entity.name}.`));
            else resolve(droppedItem);
        }

        // Listen for entityRemoved event
        bot.on("entityGone", onEntityGone);
        bot.on("auto_shot_stopped", onAutoShotStopped);
        bot.on("itemDrop", onItemDrop);
    });
}

// shoot 1 pig with a bow: shoot(bot, "bow", "pig");
async function shoot(bot, weapon, target) {
    const validWeapons = [
        "bow",
        "crossbow",
        "snowball",
        "ender_pearl",
        "egg",
        "splash_potion",
        "trident",
    ];
    if (!validWeapons.includes(weapon)) {
        bot.chat(`${weapon} is not a valid weapon for shooting`);
        return;
    }

    const weaponItem = mcData.itemsByName[weapon];
    if (!bot.inventory.findInventoryItem(weaponItem.id, null)) {
        bot.chat(`No ${weapon} in inventory for shooting`);
        return;
    }

    const targetEntity = bot.nearestEntity(
        (entity) =>
            entity.name === target
    );
    if (!targetEntity) {
        bot.chat(`No ${target} nearby`);
        return;
    }
    bot.hawkEye.autoAttack(targetEntity, "bow");
    bot.on('auto_shot_stopped', (target) => {
    })
}

