"""🧟 Zombies : souffle des roquettes (zx/rk_kb) malus rares sur morsure (zx/malus + avancement mg:zmhurt) et batte cloutée (zx/bat*). Importé par gen_zombies.py."""
import json
import os


def write(w, C, js):
    w('zx/rk_kb', ['# @s (mob) soufflé par la roquette : vitesse dans la direction explosion → mob (contexte : explosion, tourné vers @s, levé de 22°)',
                   'summon minecraft:marker ^ ^ ^1 {Tags:["mg.zkb"]}',
                   'execute store result score $kvx mg.st run data get entity @e[type=minecraft:marker,tag=mg.zkb,limit=1] Pos[0] 1000',
                   'execute store result score $kvy mg.st run data get entity @e[type=minecraft:marker,tag=mg.zkb,limit=1] Pos[1] 1000',
                   'execute store result score $kvz mg.st run data get entity @e[type=minecraft:marker,tag=mg.zkb,limit=1] Pos[2] 1000',
                   'kill @e[type=minecraft:marker,tag=mg.zkb]',
                   'scoreboard players operation $kvx mg.st -= $kbx mg.st', 'scoreboard players operation $kvy mg.st -= $kby mg.st',
                   'scoreboard players operation $kvz mg.st -= $kbz mg.st',
                   'execute store result entity @s Motion[0] double 0.0014 run scoreboard players get $kvx mg.st',
                   'execute store result entity @s Motion[1] double 0.0016 run scoreboard players get $kvy mg.st',
                   'execute store result entity @s Motion[2] double 0.0014 run scoreboard players get $kvz mg.st'])

    # --- malus, rarement (8 %), quand un mob mord un survivant
    w('zx/malus', ['# Avancement mg:zmhurt : @s touché par un mob du mode Zombies → 8 % de chances d\'un malus court',
                   'advancement revoke @s only mg:zmhurt',
                   'execute unless score $state mg.st matches 2 run return 0', 'execute unless entity @s[tag=mg.play,tag=!mg.zdead] run return 0',
                   'execute store result score #zml mg.st run random value 1..100', 'execute if score #zml mg.st matches 9.. run return 0',
                   'execute store result score #zml mg.st run random value 1..4',
                   'execute if score #zml mg.st matches 1 run effect give @s minecraft:slowness 1 2 true',
                   'execute if score #zml mg.st matches 1 run title @s actionbar {"text":"🐌 Jambe mordue : ralenti 1 s","color":"red"}',
                   'execute if score #zml mg.st matches 2 run effect give @s minecraft:blindness 2 0 true',
                   'execute if score #zml mg.st matches 2 run title @s actionbar {"text":"🩸 Du sang dans les yeux : aveuglé 2 s","color":"red"}',
                   'execute if score #zml mg.st matches 3 run effect give @s minecraft:nausea 4 0 true',
                   'execute if score #zml mg.st matches 3 run title @s actionbar {"text":"🤢 Infecté : nausée 4 s","color":"red"}',
                   'execute if score #zml mg.st matches 4 run effect give @s minecraft:weakness 3 0 true',
                   'execute if score #zml mg.st matches 4 run title @s actionbar {"text":"💢 Bras mordu : faiblesse 3 s","color":"red"}',
                   'playsound minecraft:entity.zombie.infect player @s ~ ~ ~ 0.8 1.2'])

    _adv = os.path.join(C.D, 'advancement', 'zmhurt.json')
    with open(_adv, 'w', encoding='utf-8', newline='\n') as _f:
        json.dump({'criteria': {'mob': {'trigger': 'minecraft:entity_hurt_player', 'conditions': {'damage': {'type': {
            'source_entity': {'minecraft:nbt': '{Tags:["mg.zz"]}'}}}}}},
            'rewards': {'function': 'mg:zx/malus'}}, _f, ensure_ascii=False, indent=2)
        _f.write('\n')

    # --- batte (comme dans Neo GTA, en plus forte) : remplace le couteau
    BATZ = ('item replace entity @s hotbar.0 with minecraft:wooden_sword[item_model="$(m)",unbreakable={},'
            f'custom_name={js({"text": "🏏 Batte cloutée", "color": "gold", "italic": False})},'
            'attribute_modifiers=[{type:"minecraft:attack_damage",id:"mg:zbat",amount:13.0,operation:"add_value",slot:"mainhand"},'
            '{type:"minecraft:attack_knockback",id:"mg:zbatk",amount:1.0,operation:"add_value",slot:"mainhand"}]]')
    w('zx/bat', ['# Macro $(m) : modèle', '$' + BATZ])
    w('zx/bat_give', ['execute if score $rp mg.st matches 1 run function mg:zx/bat {m:"mg:bat"}',
                      'execute unless score $rp mg.st matches 1 run function mg:zx/bat {m:"minecraft:stick"}'])
