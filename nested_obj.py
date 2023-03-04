def get_value_from_nested_object(obj, key):
    
    key_parts = key.split('/')
    
    value = obj
    for part in key_parts:
        value = value[part]

    return value

#example : Use the above function
object = {"x":{"y":{"z":"a"}}}
key = 'x/y/z'
value = get_value_from_nested_object(object, key)
print(value)  # It will give the Output: a
