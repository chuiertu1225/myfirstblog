from rest_framework.renderers import JSONRenderer as JR

class JSONRenderer(JR):

    def render(self, data, accepted_media_type=None, renderer_context=None):
        response = renderer_context['response']
        if response.status_code == 400:
            pass
        elif response.status_code == 403:
            data = {"code": 50009, "msg": "没有权限"}
        elif response.status_code == 404:
            data = {"code": 50404, "msg": "资源不存在"}
        elif response.status_code == 405:
            data = {"code": 50010, "msg": "请求方法不允许"}
        elif isinstance(data, dict) and "code" in data:
            pass
        else:
            data = {"code": 20000, "msg": "获取成功", "data": data}
        return super(JSONRenderer, self).render(data, accepted_media_type=None, renderer_context=None)


