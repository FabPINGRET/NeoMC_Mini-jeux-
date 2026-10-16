# Se charge seulement si les biomes du datapack existent (sinon l’appel échoue)
execute if biome 0 0 0 mg:tv_jungle run return 1
return 1
