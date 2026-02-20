from abc import ABC, abstractmethod
from typing import Any, List, Optional, Dict, Union


# для SensorStream: "high", "critical", "warning"
# для TransactionStream: "large", "medium", "small"
# для EventStream: "error", "warning", "info"

class DataStream(ABC):
    def __init__(self, stream_id: str, stream_type: str):
        """initialization"""
        self.stream_id = stream_id
        self.stream_type = stream_type
        self.processed_count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data"""
        pass

    def filter_data(self, data_batch: List[Any], criteria: Optional[str]
                    = None) -> List[Any]:
        """Filter data based on criteria"""
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics"""
        return {"stream_id": self.stream_id,
                "stream_type": self.stream_type,
                "processed_count": self.processed_count}


class SensorStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id, "Environmental Data")
        self.avg_temp: float = 0
        print("Initializing Sensor Stream...")
        print(F"Stream ID: {stream_id}, Type: Environmental Data")

    def process_batch(self, data_batch: List[Any]) -> str:
        temps = []
        for item in data_batch:
            if "temp" in item:
                temps.append(item["temp"])
        if temps:
            self.avg_temp = sum(temps) / len(temps)
        else:
            self.avg_temp = 0.0
        self.processed_count += len(data_batch[0])
        return f"avg temp: {self.avg_temp:.1f}°C"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        base = super().get_stats()
        base["avg_temp"] = self.avg_temp
        return base


class TransactionStream(DataStream):
    pass


class EventStream(DataStream):
    pass


class StreamProcessor:
    pass


def main():
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")
    ss = SensorStream("SENSOR_001")
    data_batch = [{"temp": 22.5, "humidity": 65, "pressure": 1013}]
    print(f"Processing sensor batch: {data_batch}")
    ss.process_batch(data_batch)
    print(F"Sensor analysis: {ss.processed_count} readings processed, avg temp: {ss.avg_temp}")


if __name__ == "__main__":
    main()
