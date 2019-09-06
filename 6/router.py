#!usr/bin/python3.7.3
# -*- coding: utf-8 -*-
"""Simple router"""

class Router:
    def __init__(self):
        self.methods = {}

    def add_path(self, path, method, func):
        self.path = path
        self.method = method
        if method not in self.methods:
            self.methods[self.method] = (self.path, func)

    def request(self, method, path):
        for key, value in self.methods.items():
            if key.lower() == method.lower():
                current_path, func = value
                if current_path == path:
                    return func(path, method)
                else:
                    return 404, "Error 404: Not Found"
        else:
            return 405, "Error 405: Method Not Allowed"

    def get(self, path):
        return self.request(self.get.__name__, path)

    def post(self, path):
        return self.request(self.post.__name__, path)

    def put(self, path):
        return self.request(self.put.__name__, path)

    def patch(self, path):
        return self.request(self.patch.__name__, path)

    def delete(self, path):
        return self.request(self.delete.__name__, path)

    def options(self, path):
        return self.request(self.options.__name__, path)


def my_info(path: str, method: str) -> tuple:
    return 200, {"me": "Joanne"}


def update_me(path: str, method: str) -> tuple:
    return 200, "OK"


if __name__ == "__main__":
    router = Router()
    router.add_path("/me", "GET", my_info)
    router.add_path("/me", "POST", update_me)
    router.add_path("/me", "PUT", update_me)
    router.add_path("/me", "PATCH", update_me)
    router.add_path("/me", "DELETE", update_me)
    router.add_path("/me", "GET", my_info)
    router.add_path("/me", "OPTIONS", my_info)

    # print(router.methods)

    print(router.get("/me"))
    print(router.post("/me"))
    print(router.get("/us"))
    print(router.put("/me"))
    print(router.patch("/me"))
    print(router.delete("/local"))
    print(router.options("/me"))
