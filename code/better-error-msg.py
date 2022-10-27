# Better Error Massages


def get_info():
    return {
        "user": {
            "name": "aerosadegh",
            "first_name": "Sadegh",
            "last_name": "Yazdani",
            "age": 30,
        },
        "job": {"name": "programmer", "title": "Python Developer"},
    }


def main():
    info = get_info()
    return f'{info["user"]["username"]}: {info["user"]["first_name"]} {info["user"]["last_name"]} with {info["job"]["titlle"]}'


if __name__ == "__main__":
    print(main())