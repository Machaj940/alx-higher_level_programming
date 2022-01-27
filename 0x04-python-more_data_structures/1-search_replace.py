#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def s_r_elm(elm):
        return (elm if elm != search else replace)
    return list(map(s_r_elm, my_list))

# or simply
#return[replace if x == search else x for x in my_list]
