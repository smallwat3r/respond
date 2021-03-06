from .abs_http_response import HTTPResponse

from flask import jsonify, make_response, Response

from typing import Optional, Any


class JSONResponse(HTTPResponse):

    @classmethod
    def _make_response(cls, status: int, data: Optional[Any] = None, headers: Optional[dict] = None, **kwargs):
        """ Returns a JSON response """
        response: Response = make_response(jsonify(data if data is not None else ""), status)
        if headers:
            for k, v in headers.items():
                response.headers.set(k, v)
        return response
