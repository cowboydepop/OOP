"""Python serial number generator."""

class SerialGenerator:
    """Machine to create unique incrementing serial numbers."""
    
    def __init__(self, start=0):
        """Initialize the SerialGenerator with a starting number."""
        self.start = start
        self.current = start

    def generate(self):
        """Generate the next sequential number."""
        self.current += 1
        return self.current - 1

    def reset(self):
        """Reset the number back to the original start number."""
        self.current = self.start

# Create an instance of SerialGenerator
serial = SerialGenerator(start=100)

# Generate and print serial numbers
print(serial.generate())  # Output: 100
print(serial.generate())  # Output: 101
print(serial.generate())  # Output: 102

# Reset and print the serial number
serial.reset()
print(serial.generate())  # Output: 100

if __name__ == "__main__":
    import doctest
    doctest.testmod()
