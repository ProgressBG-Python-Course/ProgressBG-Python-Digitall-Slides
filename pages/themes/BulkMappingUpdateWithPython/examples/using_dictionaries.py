user_roles = {'Alice': 'user', 'Bob': 'admin', 'Charlie': 'user'}
update_roles = {'Alice': 'admin', 'Charlie': 'moderator'}

user_roles.update(update_roles)

print(user_roles)
