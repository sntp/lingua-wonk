import requests


USER_DICT_URL = "http://lingualeo.com/userdict/json"
LOGIN_URL = "http://api.lingualeo.com/api/login"

s = requests.Session()


def __check_status_is_ok(r):
    if r.status_code != 200:
        raise Exception('Response status is not 200 (%d, %s)' % (r.status_code, r.url))


def __check_response_for_error(data):
    if len(data['error_msg']) != 0:
        raise Exception(data['error_msg'])


def auth(email, password):
    r = s.post(LOGIN_URL, data={'email': email.strip(), 'password': password.strip()})
    __check_status_is_ok(r)
    data = r.json()
    __check_response_for_error(data)
    return data


def user_dict(sort_by="date", word_type="0", filter_="all", page="1", group_id="dictionary"):
    param = {
        "sortBy": sort_by,
        "wordType": word_type,
        "filter": filter_,
        "page": page,
        "groupId": group_id
    }
    r = s.post(USER_DICT_URL, data=param, headers={'X-Requested-With': 'XMLHttpRequest'})
    __check_status_is_ok(r)
    data = r.json()
    __check_response_for_error(data)
    return data

