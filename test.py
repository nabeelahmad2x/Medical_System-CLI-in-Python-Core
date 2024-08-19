import bcrypt

#saved_password = '$2b$12$omt5IEFspinynfLmF1mMYubB7WSkPVTlv2UPttGR.0S5D4J2i5XZe'



# print(password)
# print(type(password))

salt = bcrypt.gensalt()
#salt.encode()
print(salt)
passwo = 'admin123'

saved_hashed_password = bcrypt.hashpw(passwo.encode(), salt)
# new_hashed_password = bcrypt.hashpw(password.encode(), salt)
# wrong_hashed_password = bcrypt.hashpw(wrong_password, salt)



# print(saved_password)
print(saved_hashed_password)
# if saved_hashed_password == saved_password:
#     print("ok")
# else:
#     print("no")
# print(type(saved_hashed_password))


# key = saved_hashed_password[:29]
# print(key)
# print(type(key))
# new_pass = 'helloworld123'
# new_hashed_pass = bcrypt.hashpw(new_pass.encode(), key)
# print(new_hashed_pass)


# if saved_hashed_password == new_hashed_pass:
#     print("Ok")
# if hashed_password == new_hashed_password:
#     print(password)
#     print(hashed_password)
# else:
#     print('no')

# if hashed_password == wrong_hashed_password:
#     print('ok')
# else:
#     print('no')


# print(hashed_password)

# if bcrypt.checkpw(wrong_password, hashed_password):
#     print('wrong')
# elif bcrypt.checkpw(password, hashed_password):
#     print('yup')
# else:
#     print('no')
