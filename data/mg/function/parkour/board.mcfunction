# Met à jour le panneau du record (macro : $(s), $(d))
$data modify entity @e[type=minecraft:text_display,tag=mg.pkboard,limit=1] text set value {text:"Record : $(s).$(d) s",color:"gold"}
