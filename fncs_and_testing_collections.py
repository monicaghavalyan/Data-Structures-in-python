import my_collections as cl
import my_online_shop as shop

def main():
    testing_hashset()
    #testing_hashmap()
    #testing_treeset()
    #testing_treemap()
    #testing_weighted_graph()
    #testing_weighted_directed_graph_treemap()
    #testing_min_priority_queue()

def testing_min_priority_queue():
    q = cl.MinPriorityQueue()
    q.enqueue(2)
    q.enqueue(4)
    q.enqueue(5)
    q.enqueue(7)
    q.enqueue(8)
    q.enqueue(9)
    q.enqueue(15)
    q.enqueue(11)
    q.enqueue(12)
    print('\nPrinting the queue')
    q.printt()
    print('\nPrinting the queue after dequeue')
    q.dequeue()
    q.printt()
    print('\nGetting the smallest (first or root) element in queue')
    print(q.front())
    
    print('\nPrinting the queue with inorder iteration')
    for i in q:
        print(i)

    print('\nTesting adding products to a queue and removing them according to the lowest price')
    online_shop = shop.MyOnlineShop('MyShop', 'address')
    online_shop.add_product_to_min_queue(product = shop.AudioBook(1, 2, 4, 'title', 'author', 'format', 'reader'))
    online_shop.add_product_to_min_queue(shop.AudioBook(2, 5, 10, 'title', 'author', 'format', 'reader'))
    online_shop.add_product_to_min_queue(shop.AudioBook(3, 7, 9, 'title', 'author', 'format', 'reader'))
    online_shop.add_product_to_min_queue(shop.PaperBook(4, 1, 6, "title", "author", "num_of_panges", "cover_type"))
    online_shop.add_product_to_min_queue(shop.PaperBook(5, 6, 2, "title", "author", "num_of_panges", "cover_type"))
    online_shop.add_product_to_min_queue(shop.AudioBook(6, 9, 4, 'title', 'author', 'format', 'reader'))
    online_shop.add_product_to_min_queue(shop.AudioBook(7, 11, 10, 'title', 'author', 'format', 'reader'))
    online_shop.add_product_to_min_queue(shop.AudioBook(8, 12, 9, 'title', 'author', 'format', 'reader'))
    online_shop.add_product_to_min_queue(shop.PaperBook(9, 0, 6, "title", "author", "num_of_panges", "cover_type"))
    online_shop.add_product_to_min_queue(shop.PaperBook(10, 3, 2, "title", "author", "num_of_panges", "cover_type"))
    online_shop.remove_product_from_min_queue()
    online_shop.remove_product_from_min_queue()
    online_shop.remove_product_from_min_queue()
    online_shop.remove_product_from_min_queue()
    online_shop.remove_product_from_min_queue()
    online_shop.remove_product_from_min_queue()
    online_shop.remove_product_from_min_queue()
    online_shop.remove_product_from_min_queue()
    online_shop.remove_product_from_min_queue()
    online_shop.remove_product_from_min_queue()

    print('\nTesting the function get_number_of_products_rated_higher')
    product_queue = cl.MinPriorityQueue()
    product_queue.enqueue(shop.AudioBook(1, 2, 4, 'title', 'author', 'format', 'reader'))
    product_queue.enqueue(shop.AudioBook(2, 5, 10, 'title', 'author', 'format', 'reader'))
    product_queue.enqueue(shop.AudioBook(3, 7, 9, 'title', 'author', 'format', 'reader'))
    product_queue.enqueue(shop.PaperBook(4, 3, 6, "title", "author", "num_of_panges", "cover_type"))
    product_queue.enqueue(shop.PaperBook(5, 1, 2, "title", "author", "num_of_panges", "cover_type"))
    print(product_queue.get_number_of_products_rating_higher(4))



