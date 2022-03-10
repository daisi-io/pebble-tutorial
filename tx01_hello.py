import sys

def hello(name=None):
    if not name:
        return "Hello world!"
    else:
        return f"Hello, {name}!"

def goodbye(who=None):
    if not who:
        return "Goodbye for now!"
    else:
        return f"Goodbye, {who}!"
        
if __name__ == "__main__":
    print(hello(sys.argv[1] if len(sys.argv) > 1 else None))
