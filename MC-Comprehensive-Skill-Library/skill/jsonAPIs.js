const fs = require('fs').promises;
const path = require('path');

const cur_dir = path.dirname(path.resolve(__filename));
// cur_dir here is actually mineflayer dir
const preToolPath = path.join(cur_dir, '../../../../MC-Comprehensive-Skill-Library/json/pre_tool.json');
const preItemPath = path.join(cur_dir, '../../../../MC-Comprehensive-Skill-Library/json/pre_item.json');
const preSmeltPath = path.join(cur_dir, '../../../../MC-Comprehensive-Skill-Library/json/pre_smelt.json');
const preCollectPath = path.join(cur_dir, '../../../../MC-Comprehensive-Skill-Library/json/pre_collect.json')
const funcPath = path.join(cur_dir, '../../../../MC-Comprehensive-Skill-Library/json/func.json');
const mapNamePath = path.join(cur_dir, '../../../../MC-Comprehensive-Skill-Library/json/map_name.json');

async function preTool(item) {
  const data = await fs.readFile(preToolPath, 'utf-8');
  const json = JSON.parse(data);
  return json[item];
}

async function preItem(item) {
  const data = await fs.readFile(preItemPath, 'utf-8');
  const json = JSON.parse(data);
  return json[item];
}

async function preSmelt(item) {
  const data = await fs.readFile(preSmeltPath, 'utf-8');
  const json = JSON.parse(data);
  return json[item];
}

async function preCollect(item) {
  const data = await fs.readFile(preCollectPath, 'utf-8');
  const json = JSON.parse(data);
  return json[item];
}

async function getFunc(item) {
  const data = await fs.readFile(funcPath, 'utf-8');
  const json = JSON.parse(data);
  return json[item];
}

async function mapName(item) {
  const data = await fs.readFile(mapNamePath, 'utf-8');
  const json = JSON.parse(data);
  if (json[item]) {
    return json[item];
  } else {
    return [item];
  }
}

async function getTotalCount(bot, type) {
  // todo: refactor this
  let nameList = [];
  let totalCount = 0;
  if (type == "plank" || type == "log" || type == "wood") {
    nameList = await mapName(type);
  } else {
    nameList = [type];
  }
  for (let itemType of nameList) {
    if (mcData.itemsByName[itemType]) {
      let itemId = mcData.itemsByName[itemType].id;
      let count = bot.inventory.count(itemId);
      totalCount += count;
    } else {
      console.warn(`Item type ${itemType} not found in mcData.itemsByName`);
    }
  }

  return totalCount;
}