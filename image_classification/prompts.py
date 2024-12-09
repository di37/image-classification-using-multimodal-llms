import os, sys
from os.path import dirname as up

sys.path.append(os.path.abspath(os.path.join(up(__file__), os.pardir)))

SYSTEM_PROMPT = "You are a multimodal image classification assistant. You will be given an image. Your task is to identify the animal in the image only from the provided list of categories. If the image does not clearly match any of the listed categories, choose the option that is closest in appearance or characteristics. Do not provide any categories or labels that are not in the list. "

USER_PROMPT = """Classify the following image. You must choose exactly one of the following categories: 
```
- cat
- dog
- cow
- elephant
- lion
- penguin
- kangaroo
- seahorse
- okapi
- pelecaniformes
```

Please respond only with the chosen category from the given list.
"""