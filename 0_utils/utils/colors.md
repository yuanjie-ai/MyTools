```python
class Colors(object):
    def __init__(self, color='BLUE'):
        self.color = color
        self.__colors = {
            'BLACK': '\033[90m%s\033[0m',
            'RED': '\033[91m%s\033[0m',
            'GREEN': '\033[92m%s\033[0m',
            'YELLOW': '\033[93m%s\033[0m',
            'BLUE': '\033[94m%s\033[0m',
            'PURPLE': '\033[95m%s\033[0m',
            'CYAN': '\033[96m%s\033[0m',
            'WHITE': '\033[97m%s\033[0m',
        }

    def __call__(self, string='Hello World!!!'):
        print(self.__colors[self.color] % string)

if __name__ == '__main__':
    Colors('YELLOW')('aaaaaaaaaa')
```
