import json;

def process_jres_file(filename, module_name):
    jres = json.load(open(filename + ".jres"))
    result = {}
    for k, v in jres.items():
        if k.startswith("tile"):
            # tiles
            result[module_name + "_" + k] = v
        elif k == "*" or k == "transparency16":
            pass
        else:
            # level
            tilemap_level = {}
            for tilemap_level_item_key, tilemap_level_item_value in v.items():
                if tilemap_level_item_key == u"tileset":
                    tilemap_level_item_array = []
                    for tile in tilemap_level_item_value:
                        tilemap_level_item_array.append(tile.replace(u"myTiles.tile", u"myTile." + module_name + u"_tile"))
                    tilemap_level[tilemap_level_item_key] = tilemap_level_item_array
                else:
                    tilemap_level[tilemap_level_item_key] = tilemap_level_item_value
            print(tilemap_level)
            result[k] = tilemap_level

    json.dump(result, open("result.jres", 'w', encoding='UTF-8'), ensure_ascii=False,  indent=4)


if __name__ == '__main__':
    filename = 'source'
    module_name = 'reese'
    process_jres_file(filename, module_name)
