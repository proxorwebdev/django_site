def inspect_model_vars(self):
    return "; ".join(["%s: %s" % (f.name, getattr(self,f.name)) for f in self._meta.fields])

class Debug:
    messages = []

    @staticmethod
    def add(message):
        Debug.messages.append(message)

class DebugMessagesMiddleware():
    def process_response(self, request, response):
        print 'Yahoo!!!'
        messages = Debug.messages
        debug_text = ''.join(messages)

        response.content = debug_text + response.content

        return response
