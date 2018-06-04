from aop import Aspect


class InvocationLoggerAspect(Aspect):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)


    def around(self, *args, **kwargs):
        self.logger.info(
            'aspectType-around-before-Invocation: name=%s, args=%s, kwargs=%s' % (
                self.function,
                args,
                kwargs
            )
        )
        response = self.execute(*args, **kwargs)
        self.logger.info(
            'aspectType-around-after-Invocation: name=%s, args=%s, kwargs=%s,response=%s' % (
                self.function,
                args,
                kwargs,
                response
            )
        )
        # self.execute(*args, **kwargs)