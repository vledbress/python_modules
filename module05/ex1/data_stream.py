from abc import ABC, abstractmethod
from typing import Any, List, Optional, Dict, Union


class DataStream(ABC):
    """
    Abstract base class representing a generic data stream.
    """

    def __init__(self, stream_id: str, stream_type: str):
        """Initialize the data stream with an ID and type."""
        self.stream_id = stream_id
        self.stream_type = stream_type
        self.processed_count = 0

    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        """Process a batch of data. Must be implemented by subclasses."""
        pass

    def filter_data(
        self, data_batch: List[Any], criteria: Optional[str] = None
    ) -> List[Any]:
        """Filter data based on specific criteria."""
        return data_batch

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return stream statistics including ID and processed count."""
        return {
            "stream_id": self.stream_id,
            "stream_type": self.stream_type,
            "processed_count": self.processed_count,
        }


class SensorStream(DataStream):
    """
    Data stream implementation for environmental sensor data.
    """

    def __init__(self, stream_id: str):
        """Initialize the sensor stream and set avg temperature to zero."""
        super().__init__(stream_id, "Environmental Data")
        self.avg_temp: float = 0.0

    def process_batch(self, data_batch: List[str]) -> str:
        """Parse temperature readings and calculate the average."""
        temps = []
        for item in data_batch:
            pair = item.split(":")
            if pair[0] == "temp":
                try:
                    temps.append(float(pair[1]))
                except ValueError:
                    print(f"Warning: invalid temperature value '{pair[1]}'")
        if temps:
            self.avg_temp = sum(temps) / len(temps)
        else:
            self.avg_temp = 0.0

        self.processed_count += len(data_batch)
        return (
            f"Sensor analysis: {self.processed_count} readings processed,"
            f"avg temp: {self.avg_temp:.1f}°C"
        )

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return sensor-specific statistics."""
        base = super().get_stats()
        base["avg_temp"] = self.avg_temp
        return base

    def filter_data(
        self, data_batch: List[str], criteria: Optional[str] = None
    ) -> List[str]:
        """
        Filter sensor data.
        Criteria='critical': temp < 15 or temp > 30.
        """
        critical, normal = [], []
        for item in data_batch:
            pair = item.split(":")
            if len(pair) != 2 or pair[0] != "temp":
                continue
            try:
                temp = float(pair[1])
            except ValueError:
                continue
            if temp < 15 or temp > 30:
                critical.append(item)
            else:
                normal.append(item)
        if criteria == "critical":
            return critical
        return normal


class TransactionStream(DataStream):
    """
    Data stream implementation for financial transactions.
    """

    def __init__(self, stream_id: str):
        """Initialize the transaction stream and set net flow to zero."""
        super().__init__(stream_id, "Financial Data")
        self.netflow = 0

    def process_batch(self, data_batch: List[str]) -> str:
        """Calculate the net flow based on 'buy' and 'sell' operations."""
        for i in data_batch:
            pair = i.split(":")
            if pair[0] == 'buy':
                self.netflow += int(pair[1])
            elif pair[0] == 'sell':
                self.netflow -= int(pair[1])
        if self.netflow > 0:
            sign = '+'
        elif self.netflow < 0:
            sign = '-'
        else:
            sign = ''
        self.processed_count += len(data_batch)
        return (
            f"Transaction analysis: {self.processed_count} operations,"
            f" net flow: {sign}{self.netflow} units"
        )

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return financial statistics."""
        base = super().get_stats()
        base["netflow"] = self.netflow
        return base

    def filter_data(
        self, data_batch: List[str], criteria: Optional[str] = None
    ) -> List[str]:
        """
        Filter transactions.
        Criteria='critical': amount > 100.
        """
        critical, normal = [], []
        for item in data_batch:
            pair = item.split(":")
            if len(pair) != 2:
                continue
            try:
                amount = int(pair[1])
            except ValueError:
                continue
            if amount > 100:
                critical.append(item)
            else:
                normal.append(item)
        if criteria == "critical":
            return critical
        return normal


class EventStream(DataStream):
    """
    Data stream implementation for system log events.
    """

    def __init__(self, stream_id: str):
        """Initialize the event stream and reset error counter."""
        super().__init__(stream_id, "System Events")
        self.errors = 0

    def process_batch(self, data_batch: List[str]) -> str:
        """Count the number of 'error' events in the batch."""
        for i in data_batch:
            if i == "error":
                self.errors += 1
        self.processed_count += len(data_batch)
        return (
            f"Event analysis: {self.processed_count} events, "
            f"{self.errors} error detected"
        )

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """Return event statistics."""
        base = super().get_stats()
        base["errors"] = self.errors
        return base

    def filter_data(
        self, data_batch: List[str], criteria: Optional[str] = None
    ) -> List[str]:
        """
        Filter events.
        Criteria='critical': only 'error' events.
        """
        critical = [item for item in data_batch if item == "error"]
        normal = [item for item in data_batch if item != "error"]
        if criteria == "critical":
            return critical
        return normal


class StreamProcessor:
    """
    Manager class to handle and process multiple data streams.
    """

    def __init__(self):
        """Initialize processor with empty streams and summary."""
        self.streams: list[DataStream] = []
        self.filtered_summary: list[str] = []

    def add_stream(self, stream: DataStream):
        """Add a data stream to the processor."""
        self.streams.append(stream)

    def process_mixed_batches(self, batches: list[list[str]]):
        """Process batches across different streams and print results."""
        self.filtered_summary.clear()
        for i in range(len(self.streams)):
            stream = self.streams[i]
            batch = batches[i]
            critical_batch = stream.filter_data(batch, criteria="critical")
            stream.process_batch(batch)
            count = len(critical_batch)
            if isinstance(stream, SensorStream):
                print(f"- Sensor data: {len(batch)} readings processed")
                self.filtered_summary.append(f"{count} critical sensor alerts")
            elif isinstance(stream, TransactionStream):
                print(f"- Transaction data: {len(batch)} operations processed")
                self.filtered_summary.append(f"{count} large transactions")
            elif isinstance(stream, EventStream):
                print(f"- Event data: {len(batch)} events processed")
                self.filtered_summary.append(f"{count} error events")
        print("Stream filtering active: High-priority data only")
        print("Filtered results:", ", ".join(self.filtered_summary))


def main():
    """Main execution point with original output format."""
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    ss = SensorStream("SENSOR_001")
    print("Initializing Sensor Stream...")
    print(f"Stream ID: {ss.stream_id}, Type: {ss.stream_type}")
    sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: {sensor_batch}")
    print(ss.process_batch(sensor_batch))

    ts = TransactionStream("TRANS_001")
    print("\nInitializing Transaction Stream...")
    print(f"Stream ID: {ts.stream_id}, Type: {ts.stream_type}")
    transaction_batch = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: {transaction_batch}")
    print(ts.process_batch(transaction_batch))

    es = EventStream("EVENT_001")
    print("\nInitializing Event Stream...")
    print(f"Stream ID: {es.stream_id}, Type: {es.stream_type}")
    event_batch = ["login", "error", "logout"]
    print(f"Processing event batch: {event_batch}")
    print(es.process_batch(event_batch))

    processor = StreamProcessor()
    processor.add_stream(ss)
    processor.add_stream(ts)
    processor.add_stream(es)

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    print("Batch 1 Results:")

    mixed_batches = [
        ["temp:35", "temp:10"],
        ["buy:200", "buy:50", "sell:150", "buy:75"],
        ["login", "error", "logout"]
    ]
    processor.process_mixed_batches(mixed_batches)
    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()