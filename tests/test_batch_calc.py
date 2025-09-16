import pytest
# import asyncio
from app.models import Patient
from app.batch_calc import batch_average_threaded, batch_average_async


@pytest.fixture
def sample_patients():
    return [Patient(name=f"Patient{i}", age=i, disease="Test") for i in range(1, 21)]


def test_batch_average_threaded(sample_patients):
    results = batch_average_threaded(sample_patients, batch_size=5)
    assert len(results) == 4   # 20 patients / batch of 5 = 4 batches
    assert all(isinstance(r, float) for r in results)


@pytest.mark.asyncio
async def test_batch_average_async(sample_patients):
    results = await batch_average_async(sample_patients, batch_size=5)
    assert len(results) == 4
    assert all(isinstance(r, float) for r in results)
