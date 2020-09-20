import json
import os


class Photo:
    def __init__(self, album_id, date, id, owner_id, image):
        self.album_id = album_id
        self.date = date
        self.id = id
        self.owner_id = owner_id
        self.image = image


    def __str__(self):
        return json.dumps({
            'album_id': self.album_id,
            'date': self.date,
            'id': self.id,
            'owner_id': self.owner_id,
            'image': self.image
            })

    def to_dictionary(self):
        return {
            'album_id': self.album_id,
            'date': self.date,
            'id': self.id,
            'owner_id': self.owner_id,
            'image': self.image
            }

    @staticmethod
    def create_photo(folders):
        """
        Функция создания фоток и файлов
        :return:
        папки созданы локально в проекте.
        """
        path: str = './photos'
        for f in folders:
            name: str = ('album' + str(f[0]))
            fullpath = os.path.join(path, name)
            if not os.path.exists(fullpath):
                os.makedirs(fullpath)

