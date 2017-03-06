'''This function takes a list of strings and returns
 a single string that is an unordered list
 (<ul>...</ul>) of those strings. '''

def unordered_list(strings):
   list = '<ul>'

   for s in strings:
       list += '<li>%s</li>' % s

   list += '</ul>'
        
   return list;

# Test Cases
print unordered_list("code")

print unordered_list(" ")

print unordered_list("@#$")

print unordered_list("Supercalifragilisticexpialidocious")