def testing_weighted_graph():
    graph = cl.WeightedGraphMap()
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 7, 8)
    graph.add_edge(1, 2, 8)
    graph.add_edge(1, 7, 11)
    graph.add_edge(2, 3, 7)
    graph.add_edge(2, 5, 4)
    graph.add_edge(2, 8, 2)
    graph.add_edge(3, 4, 9)
    graph.add_edge(3, 5, 14)
    graph.add_edge(4, 5, 10)
    graph.add_edge(5, 6, 2)
    graph.add_edge(6, 7, 1)
    graph.add_edge(6, 8, 6)
    graph.add_edge(7, 8, 7)
    print('\nPrinting the graph as a dictionary')
    graph.printt()
    
    print('\nPrinting the shortest path starting from 0 as a dictionary')
    print(graph.dijkstra(0))
    
    print('\nPrinting the minimum spanning tree by kruskal')
    graph.kruskal().printt()
    
    print('\nPrinting the minimum spanning tree by prim')
    graph.prim(0).printt()
    
    print('\nPrinting the the shortest paths by floyd warshall')
    print(graph.floyd_warshall())
    

def testing_weighted_directed_graph_treemap():
    graph = cl.WeightedDirectedGraphAdjMap()
    graph.add_edge(0, 1, 4)
    graph.add_edge(0, 7, 8)
    graph.add_edge(1, 2, 8)
    graph.add_edge(1, 7, 11)
    graph.add_edge(2, 3, 7)
    graph.add_edge(2, 5, 4)
    graph.add_edge(2, 8, 2)
    graph.add_edge(3, 4, 9)
    graph.add_edge(3, 5, 14)
    graph.add_edge(4, 5, 10)
    graph.add_edge(5, 6, 2)
    graph.add_edge(6, 7, 1)
    graph.add_edge(6, 8, 6)
    graph.add_edge(7, 8, 7)
    print('\nPrinting a directed graph as a dictionary (treemap is used)')
    graph.printt()
    
    print('\nPrinting the shortest path starting from 0 as a dictionary (treemap is used) with dijkstra')
    graph.shortest_path(0).print_for_graphs()
    
    print('\nPrinting the shortest path starting from 0 as a dictionary (treemap is used) with bellman ford')
    print(graph.bellman_ford(0))


def testing_treeset():
    treeset = cl.TreeSet()
    
    print('Inserting 10')
    treeset.add(10)
    treeset.printt()
    print('----------------------')
    
    print('Inserting 20')
    treeset.add(20)
    treeset.printt()
    print('----------------------')

    print('Inserting 8')
    treeset.add(8)
    treeset.printt()
    print('----------------------')
    
    print('Inserting 30')
    treeset.add(30)
    treeset.printt()
    print('----------------------')
    
    print('Inserting 15')
    treeset.add(15)
    treeset.printt()
    print('----------------------')
    
    print('Inserting 14')
    treeset.add(14)
    treeset.printt()
    print('----------------------')
    
    print('Inserting 14 again (nothing changes)')
    treeset.add(14)
    treeset.printt()
    print('----------------------')

    print('Removing 15')
    treeset.remove(15)
    treeset.printt()
    print('----------------------')

    print('Removing 10')
    treeset.remove(10)
    treeset.printt()
    print('----------------------')
    
    print('Inserting 35')
    treeset.add(35)
    treeset.printt()
    print('----------------------')
    
    print('Inserting 37')
    treeset.add(37)
    treeset.printt()
    print('----------------------')
    
    print('Printing with inorder traversal')
    for i in treeset:
        print(i)
    print('\n')
    
    print('Printing the element at index 3')
    print(treeset.get_element_at(3), '\n')
    
    print('Printing the element at index 8 which does not exist')
    print(treeset.get_element_at(8), '\n')
    
    print('Checking if the set contains 20')
    print(treeset.contains(20), '\n')
    
    print('Checking if the set contains 10')
    print(treeset.contains(10), '\n')
    
    print('Checking if the set is equal to {8,14,20,37,35,30}')
    print(treeset.equals({8,14,20,37,35,30}), '\n')
    
    print('Checking if the set is equal to {8,14,20,37,35,40}')
    print(treeset.equals({8,14,20,37,35,40}), '\n')


