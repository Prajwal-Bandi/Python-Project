"""
Batch average-age calculation module.

Provides threaded and async implementations to compute
average ages of patients in batches of N (default from config).
"""

import asyncio
from concurrent.futures import ThreadPoolExecutor
from .crud import SessionLocal, Patient
from .config import BATCH_SIZE


def _calc_avg_age_batch(patients):
    """Helper: calculate average age for one batch."""
    total = sum(p.age for p in patients)
    return total / len(patients) if patients else 0


def batch_average_age_threaded(batch_size: int = BATCH_SIZE):
    """
    Calculate average age of patients in batches using threads.
    Returns a list of averages (one per batch).
    """
    session = SessionLocal()
    patients = session.query(Patient).all()
    session.close()

    batches = [patients[i:i + batch_size] for i in range(0, len(patients), batch_size)]
    results = []

    with ThreadPoolExecutor() as executor:
        results = list(executor.map(_calc_avg_age_batch, batches))

    return results


async def _calc_avg_age_batch_async(patients):
    """Async helper for one batch."""
    await asyncio.sleep(0) 
    return _calc_avg_age_batch(patients)


async def batch_average_age_async(batch_size: int = BATCH_SIZE):
    """
    Calculate average age of patients in batches using asyncio.
    Returns a list of averages (one per batch).
    """
    session = SessionLocal()
    patients = session.query(Patient).all()
    session.close()

    batches = [patients[i:i + batch_size] for i in range(0, len(patients), batch_size)]
    coros = [_calc_avg_age_batch_async(batch) for batch in batches]
    results = await asyncio.gather(*coros)
    return results


if __name__ == "__main__":
    import asyncio
    from app.logger import logger

    logger.info("Running batch average age calculations...")

    try:
        avg_threaded = batch_average_age_threaded(batch_size=10)
        logger.info(f"Threaded batch average age: {avg_threaded}")

        avg_async = asyncio.run(batch_average_age_async(batch_size=10))
        logger.info(f"Async batch average age: {avg_async}")
    except Exception as e:
        logger.error(f"Batch calculation failed: {e}")

