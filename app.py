try:
    result = 5 + "hello"
except TypeError as e:
    print(f"Caught an exception: {e}")
except Exception as e:
    print(f"Caught a general exception: {e}")
finally:
    print("This will always run.")