def testing_treemap():
    treemap = cl.TreeMap()
    
    print('Inserting 10')
    treemap.put(10, 'A')
    treemap.printt()
    print('----------------------')
    
    print('Inserting 20')
    treemap.put(20, 'B')
    treemap.printt()
    print('----------------------')

    print('Inserting 8')
    treemap.put(8, 'C')
    treemap.printt()
    print('----------------------')
    
    print('Inserting 30')
    treemap.put(30, 'D')
    treemap.printt()
    print('----------------------')
    
    print('Inserting 15')
    treemap.put(15, 'E')
    treemap.printt()
    print('----------------------')
    
    print('Inserting 14')
    treemap.put(14, 'F')
    treemap.printt()
    print('----------------------')
    
    print('Inserting 14 again (the value changes)')
    treemap.put(14, 'G')
    treemap.printt()
    print('----------------------')

    print('Removing 15')
    treemap.remove(15)
    treemap.printt()
    print('----------------------')

    print('Removing 10')
    treemap.remove(10)
    treemap.printt()
    print('----------------------')
    
    print('Inserting 35')
    treemap.put(35, 'H')
    treemap.printt()
    print('----------------------')
    
    print('Inserting 37')
    treemap.put(37, 'I')
    treemap.printt()
    print('----------------------')
    
    print('Printing with inorder traversal')
    for entry in treemap:
        print(entry._key, entry._value)
    print('\n')
    
    print('Getting the value at key 20')
    print(treemap.get(20), '\n')
    
    print('Getting the value at key 4 which does not exist')
    print(treemap.get(4), '\n')

    print('Getting all the keys as a treeset')
    for i in treemap.key_set():
        print(i)
    print('\n')
    
    print('Getting the submap in the interval (20, 35)')
    for i in treemap.sub_map(20, 35):
        print(i._key)
    print('\n')

    print('Checking if the tree is complete')
    print(treemap.is_tree_complete())
    print('\n')

    print('Checking if the tree is complete after inserting 7 (it should be complete)')
    treemap.put(7, 'X')
    print(treemap.is_tree_complete())
    print('\n')

    print('Checking if the tree is complete after inserting 6 (it should be complete)')
    treemap.put(6, 'X')
    treemap.printt()
    print(treemap.is_tree_complete())
    print('\n')

    print('Checking if the tree is complete after removing 37 (it should not be complete)')
    treemap.remove(37)
    treemap.printt()
    print(treemap.is_tree_complete())
    print('\n')
    
    print('Checking if the tree is left-skewed')
    print(treemap.is_tree_left_skewed())
    print('\n')
    
    print('Checking if the tree is left-skewed after adding only 2 node')
    new_treemap = cl.TreeMap()
    new_treemap.put(2, 'A')
    new_treemap.put(1, 'B')
    print(new_treemap.is_tree_left_skewed())
    print('\n')
    
    print('Getting the set of unique values in the map')
    for i in treemap.get_set_of_unique_values():
        print(i)
    
    print('Adding 37, 39, 36, 15')
    treemap.add(37)
    treemap.add(39)
    treemap.add(36)
    treemap.add(15)
    treemap.printt()
    print('\n')

    print('Tree with preorder iteration')
    preorder = treemap.preorder_iter()
    while True:
        try:
            el = next(preorder)
            print(el)
        except StopIteration:
            break
    print('\n')

    print('Tree with preorder reverse iteration')
    preorder_rev = treemap.preorder_reverse_iter()
    while True:
        try:
            el = next(preorder_rev)
            print(el)
        except StopIteration:
            break
    print('\n')
    
    print('Tree with preorder iteration only odd positions')
    preorder_odd = treemap.preorder_odd_iter()
    while True:
        try:
            el = next(preorder_odd)
            print(el)
        except StopIteration:
            break
    print('\n')

    print('Tree with postorder iteration')
    preorder = treemap.postorder_iter()
    while True:
        try:
            el = next(preorder)
            print(el)
        except StopIteration:
            break
    print('\n')
    
    print('Tree with postorder reverse iteration')
    postorder_rev = treemap.postorder_reverse_iter()
    while True:
        try:
            el = next(postorder_rev)
            print(el)
        except StopIteration:
            break
    print('\n')
    
    print('Tree with inorder iteration')
    inorder = treemap.inorder_iter()
    while True:
        try:
            el = next(inorder)
            print(el)
        except StopIteration:
            break
    print('\n')

    print('Tree with inorder reverse iteration')
    inorder_rev = treemap.inorder_reverse_iter()
    while True:
        try:
            el = next(inorder_rev)
            print(el)
        except StopIteration:
            break
    print('\n')
    
    print('Getting the smallest key greater than 37')
    print(treemap.higher_entry(37), '\n')
    
    print('Tree with inorder index iterator')
    inorder_index_iter = treemap.inorder_index_entry_iter(5)
    while True:
        try:
            el = next(inorder_index_iter)
            print(el)
        except StopIteration:
            break
    print('\n')
    

