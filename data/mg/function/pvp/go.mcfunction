# Arène PvP — début : distribution du kit
# Plus de saturation ni de régénération naturelle : on ne se soigne que sur KILL (ou pommes d'or)
effect clear @a[tag=mg.play] minecraft:saturation
function mg:core/regen_off
execute if score $pc mg.st matches 1 run return run function mg:pvp2/kits
give @a[tag=mg.play] minecraft:iron_sword
give @a[tag=mg.play] minecraft:bow
give @a[tag=mg.play] minecraft:arrow 16
give @a[tag=mg.play] minecraft:golden_apple 2
item replace entity @a[tag=mg.play] weapon.offhand with minecraft:shield[unbreakable={}]
item replace entity @a[tag=mg.play] armor.head with minecraft:iron_helmet
item replace entity @a[tag=mg.play] armor.chest with minecraft:iron_chestplate
item replace entity @a[tag=mg.play] armor.legs with minecraft:leather_leggings
item replace entity @a[tag=mg.play] armor.feet with minecraft:iron_boots
tellraw @a[tag=mg.play] [{"text":"⚔ Chacun pour soi : dernier survivant = gagnant !","color":"yellow"}]
