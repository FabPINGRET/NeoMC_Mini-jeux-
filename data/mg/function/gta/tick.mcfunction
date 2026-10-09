# 🚓 Neo City : chaque tick tant qu'un joueur y est
scoreboard players add $gtt mg.st 1
execute as @a[tag=mg.gtw,scores={mg.gqs=1..}] if items entity @s weapon.mainhand *[custom_data~{gtaphone:1b}] run function mg:gta/phone
execute as @a[tag=mg.gtw,scores={mg.gqs=1..}] if items entity @s weapon.mainhand *[custom_data~{gtanitro:1b}] run function mg:gta/nitro
execute as @a[tag=mg.gtw,scores={mg.gmis=1..}] run function mg:gta/mis_cmd
scoreboard players remove @a[tag=mg.gtw,scores={mg.gnit=1..}] mg.gnit 1
execute as @a[tag=mg.gtw,scores={mg.gcas=1..}] at @s run function mg:gta/cas_cmd
execute as @a[tag=mg.gslot] at @s run function mg:gta/cas_slot_anim
scoreboard players remove @a[tag=mg.gtw,scores={mg.gcre=1..}] mg.gcre 1
execute as @a[tag=mg.gtw,scores={mg.gcre=1}] run function mg:gta/cas_reopen_tick
execute as @a[tag=mg.gtw,scores={mg.gqs=1..}] if items entity @s weapon.mainhand *[custom_data~{rpg:1b}] at @s run function mg:gta/panic
execute as @a[tag=mg.gtw,scores={mg.gqs=1..}] at @s if items entity @s weapon.mainhand *[custom_data~{rpg:1b}] run function mg:gta/rpg_fire
execute as @a[tag=mg.gtw,scores={mg.gqs=1..}] if items entity @s weapon.mainhand *[custom_data~{gtahome:1b}] run function mg:gta/home
execute as @a[tag=mg.gtw,scores={mg.gqs=1..}] at @s run function mg:gun/use
execute as @a[tag=mg.gtw,scores={mg.gqs=1..}] if items entity @s weapon.mainhand *[custom_data~{mg_gun:1b}] at @s run function mg:gta/panic
execute as @a[tag=mg.gtw,scores={mg.gqs=1..}] if items entity @s weapon.mainhand *[custom_data~{rpg:1b}] at @s run function mg:gta/panic
scoreboard players reset @a[scores={mg.gqs=1..}] mg.gqs
execute as @e[type=minecraft:marker,tag=mg.gtraf] at @s run function mg:gta/traffic/tick
execute as @e[type=minecraft:interaction,tag=mg.gcint] if data entity @s interaction run function mg:gta/car_int
execute as @e[type=minecraft:interaction,tag=mg.gtint] if data entity @s interaction run function mg:gta/traffic/int
execute as @e[type=minecraft:marker,tag=mg.gphel] at @s run function mg:gta/pheli_tick
function mg:gta/panic_tick
scoreboard players remove @a[tag=mg.gtw,scores={mg.gcd=1..}] mg.gcd 1
execute as @a[tag=mg.gtw,scores={mg.grl=1..}] at @s run function mg:gun/reload_tick
execute as @a[tag=mg.gtw,scores={mg.gsn=1..}] if items entity @s weapon.mainhand *[custom_data~{gun:5}] run scoreboard players reset @s mg.gsn
execute as @a[tag=mg.gtw,scores={mg.gsn=1..}] at @s run function mg:gun/sneak
scoreboard players reset @a[tag=mg.gtw,scores={mg.gsn=1..}] mg.gsn
execute as @a[tag=mg.gscope] unless items entity @s weapon.mainhand *[custom_data~{gun:5}] run function mg:gta/unscope
execute as @a[tag=mg.gscope] unless predicate mg:sneak run function mg:gta/unscope
execute as @e[type=minecraft:item_display,tag=mg.grkt] at @s run function mg:gta/rocket_tick
scoreboard players remove @a[tag=mg.gtw,scores={mg.gtl=1..}] mg.gtl 1
scoreboard players remove @a[tag=mg.gtw,scores={mg.gal=1..}] mg.gal 1
scoreboard players operation $gq2 mg.st = $gtt mg.st
scoreboard players set #2 mg.st 2
scoreboard players operation $gq2 mg.st %= #2 mg.st
execute if score $gq2 mg.st matches 0 if score $rp mg.st matches 1 as @a[tag=mg.gtw,scores={mg.gtl=..0}] if items entity @s weapon.mainhand *[custom_data~{mg_gun:1b}] at @s run function mg:gta/aim
execute if score $gq2 mg.st matches 0 if score $rp mg.st matches 1 as @a[tag=mg.gtw,scores={mg.gtl=..0}] if items entity @s weapon.mainhand *[custom_data~{rpg:1b}] at @s run function mg:gta/aim
execute as @e[type=minecraft:horse,tag=mg.gcarh] at @s run function mg:gta/car_sync
execute as @e[type=minecraft:happy_ghast,tag=mg.ghel] at @s run function mg:gta/heli_sync
scoreboard players operation $gq mg.st = $gtt mg.st
scoreboard players set #20 mg.st 20
scoreboard players operation $gq mg.st %= #20 mg.st
execute if score $gq mg.st matches 0 as @e[tag=mg.gcop] at @s if entity @a[tag=mg.gtw,scores={mg.gwl=1..},gamemode=!spectator,distance=..28] run function mg:gta/cop_fire
execute if score $gq mg.st matches 10 as @e[tag=mg.gcop] at @s if entity @a[tag=mg.gtw,scores={mg.gwl=1..},gamemode=!spectator,distance=..28] run function mg:gta/cop_fire
execute as @a[tag=mg.gtw,scores={mg.gkp=1..}] run function mg:gta/kill_player
execute as @a[tag=mg.gtw,scores={mg.gkv=1..}] run function mg:gta/kill_ped
execute as @a[tag=mg.gtw,scores={mg.gks=1..}] run function mg:gta/kill_cop
execute as @a[tag=mg.gtw,scores={mg.gkw=1..}] run function mg:gta/kill_cop
execute as @a[tag=mg.gtw,scores={mg.deaths=1..}] in mg:gta run function mg:gta/wasted
scoreboard players remove @a[tag=mg.gtw,scores={mg.gwt=1..}] mg.gwt 1
execute as @a[tag=mg.gtw,scores={mg.gwl=1..,mg.gwt=0}] run function mg:gta/wanted_down
execute as @e[type=minecraft:item_display,tag=mg.gpdi] at @s run tp @s ~ ~ ~ ~5 ~
execute as @e[type=minecraft:item_display,tag=mg.gcash,tag=!mg.gbill] at @s run tp @s ~ ~ ~ ~4 ~
execute as @a[tag=mg.gtw] at @s as @e[type=minecraft:item_display,tag=mg.gcash,distance=..1.6,limit=1] run function mg:gta/cash_take
execute as @a[tag=mg.gtw] at @s if entity @e[type=minecraft:marker,tag=mg.gexit,distance=..1.3] in minecraft:overworld run function mg:gta/leave
scoreboard players operation $gq5t mg.st = $gtt mg.st
scoreboard players set #5 mg.st 5
scoreboard players operation $gq5t mg.st %= #5 mg.st
execute if score $gq5t mg.st matches 0 as @a[tag=mg.gtw,gamemode=!spectator] if predicate mg:sneak if items entity @s weapon.mainhand *[custom_data~{mg_gun:1b}] at @s run function mg:gta/rob
execute if score $gq5t mg.st matches 0 as @a[tag=mg.gtw,gamemode=!spectator] if predicate mg:sneak if items entity @s weapon.mainhand *[custom_data~{rpg:1b}] at @s run function mg:gta/rob
execute if score $gq5t mg.st matches 0 as @a[tag=mg.gtw,scores={mg.grob=1..}] unless predicate mg:sneak run function mg:gta/rob_stop
execute if score $gq5t mg.st matches 0 as @a[tag=mg.gtw,scores={mg.gmt=1..}] at @s run function mg:gta/mis_tick
execute if score $gq5t mg.st matches 0 as @a[tag=mg.gtw,gamemode=!spectator] if predicate mg:sneak at @s if entity @e[type=minecraft:marker,tag=mg.gtraf,distance=..2.6] run function mg:gta/traffic/steal_near
scoreboard players operation $gq4 mg.st = $gtt mg.st
scoreboard players set #4 mg.st 4
scoreboard players operation $gq4 mg.st %= #4 mg.st
execute if score $gq4 mg.st matches 0 as @a[tag=mg.gtw] if items entity @s weapon.mainhand *[custom_data~{gtamap:1b}] run function mg:gta/map_show
execute as @a[tag=mg.gtw] at @s if entity @e[type=minecraft:marker,tag=mg.glup,distance=..0.8] in mg:gta run function mg:gta/lift_up
execute as @a[tag=mg.gtw] at @s if entity @e[type=minecraft:marker,tag=mg.gldn,distance=..0.8] in mg:gta run function mg:gta/lift_down
execute if score $gq mg.st matches 0 run function mg:gta/second
execute if score $gq mg.st matches 0 run function mg:gta/pads
execute if score $gq mg.st matches 10 run function mg:gta/pads
execute if score $gq mg.st matches 0 run function mg:gta/club_tick
execute if score $gq mg.st matches 10 run function mg:gta/club_tick
execute if score $gq mg.st matches 5 run function mg:gta/hud
execute if score $gq mg.st matches 5 run function mg:gta/radio_check
execute if score $gq mg.st matches 15 run function mg:gta/hud
