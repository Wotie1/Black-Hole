
import sys
import ctypes
import logging
import platform
from dataclasses import dataclass

# --- PROJECT: BLACK HOLE ---
# Güvenli disk hasarı simülasyonu.
# Diske yazmaz ve sistemi çökertmez.

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(message)s",
    datefmt="%H:%M:%S"
)

BUFFER_SIZE = 1024 * 1024  # 1 MB
SIMULATED_SIZE_MB = 500


@dataclass
class SimulationConfig:
    drive: str = r"\\.\PhysicalDrive0"
    buffer_size: int = BUFFER_SIZE
    simulated_size_mb: int = SIMULATED_SIZE_MB


def check_environment():
    """Çalışma ortamını kontrol eder; sistem ayarlarını değiştirmez."""
    logging.info("İşletim sistemi: %s", platform.system())
    logging.info("Python sürümü: %s", platform.python_version())

    if platform.system() != "Windows":
        logging.info(
            "Windows'a özgü işlemler devre dışı; "
            "simülasyon modunda devam ediliyor."
        )

    logging.info("Ortam kontrolü tamamlandı.")


def simulate_disk_write(config):
    """
    Ham disk yazma işlemini simüle eder.
    Fiziksel sürücü açılmaz ve gerçek veri silinmez.
    """
    logging.info("--- PROJECT: BLACK HOLE ---")
    logging.info("Hedef (temsili): %s", config.drive)
    logging.info("Simüle edilen blok boyutu: %d byte", config.buffer_size)
    logging.info("Simüle edilen toplam alan: %d MB",
                 config.simulated_size_mb)

    for i in range(1, config.simulated_size_mb + 1):
        if i % 50 == 0 or i == config.simulated_size_mb:
            percent = i / config.simulated_size_mb * 100
            logging.info(
                "Simülasyon ilerlemesi: %d/%d MB (%.0f%%)",
                i,
                config.simulated_size_mb,
                percent
            )

    logging.info("Simülasyon tamamlandı.")
    logging.info("Fiziksel diske hiçbir veri yazılmadı.")


def simulate_system_failure():
    """Sistem çökmesi senaryosunu yalnızca mesajlarla temsil eder."""
    logging.warning("Sanal sistem arızası senaryosu başlatıldı.")
    logging.warning("Gerçek bir sistem hatası tetiklenmedi.")
    logging.info("İşletim sistemi çalışmaya devam ediyor.")


def main():
    try:
        check_environment()

        config = SimulationConfig()
        simulate_disk_write(config)
        simulate_system_failure()

        return 0

    except (OSError, ValueError, RuntimeError) as error:
        logging.error("Simülasyon hatası: %s", error)
        return 1

    except KeyboardInterrupt:
        logging.warning("Simülasyon kullanıcı tarafından durduruldu.")
        return 130


if __name__ == "__main__":
    sys.exit(main())
