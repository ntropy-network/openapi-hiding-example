import connexion
import yaml


app = connexion.FlaskApp('hiding-example')


def some_nice_endpoint():
    return "I am nice, but nothing lasts forever", 201


def yet_another_endpoint():
    return "I am different, but who cares?", 201


def new_shiny_endpoint():
    return "I new and shiny", 201


@app.route("/openapi.json", endpoint="_openapi_json")
def _openapi_json():
    openapi_yaml_path = "openapi.yaml"

    with open(openapi_yaml_path) as openapi_yaml:
        openapi = yaml.safe_load(openapi_yaml)

    hidden_endpoints = []
    for path, methods in openapi["paths"].items():
        for method, endpoint in methods.items():
            print(f"{path} {method}")
            if endpoint.get("x-hidden"):
                hidden_endpoints.append((path, method))

    for path, method in hidden_endpoints:
        del openapi["paths"][path][method]

    return openapi


if __name__ == '__main__':
    app.add_api(
        'openapi.yaml',
        options={"serve_spec": False},
    )
    app.run(port=8080)
