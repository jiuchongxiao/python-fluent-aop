
from aop import Aspect, FluentInit
from fluent import sender, event
from flask import Flask,request


fluent = FluentInit.FluentInit()


class InvocationLoggerAspect(Aspect):

    def __init__(self, *args, **kwargs):

        super().__init__(*args, **kwargs)

    def around(self, *args, **kwargs):

        aop_status = fluent.aop_status
        if aop_status == "true":
            event.Event('method-before', {
                'function': self.function.__str__(),
                'args':   args
            })
        else :
            requestArgs = request.args
            if not requestArgs is None:
                aopStatus = requestArgs.get("fluent.aopStatus")
                if aopStatus=="true":
                    event.Event('method-before', {
                        'function': self.function.__str__(),
                        'args':   args
                    })
        response = self.execute(*args, **kwargs)
        if aop_status == "true":
            event.Event('method-after', {
                'function': self.function.__str__(),
                'args':   args.__str__(),
                'response': response
            })
        else :
            requestArgs = request.args
            if not requestArgs is None:
                aopStatus = requestArgs.get("fluent.aopStatus")
                if aopStatus=="true":
                    event.Event('method-before', {
                        'function': self.function.__str__(),
                        'args':   args.__str__(),
                        'response': response
                    })

        return response