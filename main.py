from db import DBWrapper
from vkwrapper import VkWrapper
from setup import VK_TOKKEN

from photo import Photo
from photo_export import create_local_copy_photo

if __name__ == '__main__':
    myvkphotos = VkWrapper(VK_TOKKEN)
    photos_list = myvkphotos.get_photo()
    photo_warehouse = DBWrapper()
    photo_warehouse.insert_data_to_db(photos_list)
    Photo.create_photo(photo_warehouse.select_data_from_db('./db/select_albums.sql'))
    photos = photo_warehouse.select_data_from_db('./db/select_photos.sql')
    create_local_copy_photo(photos)
