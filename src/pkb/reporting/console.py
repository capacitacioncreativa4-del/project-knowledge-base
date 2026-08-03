from pkb.reporting.report import ValidationReport


class ConsoleReporter:
    """
    Presenta en consola un ValidationReport.
    """

    @staticmethod
    def render(report: ValidationReport) -> None:

        for result in report.results:
            if result.success:
                continue

            for error in result.errors:
                print(f"[ERROR] {error}")

        if report.success:
            print("[SUCCESS] Validación completada sin errores.")
        else:
            print(
                f"[WARNING] Se encontraron {report.total_errors} errores de validación."
            )
