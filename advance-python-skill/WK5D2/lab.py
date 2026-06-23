import sys

# 1. Standard Class (Uses __dict__)
class StandardLog:
    def __init__(self, level, user_id, message):
        self.level = level
        self.user_id = user_id
        self.message = message

# 2. Optimized Class (Uses __slots__)
class SlottedLog:
    # This prevents __dict__ creation and locks down the attributes
    __slots__ = ("level", "user_id", "message")
    
    def __init__(self, level, user_id, message):
        self.level = level
        self.user_id = user_id
        self.message = message

if __name__ == "__main__":
    # Sample data
    lvl, uid, msg = "ERROR", 102938, "Connection timed out"
    
    # Instantiate both
    std_obj = StandardLog(lvl, uid, msg)
    slot_obj = SlottedLog(lvl, uid, msg)
    
    # Measure baseline object overhead (excluding the content size)
    print(f"Standard Object Size: {sys.getsizeof(std_obj)} bytes")
    print(f"Standard Object Dict Size: {sys.getsizeof(std_obj.__dict__)} bytes")
    print(f"Total Standard Overhead: {sys.getsizeof(std_obj) + sys.getsizeof(std_obj.__dict__)} bytes")
    print("-" * 40)
    print(f"Slotted Object Size: {sys.getsizeof(slot_obj)} bytes")
    
    # Proof that __dict__ is gone
    try:
        print(slot_obj.__dict__)
    except AttributeError:
        print("Confirmed: Slotted object has no __dict__ attribute!")