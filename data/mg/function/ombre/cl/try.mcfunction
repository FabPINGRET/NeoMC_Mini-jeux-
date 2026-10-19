# @s : compétence $(c)/$(s) : recharge, mana, puis effet
$execute if score @s mg.olc$(s) matches 1.. run return run function mg:ombre/cl/wait {s:$(s)}
$function mg:ombre/cl/cost_$(c)$(s)
