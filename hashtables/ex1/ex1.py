#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable,
                        hash_table_insert,
                        hash_table_remove,
                        hash_table_retrieve,
                        hash_table_resize)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)
    for weight in weights:
        key = weight
        value = limit - weight
        hash_table_insert(ht, key, value)

    for i in range(0, len(weights)):
        value_1 = None
        value_2 = None
        answer = None
        key = hash_table_retrieve(ht, weights[i])
        check = hash_table_retrieve(ht, key)
        if check is not None:
            if i > weights.index(key):
                value_1 = i
                value_2 = weights.index(key)
            else:
                value_1 = weights.index(key)
                value_2 = i
            break
            
    if value_1 is not None:
        answer = [value_1, value_2]

    return answer


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")

weights_2 = [4, 6, 10, 15, 16]
answer_2 = get_indices_of_item_weights(weights_2, 5, 21)
print(answer_2)