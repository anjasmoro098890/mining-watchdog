from minewd.algo.hasher import hash_job
from minewd.config import MinerConfig
from minewd.core.controller import MineController
from minewd.stratum.jobs import JobQueue


def test_hash_stable() -> None:
    assert hash_job(b"abc", 1) == hash_job(b"abc", 1)


def test_hash_nonce_changes() -> None:
    assert hash_job(b"abc", 1) != hash_job(b"abc", 2)


def test_job_queue() -> None:
    q = JobQueue()
    q.push("pool", 0)
    assert q.latest() is not None
    assert q.latest().job_id


def test_bench() -> None:
    report = MineController(MinerConfig()).bench(8)
    assert report["rounds"] == 8
    assert report["hashes"] == 8


def test_submit() -> None:
    ctrl = MineController(MinerConfig())
    assert ctrl.submit(3) is True
    assert ctrl.client.accepted == 1


def test_config_algo() -> None:
    assert MinerConfig().algo
