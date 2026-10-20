# (@s = victime, appelée par `if function`) : 1 si son dernier attaquant est le porteur de mg.tmsh, sinon 0
execute on attacker if entity @s[tag=mg.tmsh] run return 1
return 0
