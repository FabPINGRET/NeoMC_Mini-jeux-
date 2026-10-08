"""Outil commun des scripts de branchement (wire_elyrace*.py) : un Patcher en deux phases. Phase 1 : chaque modification est
appliquee EN MEMOIRE, et chaque ancre est comptee sur le texte courant (EXACTEMENT une occurrence, sinon le script s'arrete
sur un message clair). Phase 2 : commit() ecrit tous les fichiers. Une ancre manquante n'ecrit donc jamais rien, meme
quand les modifications precedentes avaient reussi. Les fins de ligne de chaque fichier (CRLF ou LF) sont conservees.
Python stdlib uniquement (compatible 3.8).
"""
import json
import os


class Patcher:
    def __init__(self, root):
        self.root = root
        self.files = {}          # chemin -> [texte courant, fin de ligne]
        self.touched = []

    def path(self, *parts):
        return os.path.join(self.root, *parts)

    def fn_path(self, rel):
        return self.path('data', 'mg', 'function', rel + '.mcfunction')

    def _load(self, path):
        if path not in self.files:
            with open(path, encoding='utf-8', newline='') as fh:
                s = fh.read()
            self.files[path] = [s, '\r\n' if '\r\n' in s else '\n']
        return self.files[path]

    def text(self, path):
        """Texte courant (fins de ligne normalisees en \\n) et fin de ligne d'origine."""
        s, nl = self._load(path)
        return s.replace('\r\n', '\n'), nl

    def patch(self, path, old, new):
        """Remplace `old` par `new` (une seule occurrence exigee dans le texte courant)."""
        entry = self._load(path)
        s, nl = entry
        o, n = old.replace('\n', nl), new.replace('\n', nl)
        if s.count(o) != 1:
            raise SystemExit('ancre trouvee %d fois (1 attendue) dans %s : %s' % (s.count(o), path, old[:70]))
        entry[0] = s.replace(o, n)
        if path not in self.touched:
            self.touched.append(path)

    def after(self, path, anchor, add):
        """Ajoute `add` (des lignes completes) juste apres la ligne `anchor`."""
        self.patch(path, anchor + '\n', anchor + '\n' + add)

    def between(self, path, a, b, add):
        """Insere `add` (des lignes completes) entre le texte `a` et le texte `b`, qui doivent etre consecutifs (a + fin de ligne + b,
        une seule occurrence) : une 2e execution ne retrouve plus cette adjacence et s'arrete, au lieu d'inserer en double."""
        self.patch(path, a + '\n' + b, a + '\n' + add + b)

    def replace_line(self, path, prefix, new):
        """Remplace la ligne entiere qui commence par `prefix` (une seule ligne exigee) par `new` (sans fin de ligne)."""
        s, nl = self.text(path)
        lines = [l for l in s.split('\n') if l.startswith(prefix)]
        if len(lines) != 1:
            raise SystemExit("%d lignes commencent par '%s' dans %s (1 attendue)" % (len(lines), prefix[:60], path))
        self.patch(path, lines[0] + '\n', new + '\n')

    def patch_fn(self, rel, old, new):
        self.patch(self.fn_path(rel), old, new)

    def after_fn(self, rel, anchor, add):
        self.after(self.fn_path(rel), anchor, add)

    def edit_json(self, path, edit):
        """Charge un JSON mis en forme par json.dumps(indent=2), applique edit(d) et le remet en forme (refuse tout autre format)."""
        s, nl = self.text(path)
        d = json.loads(s)
        if json.dumps(d, ensure_ascii=False, indent=2) + '\n' != s:
            raise SystemExit('%s : mise en forme inattendue, la reecriture ne serait pas identique' % path)
        edit(d)
        self.files[path][0] = (json.dumps(d, ensure_ascii=False, indent=2) + '\n').replace('\n', nl)
        if path not in self.touched:
            self.touched.append(path)

    def commit(self):
        """Phase 2 : ecrit les fichiers modifies."""
        for path in self.touched:
            with open(path, 'w', encoding='utf-8', newline='') as fh:
                fh.write(self.files[path][0])
        return len(self.touched)
