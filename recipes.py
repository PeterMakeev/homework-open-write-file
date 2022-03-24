from pprint import pprint


def file_reader(file_name, mode, encoding):
    with open (file_name, mode, encoding=encoding) as file:
        cook_book ={} 
        for dish in file:
            dish= dish.strip()            
            cook_book.update({dish: []})
            quantity_dishes = int(file.readline().strip())
            for i in range(quantity_dishes):
                list_products = file.readline().strip().split(' | ')                
                dict_products = {'ingredient_name': list_products[0], 'quantity': list_products[1], 'measure': list_products[2]}
                cook_book[dish].append(dict_products)
            file.readline()   
        
    return cook_book      
        


def get_shop_list_by_dishes(dishes, cook_book, person_count):
    dict_products = {}
    for name in cook_book.keys():        
        for dish in dishes:        
            if name == dish:
                for dict_ing in cook_book[name]:                    
                    products_name = dict_ing['ingredient_name']                    

                    try:
                        dict_products[products_name]['quantity'] += (int(dict_ing['quantity']) * person_count)
                    except:
                        dict_products[products_name] = {'measure': dict_ing['measure'],
                                              'quantity': int(dict_ing['quantity']) * person_count}
                            
    return dict_products


def file_open(file_name_1, file_name_2, file_name_3,file_name_4, encoding):
    with open (file_name_1, 'r', encoding=encoding) as file_1, \
         open (file_name_2, 'r', encoding=encoding) as file_2, \
         open (file_name_3, 'r', encoding=encoding) as file_3, \
         open (file_name_4, 'w', encoding=encoding) as file_4:               

        lines_1 = file_1.readlines()        
        count_1 = 0
        dict_1 = {}
        for line in lines_1:
            count_1 += 1            
            dict_1[file_name_1] = [count_1,lines_1] 

        lines_2 = file_2.readlines()        
        count_2 = 0
        dict_2 = {}
        for line in lines_2:
            count_2 += 1            
            dict_2[file_name_2] = [count_2,lines_2]

        lines_3 = file_3.readlines()        
        count_3 = 0
        dict_3 = {}
        for line in lines_3:
            count_3 += 1            
            dict_3[file_name_3] = [count_3,lines_3]
        dict_1.update(dict_2)
        dict_1.update(dict_3)          
        for i in sorted (dict_1.items(), key=lambda x: x[1]):          
            file_4.write(f'''\n{i[0]}\n{i[1][0]}\n{''.join(map(str, i[1][1]))}''')
    return         

print('Задача №1')
print(file_reader('recipes.txt','rt','utf-8'))
print('-------')
print('Задача №2')
pprint(get_shop_list_by_dishes(['Омлет', 'Омлет'], file_reader('recipes.txt','rt','utf-8'), 2))
print('-------')
print('Задача №3')
print(file_open('1.txt','2.txt', '3.txt','sorted_text.txt','utf-8'))


