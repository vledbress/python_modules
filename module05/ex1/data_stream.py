from abc import ABC, abstractmethod
from typing import Any, List, Optional, Dict, Union


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
        self.avg_temp: float = 0.0

    def process_batch(self, data_batch: List[str]) -> str:
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
        return (f"Sensor analysis: {self.processed_count} readings processed,"
                f"avg temp: {self.avg_temp:.1f}°C")

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        base = super().get_stats()
        base["avg_temp"] = self.avg_temp
        return base

    def filter_data(self, data_batch: List[str], criteria: Optional[str]
                    = None) -> List[str]:
        """
        Фильтруем данные по критичности:
        - criteria="critical": temp < 15 или temp > 30
        - criteria="normal" или None: остальные температуры
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
    def __init__(self, stream_id: int):
        super().__init__(stream_id, "Financial Data")
        self.netflow = 0

    def process_batch(self, data_batch: List[str]) -> str:
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
        return (F"Transaction analysis: {self.processed_count} opearations,"
                F" net flow: {sign}{self.netflow} units")

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        base = super().get_stats()
        base["netflow"] = self.netflow
        return base

    def filter_data(self, data_batch: List[str], criteria: Optional[str]
                    = None) -> List[str]:
        """
        Фильтруем транзакции:
        - criteria="critical": buy/sell > 100
        - criteria="normal" или None: остальные
        """
        critical, normal = [], []
        for item in data_batch:
            pair = item.split(":")
            if len(pair) != 2:
                continue
            key, value = pair
            try:
                amount = int(value)
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
    def __init__(self, stream_id: str):
        super().__init__(stream_id, "System Events")
        self.errors = 0

    def process_batch(self, data_batch: List[str]) -> str:
        for i in data_batch:
            if i == "error":
                self.errors += 1
        self.processed_count += len(data_batch)
        return (F"Event analysis: {self.processed_count} events, "
                F"{self.errors} error detected")

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        base = super().get_stats()
        base["errors"] = self.errors
        return base

    def filter_data(self, data_batch: List[str], criteria: Optional[str]
                    = None) -> List[str]:
        """
        Фильтруем события:
        - criteria="critical": только 'error'
        - criteria="normal" или None: все остальные события
        """
        critical = [item for item in data_batch if item == "error"]
        normal = [item for item in data_batch if item != "error"]
        if criteria == "critical":
            return critical
        return normal


class StreamProcessor:
    def __init__(self):
        self.streams: List[DataStream] = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)


def main():
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    ss = SensorStream("SENSOR_001")
    data_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: {data_batch}")
    print(ss.process_batch(data_batch))

    data_batch = ["buy:100", "sell:150", "buy:75"]
    ts = TransactionStream("TRANS_001")
    print(f"Processing sensor batch: {data_batch}")
    print(ts.process_batch(data_batch))

    es = EventStream("EVENT_001")
    data_batch = ["login", "error", "logout"]
    print(f"Processing sensor batch: {data_batch}")
    print(es.process_batch(data_batch))


if __name__ == "__main__":
    main()
