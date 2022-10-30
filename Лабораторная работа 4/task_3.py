def delete(list_, index=None):
    if len(list_) == 0:
        return 'Список пуст, удалять нечего'
    elif len(list_) == 1:
        if index == 0:
           return 'Вы удалили последний элемент списка'
        return 'В списке нет элемента с таким индексом'
    elif index is not None:
        if 0 <= index < len(list_):
            pre_list = list_[:index]
            post_list = list_[index+1:]
            pre_list.extend(post_list)
            return pre_list
        return 'В списке нет элемента с таким индексом'
    return list_

print(delete([0, 0, 1, 2], index=0))
print(delete([0, 1, 1, 2, 3], index=1))
print(delete([0, 1, 2, 3, 4, 4]))
