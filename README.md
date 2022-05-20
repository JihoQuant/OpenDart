# OpenDart

전자공시 OPEN DART API Library

[![opendart](https://opendart.fss.or.kr/images/logo.png)](https://opendart.fss.or.kr)
[![github](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/JihoQuant/OpenDart)

## Overview

해당 라이브러리는 OPEN DART 스펙에 맞춰 쉽게 사용할 수 있도록 구성하고 있습니다.
이 라이브러리를 통해 투자를 하는 경우 ***책임은 사용자에게 있습니다***.

사용을 위해서는 직접 Open Dart 시스템에서 API KEY를 발급받아 세팅을 해주어야 합니다.
또한 도메인 지식이 미천하여 제가 모르는 내용은 추가하지 않았으며, 도중에 그만둘 수도 있습니다.

***하지만 만족하는 결과가 나올 때까지는 최선을 다하겠습니다.***

## Get Started

```bash
pip install opendart
```

### ⚠️ WARNING ⚠️

해당 라이브러리를 사용하기 위해서는 `python-dotenv` 라이브러리 사용이 필요합니다.
프로젝트 루트 위치에 다음과 같이 `.env` 파일을 생성하고,
발급받은 `DART_API_KEY`를 입력해야 합니다.

이미 사용중인 `.env` 파일이 있다면 추가해야 합니다.
자세한 사용법은 [pypi.org](https://github.com/theskumar/python-dotenv) 혹은
[github](https://github.com/theskumar/python-dotenv)을 참고바랍니다.

```env
DART_API_KEY = '발급받은 API KEY'
```

## Usage

```python
from typing import List, TYPE_CHECKING

from opendart import api, utils

if TYPE_CHECKING:
    from opendart.models.public_notice import Corporation


FILE_PATH = 'listed_corps'
listed_corps: List['Corporation']
'''종목코드가 발급된 상장사 목록'''

try:
    listed_corps: List['Corporation'] = utils.read_json_by_file_path(FILE_PATH)
except:
    listed_corps: List['Corporation'] = api.fetch_all_listed_corp()
    utils.save_json_as_file(listed_corps, FILE_PATH)
```
