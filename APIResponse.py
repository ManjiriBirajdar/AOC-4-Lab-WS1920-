class Response:
    def __init__(self, response_id, success):
        self.response_id = response_id
        self.success = success


class GetResponse(Response):
    def __init__(self, response_id, success, component):
        super().__init__(response_id, success)
        self.component = component


class PostResponse(Response):
    def __init__(self, response_id, success, component_id):
        super().__init__(response_id, success)
        self.component_id = component_id


class PutResponse(Response):
    def __init__(self, response_id, success, component_id):
        super().__init__(response_id, success)
        self.component_id = component_id


class DeleteResponse(Response):
    def __init__(self, response_id, success, component_id):
        super().__init__(response_id, success)
        self.component_id = component_id

