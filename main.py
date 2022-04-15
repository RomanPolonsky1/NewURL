import  uuid

urls = [
    {
        "id": 1,
        "website_original": "www.thank.at",
        "website_short": uuid.uuid4().hex
    }
]


def get_strip_uuid():
    return uuid.uuid4().hex

print(get_strip_uuid())

def create_new_short_url(website_original):
    short = get_strip_uuid()
    dic = {
        "id": (len(urls) + 1),
        "website_original": website_original,
        "website_short": short
    }
    urls.append(dic)
    return dic

print(len(urls))
create_new_short_url('another.org')
print(len(urls))