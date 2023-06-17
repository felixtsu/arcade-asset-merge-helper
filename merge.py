import json;
import glob;

result = {}



# TODO 这个地方有问题，还需要生成transparent和* 
def process_jres_file(filename, module_name):
    modified_tiles = []
    jres = json.load(open(filename))
    for k, v in jres.items():
        if k == "*" or k == "transparency16":
            pass
        elif v['mimeType'] == 'image/x-mkcd-f4':
            # tiles
            v['displayName'] = module_name + "_" + v['displayName']
            modified_tiles.append(v['displayName'])
            result[module_name + "_" + k] = v
        elif v['mimeType'] == "application/mkcd-tilemap":
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
            if k in result:
                result[module_name + "_" + k] = tilemap_level
                tilemap_level["id"] = module_name + "_" + k
            else:    
                result[k] = tilemap_level

    json.dump(result, open("result.jres", 'w', encoding='UTF-8'), ensure_ascii=False,  indent=4)
    return modified_tiles



def process_ts_file(module_name, modified_tiles):
    # 实际这个文件需要做的事情就是
    # 1. 处理tiles
    # export const 那堆自定义的tiles
    # helpers._registerFactory("tile", function(name: string) {
    # 2. 处理tilemaps   
    # helpers._registerFactory("tilemap", 的function里面把其他tilemap都放在这里；
    # 这里需要替换jres文件里面加入了tilemap的前缀，以及这些tilemaps里面用到的tiles的名称
    

    file_text = open(module_name + ".ts")
    for tile in modified_tiles:
        pass

if __name__ == '__main__':
    module_name = 'mushroomfarm'
    for f in glob.glob("*g.jres"):
        module_name = f[:f.index('.')]
        modified_tiles = process_jres_file(f, module_name)

        process_ts_file(module_name, modified_tiles)
    
