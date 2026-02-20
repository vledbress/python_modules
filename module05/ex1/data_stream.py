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
        self.streams: list[DataStream] = []
        self.filtered_summary: list[str] = []

    def add_stream(self, stream: DataStream):
        """Добавить поток в процессор"""
        self.streams.append(stream)

    def process_mixed_batches(self, batches: list[list[str]]):
        """
        batches: список батчей для потоков, порядок соответствует self.streams
        """
        self.filtered_summary.clear()

        # Проходим по индексам потоков
        for i in range(len(self.streams)):
            stream = self.streams[i]
            batch = batches[i]

            # Фильтрация критических данных
            critical_batch = stream.filter_data(batch, criteria="critical")

            # Обработка батча (обновляет processed_count и stats)
            _ = stream.process_batch(batch)

            # Счётчик критических элементов для отчёта
            count = len(critical_batch)

            # Формируем строку отчёта по типу потока
            if isinstance(stream, SensorStream):
                print(f"- Sensor data: {len(batch)} readings processed")
                self.filtered_summary.append(f"{count} critical sensor alerts")
            elif isinstance(stream, TransactionStream):
                print(f"- Transaction data: {len(batch)} operations processed")
                self.filtered_summary.append(f"{count} large transactions")
            elif isinstance(stream, EventStream):
                print(f"- Event data: {len(batch)} events processed")
                self.filtered_summary.append(f"{count} error events")

        # Финальный отчёт
        print("Stream filtering active: High-priority data only")
        print("Filtered results:", ", ".join(self.filtered_summary))


def main():
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    # === Инициализация потоков ===
    ss = SensorStream("SENSOR_001")
    print("Initializing Sensor Stream...")
    print(f"Stream ID: {ss.stream_id}, Type: {ss.stream_type}")
    sensor_batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: {sensor_batch}")
    print(ss.process_batch(sensor_batch))  # avg temp: 22.5°C

    ts = TransactionStream("TRANS_001")
    print("\nInitializing Transaction Stream...")
    print(f"Stream ID: {ts.stream_id}, Type: {ts.stream_type}")
    transaction_batch = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: {transaction_batch}")
    print(ts.process_batch(transaction_batch))  # net flow: +25 units

    es = EventStream("EVENT_001")
    print("\nInitializing Event Stream...")
    print(f"Stream ID: {es.stream_id}, Type: {es.stream_type}")
    event_batch = ["login", "error", "logout"]
    print(f"Processing event batch: {event_batch}")
    print(es.process_batch(event_batch))  # 1 error detected

    # === Polymorphic Stream Processing ===
    processor = StreamProcessor()
    processor.add_stream(ss)
    processor.add_stream(ts)
    processor.add_stream(es)

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...")
    print("Batch 1 Results:")

    # Используем батчи, которые могут дать нужные "critical" результаты
    # В примере критические: 2 sensor alerts, 1 large transaction, 3 events
    mixed_batches = [
        ["temp:35", "temp:10"],              # SensorStream (2 critical)
        ["buy:200", "buy:50", "sell:150", "buy:75"],  # TransactionStream (1 large)
        ["login", "error", "logout"]         # EventStream (1 error)
    ]
    processor.process_mixed_batches(mixed_batches)

    print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":
    main()
