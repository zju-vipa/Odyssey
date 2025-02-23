const fs = require('fs').promises;
const path = require('path');

const cur_dir = path.dirname(path.resolve(__filename));
// cur_dir here is actually mineflayer dir
const countMapNamePath = path.join(cur_dir, '../../../MCskill/json/count_map_name.json');
const preToolPath = path.join(cur_dir, '../../../MCskill/json/pre_tool.json');
const preItemPath = path.join(cur_dir, '../../../MCskill/json/pre_item.json');
const preSmeltPath = path.join(cur_dir, '../../../MCskill/json/pre_smelt.json');
const preCollectPath = path.join(cur_dir, '../../../MCskill/json/pre_collect.json')
const funcPath = path.join(cur_dir, '../../../MCskill/json/func.json');
const mapNamePath = path.join(cur_dir, '../../../MCskill/json/map_name.json');

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

async function mapNameReverse(item) {
  let no_need_to_handle = ["log", "cobble", "cobblestone", "cobbled_deepslate", "stone", "deepslate", "gravel", "grass"];
  if (no_need_to_handle.includes(item)) return item;
  // manually handle something... (LLM tends to use '_ore' as type para)
  const data = await fs.readFile(mapNamePath, 'utf-8');
  const json = JSON.parse(data);
  for (const [key, valueList] of Object.entries(json)) {
    if (valueList.includes(item)) {
      return key;
    }
  }
  return item;
}

async function countMapName(item) {
  const data = await fs.readFile(countMapNamePath, 'utf-8');
  const json = JSON.parse(data);
  if (json[item]) {
    return json[item];
  } else {
    return [item];
  }
}

async function getTotalCount(bot, type) {
  let nameList = [];
  let totalCount = 0;
  nameList = await countMapName(type);
  for (let itemType of nameList) {
    if (mcData.itemsByName[itemType]) {
      let itemId = mcData.itemsByName[itemType].id;
      let count = bot.inventory.count(itemId);
      totalCount += count;
    } else {
      console.warn(`Item type ${itemType} not found in mcData.itemsByName`);
      bot.chat(`Item type ${itemType} not found in mcData.itemsByName`);
    }
  }
  return totalCount;
}

async function default_fallback_function(bot) {
  bot.chat('Error parsing LLM response. Retrying...');
  return;
}