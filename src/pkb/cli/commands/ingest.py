from pkb.services.ingestion_service import IngestionService


def run(lot_number: int) -> None:
    IngestionService.run(lot_number)
