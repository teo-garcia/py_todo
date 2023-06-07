def get_int(input_message, error_message = "Invalid number. Please try again."):
  while True:
    try:
      value = int(input(input_message))
      return value
    except ValueError:
      print(error_message)

def get_string(input_message, error_message = "Invalid string. Please try again."):
  while True:
    try:
      value = int(input(input_message))
      if value.strip():
        return value
    except ValueError:
      print(error_message)
