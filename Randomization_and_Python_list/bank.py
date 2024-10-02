all_users = ["John", "Luke", "Matthew"]


def register_user(name, id):
    all_users.append(name)
    return all_users


def delete_user(name):
    all_users.remove(name)


def total_user():
    return len(all_users)
