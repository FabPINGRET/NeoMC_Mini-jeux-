# ================================================================== RESOURCE PACK (resourcepack/, espace de noms mg)
# Activé par /function mg:rp_on ($rp mg.st = 1) : chaque nouvelle entité du kart reçoit son modèle du pack
# (kart 3D teinté, carapaces, bananes, bob-omb, boîtes ?). Sans pack ($rp = 0), rien ne change.
K3 = 0.85
K3TR = (0, round(0.5 * K3, 3), round(-2.5 / 16 * K3, 3))
FLIP = 'left_rotation:[0f,1f,0f,0f],right_rotation:[0f,0f,0f,1f]'
RGB = {'red': 0xE53935, 'blue': 0x2962FF, 'lime': 0x64DD17, 'yellow': 0xFFD600, 'purple': 0x8E24AA, 'orange': 0xFF6D00,
       'cyan': 0x00B8D4, 'pink': 0xFF4081}
SKIN = [('minecraft:yellow_dye', 'banana'), ('minecraft:leather_helmet[minecraft:dyed_color=3381555]', 'shell_green'),
        ('minecraft:leather_helmet[minecraft:dyed_color=13382451]', 'shell_red'),
        ('minecraft:leather_helmet[minecraft:dyed_color=3364351]', 'shell_blue'), ('minecraft:black_concrete', 'bobomb'),
        ('minecraft:yellow_stained_glass', 'item_box')]

def k3tf(f):
    return 'translation:[%sf,%sf,%sf],%s,scale:[%sf,%sf,%sf]' % (*[round(v * f, 3) for v in K3TR], FLIP, *[round(K3 * f, 3)] * 3)

def setmodel(m):
    return f'item modify entity @s contents {{"function":"minecraft:set_components","components":{{"minecraft:item_model":"mg:{m}"}}}}'

skin = ['# Habille @s (nouvelle entité du kart) avec le modèle du resource pack', 'tag @s add mg.rps',
        'execute if entity @s[tag=mg.kart] run return run function mg:kart/rp_kart']
skin += [f'execute if entity @s[type=minecraft:block_display,tag={t}] run return run data modify entity @s block_state.Name set value "minecraft:air"'
         for t in ('mg.kp1', 'mg.kp2', 'mg.kp3', 'mg.kp4')]
skin += [f'execute if entity @s[type=minecraft:item_display] if items entity @s contents {it} run return run {setmodel(m)}' for it, m in SKIN]
fn('rp_skin', '\n'.join(skin) + '\n')

kart3d = ['# Kart 3D du pack : un seul modèle teinté à la couleur du pilote, monté sur le kart (le bloc devient invisible)',
          f'summon minecraft:item_display ~ ~ ~ {{Tags:["mg.k3d","mg.k3dn","mg.kpart","mg.fx","mg.rps"],teleport_duration:2,'
          f'item:{{id:"minecraft:leather_horse_armor",components:{{"minecraft:item_model":"mg:kart","minecraft:dyed_color":{RGB["red"]}}}}},'
          f'transformation:{{{k3tf(1)}}}}}']
kart3d += [f'execute if data entity @s {{block_state:{{Name:"minecraft:{c}_concrete"}}}} run data modify entity @e[type=minecraft:item_display,tag=mg.k3dn,limit=1] item.components."minecraft:dyed_color" set value {RGB[c]}'
           for c in COLORS]
kart3d += ['data modify entity @s block_state.Name set value "minecraft:air"',
           'ride @e[type=minecraft:item_display,tag=mg.k3dn,limit=1] mount @s',
           'rotate @e[type=minecraft:item_display,tag=mg.k3dn,limit=1] ~ 0',
           'tag @e[tag=mg.k3dn] remove mg.k3dn']
fn('rp_kart', '\n'.join(kart3d) + '\n')

def patch_fn(name, old, new):
    p = os.path.join(K, name + '.mcfunction')
    s = open(p, encoding='utf-8').read()
    assert old in s, (name, old)
    with open(p, 'w', encoding='utf-8', newline='\n') as f: f.write(s.replace(old, new, 1))

patch_fn('tick', 'scoreboard players add $ktime mg.st 1\n',
         'scoreboard players add $ktime mg.st 1\n'
         'execute if score $rp mg.st matches 1 as @e[tag=mg.kart,tag=!mg.rps] at @s run function mg:kart/rp_skin\n'
         'execute if score $rp mg.st matches 1 as @e[tag=mg.fx,tag=!mg.rps] at @s run function mg:kart/rp_skin\n')
# boîte qui réapparaît : on la rhabille au tick suivant
patch_fn('box_wait', 'tag @s remove mg.kboff\n', 'tag @s remove mg.kboff\ntag @s remove mg.rps\n')
# méga champignon : le kart 3D grossit aussi
patch_fn('use_mega', 'title @s actionbar',
         f'execute as {KK} on passengers if entity @s[tag=mg.k3d] run data merge entity @s {{start_interpolation:0,interpolation_duration:8,transformation:{{{k3tf(MEGA)}}}}}\ntitle @s actionbar')
patch_fn('mega_end', 'execute at @s run playsound',
         f'execute as {KK} on passengers if entity @s[tag=mg.k3d] run data merge entity @s {{start_interpolation:0,interpolation_duration:8,transformation:{{{k3tf(1)}}}}}\nexecute at @s run playsound')

# objet en main : icône du pack
give = ['# Icône du resource pack pour l\'objet en main (appelé par item_give si $rp = 1)']
ICON = {1: 'banana', 2: 'shell_green', 3: 'shell_red', 4: 'mushroom', 5: 'star', 6: 'lightning', 7: 'shell_blue', 8: 'banana',
        9: 'shell_green', 10: 'shell_red', 11: 'mushroom', 12: 'mushroom_gold', 13: 'bobomb', 14: 'bullet', 15: 'blooper',
        16: 'horn', 17: 'boo', 18: 'item_box', 19: 'mushroom_mega'}
for k, m in ICON.items():
    give.append(f'execute if score @s mg.kit matches {k} run item modify entity @s hotbar.0 {{"function":"minecraft:set_components","components":{{"minecraft:item_model":"mg:{m}"}}}}')
fn('rp_icon', '\n'.join(give) + '\n')
patch_fn('item_give', "scoreboard players set @s mg.kic 1\n",
         "execute if score $rp mg.st matches 1 run function mg:kart/rp_icon\nscoreboard players set @s mg.kic 1\n")
