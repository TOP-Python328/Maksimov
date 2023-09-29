def tree_leaves(leaves) -> int:
    """Функция которая считает количество листьев на дереве"""
    q = leaves[:]
    count = 0
    while q:
        entry = q.pop()
        if isinstance(entry, list):
            q += entry
        if entry == 'leaf': count += 1
    return count
        
# >>> tree = [[[['leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf', 'leaf'], 'leaf', 'leaf'], ['leaf', 'leaf', 'leaf']], [['leaf', 'leaf'], ['leaf', 'leaf', 'leaf', 'leaf', 'leaf', 'leaf'], 'leaf', 'leaf', 'leaf'], [['leaf'], ['leaf', 'leaf', ['leaf', 'leaf', 'leaf']], 'leaf', 'leaf'], ['leaf', 'leaf', ['leaf', 'leaf'], 'leaf']]
# >>>
# >>> tree_leaves(tree)
# 38