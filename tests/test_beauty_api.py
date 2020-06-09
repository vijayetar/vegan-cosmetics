from vegan_cosmetics.search_with_api.beauty_api import beauty_api_call, making_vegan_makeup_list
import json
 
# def test_beauty_api_exists():
#     assert beauty_api_call()

def test_read_file():
    with open('./assets/beauty_api.json', 'r') as f:
        response = json.loads(f.read())
    # with open('./assets/test_beauty_api.json', 'w') as f:
    #     for item in response:
    #         f.write(str(item))
    # assert './assets/test_beauty_api.json'
    if response:
        actual = True
    expected = False
    assert actual == expected



# def test_