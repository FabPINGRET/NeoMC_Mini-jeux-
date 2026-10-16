# @s : barre d'action selon l'objet en main
execute if items entity @s weapon.mainhand *[custom_data~{tv:2}] run return run function mg:terra/hud_heat
execute if items entity @s weapon.mainhand *[custom_data~{tv:3}] run return run function mg:terra/hud_heat
execute if items entity @s weapon.mainhand *[custom_data~{tv:7}] run return run function mg:terra/hud_heat
execute if items entity @s weapon.mainhand *[custom_data~{tv:14}] if score @s mg.trcd matches 1.. run return run title @s actionbar {"text":"🎖 Capacité : recharge…","color":"gray"}
execute if items entity @s weapon.mainhand *[custom_data~{tv:14}] run return run title @s actionbar {"text":"🎖 Capacité PRÊTE (clic droit)","color":"gold","bold":true}
execute if items entity @s weapon.mainhand *[custom_data~{tv:8}] run return run function mg:terra/hud_heat
execute if items entity @s weapon.mainhand *[custom_data~{tv:4}] if score @s mg.tvsc matches 1.. run return run title @s actionbar {"text":"📢 Canon sonique : recharge…","color":"gray"}
execute if items entity @s weapon.mainhand *[custom_data~{tv:4}] run return run title @s actionbar {"text":"📢 Canon sonique : PRÊT (clic droit)","color":"aqua","bold":true}
execute if items entity @s weapon.mainhand *[custom_data~{tv:5}] run return run title @s actionbar [{"text":"🕸 Filets : ","color":"white"},{"score":{"name":"@s","objective":"mg.tvnet"},"color":"yellow","bold":true}]
execute if items entity @s weapon.mainhand *[custom_data~{tv:6}] run return run title @s actionbar [{"text":"⚙ Pièges : ","color":"gray"},{"score":{"name":"@s","objective":"mg.tvtr"},"color":"yellow","bold":true},{"text":"  (clic droit : poser à tes pieds)","color":"gray"}]
execute if score @s mg.tvhm matches 1.. run return 0
function mg:terra/hud_main
