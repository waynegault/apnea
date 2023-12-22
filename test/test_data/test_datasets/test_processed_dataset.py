import os

import pytest
from src.data.datasets.processed_dataset import ProcessedDataset
from src.data.utils import get_nb_events

@pytest.fixture(scope="function")
def relative_path():
    yield '../../'

def test___getitem__(base_directory):
    data_path = os.path.join(base_directory, 'data', 'repository', 'datasets', '7d8965a5-523c-41e6-8284-8024b7036267')
    ds = ProcessedDataset(data_path=data_path, output_type='dataframe')

    assert len(ds) == 1494
    nb_events, _ = get_nb_events(ds)
    assert nb_events == 24