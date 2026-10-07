# Nouveau meneur d'un classement ? (@s) — fige « libellé / pseudo — score » dans le hall — macro
$execute unless score #top $(obj) matches 0.. run scoreboard players set #top $(obj) 0
$execute unless score @s $(obj) > #top $(obj) run return 0
$scoreboard players operation #top $(obj) = @s $(obj)
$item modify entity @e[type=minecraft:item_display,tag=mg.hallbuf,limit=1] contents {function:"minecraft:set_name",entity:"this",target:"custom_name",name:[{text:"$(lbl)",color:"$(col)",bold:true},{text:"\n",bold:false},{selector:"@s",color:"white",bold:false},{text:" — ",color:"gray",bold:false},{score:{name:"@s",objective:"$(obj)"},color:"gold",bold:false},{text:"$(unit)",color:"gray",bold:false}]}
$data modify storage mg:hall e.$(key) set from entity @e[type=minecraft:item_display,tag=mg.hallbuf,limit=1] item.components."minecraft:custom_name"
$data modify entity @e[type=minecraft:text_display,tag=mg.h_$(key),limit=1] text set from storage mg:hall e.$(key)
