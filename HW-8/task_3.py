params = {'v': 'some_id',
          'list': 'some_list',
          'index': '6',
          't': '0s'}

initial_str = 'https://www.youtube.com/watch?'

print(initial_str + '&'.join([f'{key}={value}' for key, value in params.items()]))
