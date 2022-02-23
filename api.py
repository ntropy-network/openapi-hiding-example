import connexion


app = connexion.FlaskApp('hiding-example')


def some_nice_endpoint():
    return "I am nice, but nothing lasts forever", 201


def yet_another_endpoint():
    return "I am different, but who cares?", 201


if __name__ == '__main__':
    app.add_api('openapi.yaml')
    app.run(port=8080)
