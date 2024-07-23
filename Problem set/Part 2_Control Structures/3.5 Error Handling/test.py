my_other_var = 1
try:
    result = 10 // my_var
    print(result)
except (ZeroDivisionError, TypeError):
    print("An expected error occurred!")
else:
    print("No errors occurred!")
finally:
    print("Closing down...")
print("Done!")