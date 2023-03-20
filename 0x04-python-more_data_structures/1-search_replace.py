#!/usr/bin/python3
def search_replace(my_list, search, replace):
    def s_r_elm(elm):
        return (elm if elm != search else replace)
    return list(map(s_r_elm, my_list))

# or simply
#return[replace if x == search else x for x in my_list]

# the logic is shown below

#   def search_replace(my_list, search, replace):

#      new_list = []

#      for elem in my_list:
#          if elem == search:
#              elem = replace
#          new_list.append(elem)
#      return new_list
