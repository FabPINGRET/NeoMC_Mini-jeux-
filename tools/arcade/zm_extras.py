"""🧟 Zombies : lance-roquettes (zx/rpg_*, zx/rk_*) et souffle (zx/rk_kb), malus rares sur morsure (zx/malus + avancement mg:zmhurt), batte cloutée (zx/bat*). Importé par gen_zombies.py."""
import json
import os


def write(w, C, js, BOOM):
    # --- lance-roquettes (munitions illimitées, une roquette toutes les 1,5 s, sans casser le décor)
    RPGB = ('minecraft:warped_fungus_on_a_stick[custom_data={zrpg:1b},unbreakable={},custom_name=' + js({'text': '🚀 Lance-roquettes', 'color': 'red', 'bold': True, 'italic': False}) +
            ',lore=[' + js({'text': 'Clic droit : tirer une roquette', 'color': 'gray', 'italic': False}) + ']')
    w('zx/rpg_put', ['# Macro $(slot) : lance-roquettes', f'$execute if score $rp mg.st matches 1 run item replace entity @s $(slot) with {RPGB},item_model="mg:gun_rpg"]',
                     f'$execute unless score $rp mg.st matches 1 run item replace entity @s $(slot) with {RPGB},item_model="minecraft:crossbow"]'])
    w('zx/rpg_fire', ['# @s tire une roquette', 'scoreboard players reset @s mg.qs', 'execute if score @s mg.gcd matches 1.. run return 0',
                      'scoreboard players set @s mg.gcd 30',
                      'execute anchored eyes positioned ^-0.2 ^-0.1 ^1 run summon minecraft:item_display ~ ~ ~ {Tags:["mg.zent","mg.zrk","mg.zrkn"],'
                      'item:{id:"minecraft:firework_rocket",count:1},teleport_duration:1,'
                      'transformation:{left_rotation:[0.5f,0.5f,-0.5f,0.5f],right_rotation:[0f,0f,0f,1f],translation:[0f,0f,0f],scale:[1.4f,1.4f,1.4f]}}',
                      'execute anchored eyes positioned ^-0.2 ^-0.1 ^1 rotated as @s run tp @e[type=minecraft:item_display,tag=mg.zrkn] ~ ~ ~ ~ ~',
                      'scoreboard players operation @e[type=minecraft:item_display,tag=mg.zrkn] mg.zmo = @s mg.zid',
                      'scoreboard players set @e[type=minecraft:item_display,tag=mg.zrkn] mg.zmc 0', 'tag @e[tag=mg.zrkn] remove mg.zrkn',
                      'playsound minecraft:entity.firework_rocket.launch player @a ~ ~ ~ 1.5 0.6', 'playsound minecraft:entity.blaze.shoot player @a ~ ~ ~ 1 0.5'])
    w('zx/rk_tick', ['# @s : roquette en vol, 3 pas de 0,7 bloc par tick', 'scoreboard players add @s mg.zmc 1',
                     'execute if score @s mg.zmc matches 40.. run return run function mg:zx/rk_boom',
                     'function mg:zx/rk_step', 'execute if entity @s at @s run function mg:zx/rk_step', 'execute if entity @s at @s run function mg:zx/rk_step',
                     'execute if entity @s run particle minecraft:flame ~ ~ ~ 0.05 0.05 0.05 0.02 3'])
    w('zx/rk_step', ['execute unless block ^ ^ ^0.7 #mg:ray_pass positioned ^ ^ ^0.4 run return run function mg:zx/rk_boom',
                     'execute positioned ^ ^ ^0.7 positioned ~ ~-1 ~ if entity @e[tag=mg.zz,distance=..1.3] positioned ~ ~1 ~ run return run function mg:zx/rk_boom',
                     'tp @s ^ ^ ^0.7'])
    w('zx/rk_boom', ['# La roquette explose : 100 de dégâts dans un rayon de 4 (crédités au tireur)'] + BOOM +
      ['scoreboard players set $gdm mg.st 1000', 'execute as @e[tag=mg.zz,distance=..4] run function mg:gun/hit_mob', 'tag @a remove mg.gsh',
       '# souffle : les survivants à 6 blocs sont projetés en arrière',
       '# origine du souffle = point d\'explosion (position d\'exécution, 0,4 à 0,7 bloc devant la roquette) : marqueur temporaire',
       'summon minecraft:marker ~ ~ ~ {Tags:["mg.zkb0"]}',
       'execute store result score $kbx mg.st run data get entity @e[type=minecraft:marker,tag=mg.zkb0,limit=1] Pos[0] 1000',
       'execute store result score $kby mg.st run data get entity @e[type=minecraft:marker,tag=mg.zkb0,limit=1] Pos[1] 1000',
       'execute store result score $kbz mg.st run data get entity @e[type=minecraft:marker,tag=mg.zkb0,limit=1] Pos[2] 1000',
       'kill @e[type=minecraft:marker,tag=mg.zkb0]',
       'execute as @e[tag=mg.zz,distance=..6] facing entity @s feet rotated ~ -22 run function mg:zx/rk_kb',
       'particle minecraft:explosion_emitter ~ ~ ~ 0 0 0 0 1 force', 'particle minecraft:flame ~ ~ ~ 1.5 1.2 1.5 0.12 40 force',
       'playsound minecraft:entity.generic.explode master @a ~ ~ ~ 4 0.8', 'kill @s'])

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
    w('zx/malus', ['# Avancement mg:zmhurt : @s touché par un mob du mode Zombies ($zpts = 1, pas en Infection) → 8 % de chances d\'un malus court',
                   'advancement revoke @s only mg:zmhurt',
                   'execute unless score $state mg.st matches 2 run return 0', 'execute unless score $zpts mg.st matches 1 run return 0',
                   'execute unless entity @s[tag=mg.play,tag=!mg.zdead] run return 0',
                   'execute store result score #zml mg.st run random value 1..100', 'execute if score #zml mg.st matches 9.. run return 0',
                   'execute store result score #zml mg.st run random value 1..4',
                   'execute if score #zml mg.st matches 1 run effect give @s minecraft:slowness 1 2 true',
                   'execute if score #zml mg.st matches 1 run tellraw @s {"text":"🐌 Jambe mordue : ralenti 1 s","color":"red"}',
                   'execute if score #zml mg.st matches 2 run effect give @s minecraft:blindness 2 0 true',
                   'execute if score #zml mg.st matches 2 run tellraw @s {"text":"🩸 Du sang dans les yeux : aveuglé 2 s","color":"red"}',
                   'execute if score #zml mg.st matches 3 run effect give @s minecraft:nausea 4 0 true',
                   'execute if score #zml mg.st matches 3 run tellraw @s {"text":"🤢 Infecté : nausée 4 s","color":"red"}',
                   'execute if score #zml mg.st matches 4 run effect give @s minecraft:weakness 3 0 true',
                   'execute if score #zml mg.st matches 4 run tellraw @s {"text":"💢 Bras mordu : faiblesse 3 s","color":"red"}',
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
