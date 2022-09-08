# Git Cheatsheet


Setting local branch to exactly match remote.

```bash
git fetch origin
git reset --hard origin/<branch>
```

If you need to save your work beforehand:

```bash
git commit -a -m "saving my work incase"
git branch saved-work-xyz
```


