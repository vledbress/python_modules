from abc import ABC, abstractmethod
from typing import Any, List, Optional, Dict, Union, Protocol


class Stage(Protocol):
    def process(self, data: Any) -> Any:
        ...


class InputStage:
    pass


class TransformStage:
    pass


class OutputStage:
    pass


class ProcessingPipeline(ABC):
    def __init__(self):
        self.stages: List[Stage] = []
        self.pipeline_id: str

    def add_stage(self, stage: Union[Stage]):
        self.stages.append(stage)

    def process(self, data: Any) -> Any:
        pass


class JSONAdapter(ProcessingPipeline):
    pass


class CSVAdapter(ProcessingPipeline):
    pass


class StreamAdapter(ProcessingPipeline):
    pass


class NexusManager:
    def __init__(self):
        self.pipelines: List[ProcessingPipeline] = []


def main():
    print("Ilka pidor")


main()
