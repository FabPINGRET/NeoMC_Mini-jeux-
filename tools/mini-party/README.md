# Générateur de la carte Mini Party

`gen_board.py` produit l'île du plateau (terrain, chemins, cases, décor, panneaux) et les tables de jeu
(`place`, `next`, `next_fork`, `prev`, `case_type`, `is_fork`, `star_place`, `star_pick`, `fork_info`, `dice_show`)
dans `data/mg/function/party/`.

```
python gen_board.py ../../data/mg            # régénère les fonctions
python gen_board.py ../../data/mg apercu.png # + aperçu vu du ciel
```

Les chemins se règlent dans `SEG` (points de passage), les zones dans `zone()` et `H0()`, les proportions de cases dans `WEIGHTS`.
Le jeu lui-même (tours, dé, effets) est dans les autres fonctions de `party/`, écrites à la main.
