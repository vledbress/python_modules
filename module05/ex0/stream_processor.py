from abc import ABC, abstractmethod
from typing import Any


class ValidationError(Exception):
    """Custom validation exception"""
    pass


class DataProcessor(ABC):
    @abstractmethod
    def process(self, data: Any) -> str:
        """processes data and returns string"""
        pass

    @abstractmethod
    def validate(self, data: Any) -> bool:
        """validates if data is appropriate"""
        pass

    def format_output(self, result: str) -> str:
        """Formats the output string"""
        return f"Output: {result}"


class NumericProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        """validates if data is appropriate"""
        if not isinstance(data, list):
            return False
        for i in data:
            if not isinstance(i, (int, float)):
                return False
        return True

    def process(self, data: Any) -> str:
        """processes data and returns string"""
        if not self.validate(data):
            raise (ValidationError("Failed data validation"))
        return (F"Processed {len(data)} numeric values, sum = {sum(data)},"
                F" avg = {sum(data) / len(data)}")

    def format_output(self, result: str) -> str:
        """Formats the output string"""
        return super().format_output(result)


class TextProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        """validates if data is appropriate"""
        if not isinstance(data, str):
            return False
        return True

    def process(self, data: Any) -> str:
        """processes data and returns string"""
        if not self.validate(data):
            raise (ValidationError("Failed data validation"))
        return (F"Processed text: {len(data)} characters,"
                F" {len(data.split())} words")

    def format_output(self, result: str) -> str:
        """Formats the output string"""
        return super().format_output(result)


class LogProcessor(DataProcessor):
    def validate(self, data: Any) -> bool:
        """validates if data is appropriate"""
        if not isinstance(data, str):
            return False
        return True

    def process(self, data: Any) -> str:
        """Processes log data"""
        if not self.validate(data):
            raise ValidationError("Failed data validation")
        level, message = data.split(":", 1)
        level = level.strip().upper()
        message = message.strip()
        prefix = "[ALERT]" if level == "ERROR" else f"[{level}]"
        return f"{prefix} {level} level detected: {message}"

    def format_output(self, result: str) -> str:
        """Formats the output string"""
        return super().format_output(result)


def main():
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")
    np = NumericProcessor()
    print("Initializing Numeric Processor...")
    data = [1, 2, 3, 4, 5]
    try:
        print(F"Processing data: {data}")
        res = np.process(data)
        print("Validation: Numeric data verified")
        print(np.format_output(res))
    except ValidationError as e:
        print(e)
    print()

    tp = TextProcessor()
    print("Initializing Text Processor...")
    data = "Hello Nexus World"
    try:
        print(F"Processing data: {data}")
        res = tp.process(data)
        print("Validation: Text data verified")
        print(tp.format_output(res))
    except ValidationError as e:
        print(e)
    print()

    lp = LogProcessor()
    print("Initializing Log Processor...")
    data = "ERROR: Connection timeout"
    try:
        print(F"Processing data: {data}")
        res = lp.process(data)
        print("Validation: Log entry verified")
        print(lp.format_output(res))
    except ValidationError as e:
        print(e)
    print()

    print("=== Polymorphic Processing Demo ===")
    print("Code Nexus Polymorphic Data Streams in the Digital Matrix")
    print("Processing multiple data types through same interface...")

    polymorphic_data = [
        ([1, 2, 3], NumericProcessor()),
        ("Hello Nexus", TextProcessor()),
        ("INFO: System ready", LogProcessor())
    ]

    for i in range(len(polymorphic_data)):
        data, processor = polymorphic_data[i]
        result = processor.process(data)
        print(f"Result {i+1}: {result}")
    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()
