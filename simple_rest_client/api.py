from simple_rest_client.resource import Resource


class API:
    def __init__(self, api_root_url=None, params={}, headers={}, timeout=None,
                 append_slash=False, json_encode_body=False):
        self.api_root_url = api_root_url
        self.params = params
        self.headers = headers
        self.timeout = timeout
        self.append_slash = append_slash
        self.json_encode_body = json_encode_body
        self._resources = {}

    def add_resource(self, api_root_url=None, resource_name=None,
                     resource_class=None, action_urls={}, params={},
                     headers={}, timeout=None, append_slash=False,
                     json_encode_body=False):
        resource_class = resource_class or Resource
        api_root_url = api_root_url or self.api_root_url
        params = params or self.params
        headers = headers or self.headers
        timeout = timeout or self.timeout
        json_encode_body = json_encode_body or self.json_encode_body
        resource = resource_class(
            api_root_url=api_root_url, resource_name=resource_name,
            action_urls=action_urls, params=params, headers=headers,
            timeout=timeout, append_slash=append_slash,
            json_encode_body=json_encode_body
        )
        self._resources[resource_name] = resource
        setattr(self, resource_name, resource)

    def get_resource_list(self):
        return list(self._resources.keys())