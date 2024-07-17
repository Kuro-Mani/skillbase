#usernames=[]
#def get_formatted_name(first_name,last_name):
#    full_name = f"{first_name}{last_name}"
#    return full_name.title()
#while True:
#    print("\n名前教えて")
#    lname=input("last_name")
#    if lname=='exit':
#        break
#    fname=input("first_name")
#    if fname=='exit':
#        break
#    formatted_name=get_formatted_name(fname,lname)
#    usernames.append(formatted_name.title())
#    print(f"\n{formatted_name}")

#def greet_users(names):
#    for name in names:
#        msg = f"{name.title()}"
#        print(msg)
#greet_users(usernames)
#uncheck_items=[]
#passed_items=[]
#while True:
#    items=input("put your items:::")
#    if items=='exit':
#        break
#    uncheck_items.append(items)
#def checkmodels(uncheck_items,passed_items):
#    while uncheck_items:
#        current_item = uncheck_items.pop()
#        print(f"{current_item}")
#        passed_items.append(current_item)
#def completed_item(passed_items):
#    for passed_item in passed_items:
#        print(passed_item)
#checkmodels(uncheck_items,passed_items)
#completed_item(passed_items)
# msg
#message=["hello","come on","good bye","how are you","be quiet"]
#get_message=[]
#for send_message in message:
#    print(f"send   {send_message}")
#    get_message.append(send_message)
#for get_messages in get_message:
#    print(f"get   {get_messages}")
# 位置引数
#def make_sand(size,*toppings):
#    print(f"\n{size}inch")
#    for topping in toppings:
#        print(f"- {topping}")
#make_sand('S','egg','ham')
#make_sand('L','salada','tomato')
# 可変引数
def build_profile(first,last,blood,age,**info):
    info['first_name']=first
    info['last_name']=last
    info['blood_type']=blood
    info['age']=age
    return info
while True:
    user=input("firstname:")
    info['first_name'].append==(user)
    if user=='exit':
        break
print(user)