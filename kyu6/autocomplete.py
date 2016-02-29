import re

def autocomplete(input_, dictionary):
    input_ = re.sub('[^a-zA-Z]', '', input_)
    return [d for d in dictionary if d.lower().startswith(input_)][:5]
