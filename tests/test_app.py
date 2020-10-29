from unittest import TestCase, mock
from db import DBWrapper
from vkwrapper import VkWrapper
from photo import Photo


class TestGetphotos(TestCase):
    @mock.patch('vkwrapper.requests.get')
    def setUp(self, mock):
        self.test_db_wrapper = DBWrapper()
        self.test_vk_wrapper = VkWrapper('key')
        mock.return_value.json.return_value = {
            'response':
                {'items':
                    [
                        {
                            'album_id': 272606173,
                            'date': 1590994322,
                            'id': 457239044,
                            'owner_id': 446973528,
                            'has_tags': False,
                            'height': 221,
                            'photo_130': 'https://sun9-13.userapi.com/c855736/v855736967/23f76c/fZE39u9CU-M.jpg',
                            'photo_604': 'https://sun9-40.userapi.com/c855736/v855736967/23f76d/9oH9coD44y4.jpg',
                            'photo_75': 'https://sun9-63.userapi.com/c855736/v855736967/23f76b/eMTpZP3V3kU.jpg',
                            'text': '',
                            'width': 576
                        }
                    ]
                }
        }
        self.photos_list = self.test_vk_wrapper.get_photo()
        # self.photos_list[0].image = b'\x00\x00\x00\x00\x00'

    def test_app(self):
        test_warehouse = DBWrapper()
        test_warehouse.insert_data_to_db(self.photos_list)
        expected_result = [(272606173, )]

        self.assertEquals(test_warehouse.select_data_from_db('../db/select_albums.sql'), expected_result)

