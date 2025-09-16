import asyncio
from .crud import SessionLocal, Patient
from .config import BATCH_SIZE

async def _calc_avg_age_batch_async(patients):
    await asyncio.sleep(0)  # simulate async
    total = sum(p.age for p in patients)
    return total / len(patients) if patients else 0

async def batch_average_age_async():
    session = SessionLocal()
    patients = session.query(Patient).all()
    session.close()

    batches = [patients[i:i+BATCH_SIZE] for i in range(0, len(patients), BATCH_SIZE)]
    coros = [_calc_avg_age_batch_async(batch) for batch in batches]
    results = await asyncio.gather(*coros)
    return results
