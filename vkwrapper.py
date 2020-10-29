import requests
from photo import Photo
from requests.exceptions import HTTPError


class VkWrapper:
    uri: str = 'https://api.vk.com/method/photos.getAll?v=5.52&access_token='

    def __init__(self, key):
        self.key = key
        self.uri = VkWrapper.uri + str(key)

    def _photo_creator(self):
        """
        :return:
        Оставляем в списке только фотографию наилучшего качества
        """
        res = self._get_photos_info()
        photos_list: list = []
        for r in res:
            self._max_photo_size_searcher(r)
            photos_list.append(
                Photo(r['album_id'], r['date'], r['id'], r['owner_id'], r['image'])
            )
        return photos_list

    @staticmethod
    def _max_photo_size_searcher(r):
        """
        Определяем максимальное разрешение фотографии из возможных вариантов, для записи в БД
        """
        word_list = []
        for key in r:
            if 'photo' in key:
                word_list += key.split('_')
        num_list = [int(num) for num in filter(lambda num: num.isnumeric(), word_list)]
        bigest_photo_size = max(num_list)
        response = requests.get(r['photo_' + str(bigest_photo_size)])
        r['image'] = response.content
        return r

    def get_photo(self):
        return self._photo_creator()

    def _get_photos_info(self):
        """
        Получаем список фотографий
        return
        Отдаем список словарей с фотками из ВК АПИ
        """
        try:
            response = requests.get(self.uri)
            response.raise_for_status()
            res: dict = response.json()
        except HTTPError as http_err:
            print(f"Error + {http_err}")
        except Exception as err:
            print(f"Error + {err}")
        else:
            print('Success!' + str(response.status_code))
            return res['response']['items']