def testing_hashset_products_iter():
    hash_set = cl.HashSet()
    hash_set.add(shop.AudioBook(1, 2, 4, 'title', 'author', 'format', 'reader'))
    hash_set.add(shop.AudioBook(4, 5, 10, 'title', 'author', 'format', 'reader'))
    hash_set.add(shop.AudioBook(6, 7, 9, 'title', 'author', 'format', 'reader'))
    hash_set.add(shop.PaperBook(8, "price", 6, "title", "author", "num_of_panges", "cover_type"))
    hash_set.add(shop.PaperBook(9, "price", 2, "title", "author", "num_of_panges", "cover_type"))
    it = hash_set.product_type_iterator(shop.ProductType.AudioBook)
    while True:
        try:
            el = next(it)
            print(el._id)
        except StopIteration:
            break       


def testing_hashset():
    hash_set = cl.HashSet()
    hash_set.add('arrow')
    hash_set.add('arm')
    hash_set.add('Dog')
    hash_set.add('bed')
    hash_set.add('Armenia')
    hash_set.add('arev')
    hash_set.add('amp')
    hash_set.add('bak')
    hash_set.add('buys')
    hash_set.add('barev')
    hash_set.add('desk')
    hash_set.add('door')

    print('Testing the iterator')
    for i in hash_set:
        print(i)
    print('-'*10)
    
    print('\nChecking if element dog exists')
    print(hash_set.contains('Dog'))
    
    print('\nRemoving element Dog')
    hash_set.remove('Dog')
    hash_set.printt()
    
    print('Checking if element dog exists after removal')
    print(hash_set.contains('Dog'))

    print('\nTrying to remove the element after Dog which does not exist')
    hash_set.remove_after('Dog')
    hash_set.printt()
    print('Nothing changed')
    
    print('\nTrying to remove the element after arm')
    hash_set.remove_after('arm')
    hash_set.printt()
    print('Armenia was removed')
    
    print('\nTrying to remove the element after barev')
    hash_set.remove_after('barev')
    hash_set.printt()
    print('desk was removed')
    
    print('\nTrying to get an element at non-existing index')
    print(hash_set.get_element_at(50))
    
    print('\nTrying to get an element at 0 index')
    print(hash_set.get_element_at(0))

    print('\nTrying to get an element at last index')
    print(hash_set.get_element_at(hash_set.get_size()-1))  
    
    set1 = {'amp', 'arrow', 'arm', 'arev', 'bed', 'bak', 'buys', 'barev', 'door'}
    print(f'\nChecking if the set {set1} is equal to our set')
    print(hash_set.equals(set1))
    
    set2 = {'arrow', 'arm', 'arev', 'bed', 'bak', 'buys', 'barev', 'door'}
    print(f'\nChecking if the set {set2} is equal to our set (which is not equal)')
    print(hash_set.equals(set2))
    
    print('\nGetting intersection of 2 sets')
    hash_set2 = cl.HashSet()
    hash_set2.add('arrow')
    hash_set2.add('door')
    hash_set2.add('bed')
    print('Set 1: ')
    hash_set.printt()
    print('Set 2: ')
    hash_set2.printt()
    print('Intersection: ')
    hash_set.keep_all(hash_set2)
    hash_set.printt()


