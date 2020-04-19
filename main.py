from getting_compared_data.compared_data_to_user import *
if __name__ == '__main__':
    try:
        class_compared.finally_get_it()
        class_compared.writing_data_to_db()
        class_compared.getting_ids_data()
    except Exception as error:
        print(error)
