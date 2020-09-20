
def create_local_copy_photo(res):
    """
    фунция создания файлов локально, с фотографиями
    :return:
    файлы созданы как результат выполнения функции
    """
    for r in res:
        path: str = './photos/' + 'album' + str(r[0]) + '/photo' + str(r[1]) + '.jpeg'
        with open(path, 'wb') as file:
            file.write(r[2])