def testing_hashmap():
    hash_map = cl.HashMap()
    hash_map.put('Monica', 1)
    hash_map.put('Zara', 2)
    hash_map.put('Aram', 3)
    hash_map.put('Anna', 4)
    hash_map.put('Mane', 5)
    hash_map.put('Zvart', 6)
    hash_map.put('Alla', 7)
    hash_map.put('Marine', 8)
    hash_map.put('Alina', 9)

    print('Trying to add an Entry which already exists but with another value')
    print(hash_map.put('Alina', 10))
    print('The value of key Alina is changed to 10')
    print(hash_map.get('Alina'))

    print('\nPrinting all keys in the map')
    col_iter = hash_map.key_iter()
    while True:
        try:
            el = next(col_iter)
            print(el)
        except StopIteration:
            break
    print('-'*10)

    print('\nGetting the value of key Zvart')
    print(hash_map.get('Zvart'))
    
    print('\nRemoving the element with key Zvart and getting the value of that element')
    print(hash_map.remove('Zvart'))
    print('Zvart is removed')
    
    print('\nGetting the keys of the map as a set')
    sett = hash_map.key_set()
    sett.printt()
    
    print('\nPrinting all keys')
    key_iter = hash_map.key_iter()
    while True:
        try:
            el = next(key_iter)
            print(el)
        except StopIteration:
            break
    print('-'*10)
 
    print('\nPrinting all keys at odd positions')
    odd_key_iter = hash_map.odd_key_iter()
    while True:
        try:
            el = next(odd_key_iter)
            print(el)
        except StopIteration:
            break
    print('-'*10)


def testing_queue():
    queue = cl.DoubleLinkedListDeque()
    queue.add(1)
    queue.add(2)
    print('The initial queue')
    queue.printt()
    print('-'*10)

    print('Enqueue 3')
    queue.enqueue(3)
    queue.printt()
    print('-'*10)

    print('Dequeue')
    queue.dequeue()
    queue.printt()
    print('-'*10)

    print('Enqueue 0 from the left')
    queue.left_enqueue(0)
    queue.printt()
    print('-'*10)

    print('Dequeue from the right')
    queue.right_dequeue()
    queue.printt()
    print('-'*10)

    print('Swap 0 and 2')
    queue.swap(0, 2)
    queue.printt()
    print('-'*10)

    print('Swap when the elements are not present e.g. (1,2)')
    queue.swap(1, 2)
    queue.printt()
    print('Nothing changed')
    print('-'*10)

    print('Swap elements which are present more than once')
    queue.add(2)
    queue.add(2)
    queue.add(0)
    print('The initial queue')
    queue.printt()
    print('Queue after swaping 0 and 2')
    queue.swap(0, 2)
    queue.printt()
    print('-'*10)

    queue.add(5)
    queue.add(6)
    queue.add(7)
    queue.add(8)
    queue.add(9)
    print('Trying to enque 10 when the deque is full (in case of array queue)')
    print('Deque before enqueueing')
    queue.printt()
    print('Deque after enqueueing')
    queue.enqueue(10)
    queue.printt()
    print('Nothing changes in case of array deque but in case of linked list queue the element is being added')
    print('-'*10)
    
    print('Testing the position iterator with step 3 (that is the default in the function which can be changed)')
    for i in queue(2):
        print(i)
        

def testing_list():
    listt = cl.LinkedList()
    listt.add(1)
    listt.add(2)
    listt.add(3)
    listt.add(4)
    listt.add(5)
    listt.add(6)
    listt.add(7)
    listt.add(8)
    listt.add(9)
    listt.add(10)
    listt.add(11)
    listt.add(12)
    listt.add(13)
    listt.swap(2, 4)
    listt.right_dequeue()
    listt.remove_last()
    listt.remove_last()
    listt.remove_last()
    listt.remove_last()
    listt.remove_first()
    listt.printt(listt)
    reverse_list(listt)

def reverse_list(listt):
    if listt.is_empty() or listt.get_size() == 1:
        return
    last = listt.last()
    listt.remove_last()
    reverse_list(listt)
    listt.add_first(last)
    
def reverse_queue(queue):
    if queue.is_empty() or queue.get_size() == 1:
        return
    first = queue.dequeue()
    reverse_queue(queue)
    queue.enqueue(first)
    

if __name__ == "__main__":
    main()
