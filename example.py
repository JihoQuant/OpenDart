from typing import List, TYPE_CHECKING

from opendart import api, utils

if TYPE_CHECKING:
    from opendart.models.public_notice import Corporation


FILE_NAME = 'listed_corps'
listed_corps: List['Corporation']
'''종목코드가 발급된 상장사 목록'''

try:
    listed_corps: List['Corporation'] = utils.read_json_by_file_path(FILE_NAME)
except:
    listed_corps: List['Corporation'] = api.fetch_all_listed_corp()
    utils.save_json_as_file(listed_corps, FILE_NAME)
